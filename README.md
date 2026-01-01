# 🔐 Multiprocessing Hash Cracker in Python

## 🧩 Overview

 This project implements a **CPU‑bound password hash cracking tool** using Python’s
 `multiprocessing` module.  
 The program distributes hash‑comparison tasks across multiple CPU cores to
 significantly improve performance compared to a single‑process approach.

⚠️ **This project is intended strictly for educational and authorized use only.**

## 🎯 Objectives

- Demonstrate **multiprocessing** in Python
- Apply parallelism to a **CPU‑intensive task**
- Understand process pools and early termination
- Practice safe and correct use of type annotations

## ✨ Key Features

- Uses all available CPU cores (`multiprocessing.Pool`)
- Early termination when the password is found
- Supports multiple hash algorithms via `hashlib`
- Clean command‑line interface (CLI)
- Type‑safe implementation using Python type hints
- Follows multiprocessing best practices (no worker I/O)

## ⚙️ How It Works

1. The user provides:
   - Target password hash
   - Wordlist file
   - Hashing algorithm (optional)
2. The wordlist is read and distributed among worker processes
3. Each worker:
   - Hashes a candidate password
   - Compares it with the target hash
4. As soon as a match is found:
   - The password is returned
   - All worker processes are terminated immediately

## 🗂️ Project Structure

 .  
 ├── crack.py  
 ├── passwords.txt  
 └── README.md

## 🧰 Requirements

 - Python **3.9+**
 - Standard Library only (no external dependencies)

## ▶️ Usage

 ```bash
 python crack.py -p <hash> -w <wordlist> [-a algorithm]
 ```

| Option              | Description                        |
| ------------------- | ---------------------------------- |
| `-p`, `--password`  | Target password hash (required)    |
| `-w`, `--wordlist`  | Path to wordlist file (required)   |
| `-a`, `--algorithm` | Hashing algorithm (default: `md5`) |


```bash
python crack.py \
  -p 8fa60e0ed4068a8ad2f0da8365094e98 \
  -w passwords.txt \
  -a md5
```

## 🔐 Supported Hash Algorithms

 The program supports all algorithms available in Python’s `hashlib`, including:

 - md5
 - sha1
 - sha224
 - sha256
 - sha384
 - sha512

 (Validated using `hashlib.algorithms_available`)

## 🚀 Why Multiprocessing?

 - Hash cracking is a **CPU‑bound problem**
 - Python threads are limited by the **Global Interpreter Lock (GIL)**
 - `multiprocessing` allows **true parallel execution**
 - `imap_unordered()` enables faster result retrieval and early exit

## 🧠 Design Considerations

 - Worker processes are **pure functions**
   - No printing
   - No I/O
   - No shared state
 - All output is handled by the **main process**
 - Early termination minimizes wasted CPU cycles

## ⚠️ Limitations

 - Entire wordlist is loaded into memory
    - Acceptable for small/medium wordlists
    - Streaming can be implemented as an improvement
 - Does not support salted or adaptive hashes (e.g., bcrypt)

## 🎓 Academic Relevance

 This project is suitable for:

 - Operating Systems
 - Parallel Processing
 - CPU Scheduling
 - Introduction to Cybersecurity
 - Python multiprocessing labs
 - Ethical Disclaimer

## 📜 Ethical Disclaimer

 >This tool is provided **for educational purposes only.**  
 Do not use it on systems, data, or accounts without explicit permission.  
 Unauthorized use may be illegal and unethical.

## 🔧 Possible Enhancements

 - Stream wordlist instead of loading into memory
 - Add execution time benchmarking
 - Support salted hashes
 - Replace `multiprocessing.Pool` with `ProcessPoolExecutor`
 - Add progress tracking in the main process

## 📄 License

 MIT License
 Free to use for learning, teaching, and academic projects.

👤 **Author**: Student Project  
🐍 **Language**: Python