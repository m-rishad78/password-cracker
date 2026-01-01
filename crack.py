from hashlib import new
from hashlib import algorithms_available

from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple

from multiprocessing import Pool
from multiprocessing import cpu_count

from argparse import ArgumentParser
from pathlib import Path


def get_args() -> Tuple[str, Path, str]:
    parser = ArgumentParser()
    parser.add_argument("-p", "--password", type=str, help="Enter the password hash", required=True)
    parser.add_argument("-w", "--wordlist", type=Path, help="Enter the wordlist path", required=True)
    parser.add_argument("-a", "--algorithm", type=str, help="Enter the hashing algorithm type | default= md5")

    args = parser.parse_args()

    password_hash: str = args.password.strip()
    wordlist_path: Path = args.wordlist
    algorithm: str = args.algorithm.lower() if args.algorithm else "md5"

    return (password_hash, wordlist_path, algorithm)


def generate_hash(password: str, algorithm: str) -> str:
    return new(algorithm, password.encode()).hexdigest()


def get_wordlist(path: Path) -> Generator[str, None, None]:
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            yield line.strip()


def worker(args: Tuple[str, str, str]) -> Optional[str]:
    password, target_hash, algorithm = args

    if generate_hash(password, algorithm) == target_hash:
        return password

    return None


def crack_hash(target_hash: str, wordlist_path: Path, algorithm: str) -> None:
    try:
        if algorithm not in algorithms_available:
            raise ValueError("Invalid algorithm")

        if not wordlist_path.exists():
            raise FileNotFoundError("File not Found!")

        password_list: list[str] = list(get_wordlist(wordlist_path))

        with Pool(cpu_count()) as pool:
            args: Iterable[Tuple[str, str, str]] = ((password, target_hash, algorithm) for password in password_list)

            for result in pool.imap_unordered(worker, args, chunksize=100):
                if result is None:
                    continue

                print(f"\r[+] Password Found: {result}\n")
                pool.terminate()

                return

        print("\r[-] Password not Found!")

    except ValueError as e:
        print(f"Error: {str(e)}")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    crack_hash(*get_args())
