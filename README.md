# ccwc - Unix `wc` Clone in Python

A fast, lightweight, and POSIX-compliant clone of the Unix `wc` (word count) command-line utility, built following [John Crickett's Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc).

## 🚀 Features

- **Byte Count (`-c`)**: Accurately counts raw binary octets.
- **Line Count (`-l`)**: Counts newline characters (`\n` / `0x0A`) matching POSIX standards.
- **Word Count (`-w`)**: Counts whitespace-delimited tokens.
- **Character Count (`-m`)**: Correctly handles multi-byte UTF-8 encodings (runes/glyphs).
- **Max Display Line Length (`-L`)**: Measures the length of the longest line.
- **Default Mode**: Outputs lines, words, and bytes when no flags are specified.
- **Standard Input (`stdin`)**: Seamlessly reads from terminal pipes (`cat file.txt | ccwc -l`).
- **Multiple Files & Totals**: Automatically prints counts for each file plus a `total` summary line.
- **Robust Error Handling**: Graceful error messages and POSIX exit codes (`0` on success, `1` on error).

---

## 🛠️ Installation & Quickstart

Clone the repository:
```bash
git clone https://github.com/your-username/ccwc.git
cd ccwc
```

### Usage

```bash
# Count bytes
python ccwc.py -c test.txt

# Count lines
python ccwc.py -l test.txt

# Count words
python ccwc.py -w test.txt

# Count UTF-8 characters
python ccwc.py -m test.txt

# Default (lines, words, bytes)
python ccwc.py test.txt

# Read from a pipe (standard input)
cat test.txt | python ccwc.py -l

# Multiple files with a total row
python ccwc.py -l file1.txt file2.txt
```

### Create a Terminal Alias
In Git Bash or Linux, add an alias to your `~/.bashrc`:
```bash
alias ccwc="python $(pwd)/ccwc.py"
```
Now you can invoke it directly:
```bash
ccwc -l test.txt
```

---

## 🧪 Automated Testing

An automated test script is included that compares `ccwc` directly against the system's native Unix `wc`:

```bash
bash test.sh
```

---

## 💡 Engineering Deep Dive (Interview Talking Points)

### 1. Bytes vs. Characters (UTF-8 Multibyte Encodings)
* In ASCII, 1 character = 1 byte.
* In UTF-8, characters are variable-length (1 to 4 bytes). Special punctuation, accented characters, and emojis occupy multiple bytes on disk.
* For `test.txt`, `ccwc -c` returns `342,190` bytes, while `ccwc -m` returns `339,292` characters. The difference represents multi-byte UTF-8 characters.

### 2. POSIX Definition of a Line
* A "line" in Unix is strictly defined as a sequence of bytes ending with a newline byte (`0x0A` or `\n`). 
* If a file contains words but no terminating `\n`, `wc -l` reports `0`.
* By scanning raw bytes with `b'\n'`, the line counter never crashes due to text encoding mismatches (like Windows `cp1252`).

### 3. Unified Streaming via Standard Input
* Command line arguments are separated into flags and targets.
* When targets are absent, the application reads directly from `sys.stdin.buffer`, enabling Unix pipeline composition (`cat ... | ccwc`).


