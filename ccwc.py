import sys
import os

# ==============================================================================
# ccwc - Coding Challenges Clone of Unix wc (Word Count)
# Supports:
#   -c : byte count
#   -l : line count
#   -w : word count
#   -m : character count (UTF-8 decoded)
#   -L : maximum display line length
#   Default (no flags): lines, words, bytes
#   Input: File arguments or Standard Input (pipes)
#   Multiple files support with "total" line
# ==============================================================================

def process_stream(content):
    """
    Given raw bytes 'content', calculates:
    - lines: count of newline bytes (b'\n')
    - words: count of whitespace-delimited tokens
    - bytes: physical size in bytes
    - chars: character count decoded via UTF-8
    - max_line_len: length of the longest line (for -L option)
    """
    byte_count = len(content)
    line_count = content.count(b'\n')
    word_count = len(content.split())
    
    # Character count (handle UTF-8 decoding safely)
    try:
        text = content.decode('utf-8')
        char_count = len(text)
        # Maximum line length (splitlines without newlines)
        lines = text.splitlines()
        max_line_len = max((len(line) for line in lines), default=0)
    except UnicodeDecodeError:
        # Fallback for binary / non-utf8 files
        char_count = byte_count
        raw_lines = content.splitlines()
        max_line_len = max((len(line) for line in raw_lines), default=0)
        
    return {
        'lines': line_count,
        'words': word_count,
        'bytes': byte_count,
        'chars': char_count,
        'max_line': max_line_len
    }

def format_output(counts, flag, label=""):
    """
    Formats the output string according to standard wc convention.
    """
    suffix = f" {label}" if label else ""
    
    if flag == '-c':
        return f"  {counts['bytes']}{suffix}"
    elif flag == '-l':
        return f"  {counts['lines']}{suffix}"
    elif flag == '-w':
        return f"  {counts['words']}{suffix}"
    elif flag == '-m':
        return f"  {counts['chars']}{suffix}"
    elif flag == '-L':
        return f"  {counts['max_line']}{suffix}"
    else:
        # Default: lines, words, bytes
        return f"  {counts['lines']}  {counts['words']}  {counts['bytes']}{suffix}"

def main():
    flags = []
    files = []
    
    # Parse command line arguments
    for arg in sys.argv[1:]:
        if arg.startswith('-') and len(arg) > 1:
            flags.append(arg)
        else:
            files.append(arg)
            
    active_flag = flags[0] if flags else None

    # Case 1: Read from standard input (pipeline)
    if not files:
        content = sys.stdin.buffer.read()
        counts = process_stream(content)
        print(format_output(counts, active_flag, label=""))
        sys.exit(0)
        
    # Case 2: Read from one or more files
    totals = {'lines': 0, 'words': 0, 'bytes': 0, 'chars': 0, 'max_line': 0}
    has_error = False

    for file_path in files:
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            counts = process_stream(content)
            print(format_output(counts, active_flag, label=file_path))
            
            # Accumulate totals
            totals['lines'] += counts['lines']
            totals['words'] += counts['words']
            totals['bytes'] += counts['bytes']
            totals['chars'] += counts['chars']
            totals['max_line'] = max(totals['max_line'], counts['max_line'])
            
        except FileNotFoundError:
            print(f"ccwc: {file_path}: No such file or directory", file=sys.stderr)
            has_error = True
        except IsADirectoryError:
            print(f"ccwc: {file_path}: Is a directory", file=sys.stderr)
            has_error = True
        except PermissionError:
            print(f"ccwc: {file_path}: Permission denied", file=sys.stderr)
            has_error = True

    # If multiple files were provided, print a "total" summary line
    if len(files) > 1:
        print(format_output(totals, active_flag, label="total"))
        
    if has_error:
        sys.exit(1)

if __name__ == '__main__':
    main()