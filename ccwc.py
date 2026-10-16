import sys

# Step 1: Parse arguments into flag and filename
flag = None
filename = None

for arg in sys.argv[1:]:
    if arg.startswith('-'):
        flag = arg
    else:
        filename = arg

# Step 2: Read raw bytes from file or standard input
if filename:
    with open(filename, 'rb') as f:
        content = f.read()
else:
    content = sys.stdin.buffer.read()

# Step 3: Compute metrics
line_count = content.count(b'\n')
word_count = len(content.split())
byte_count = len(content)

# Label: include filename if reading from disk, omit if reading from pipe
label = f" {filename}" if filename else ""

# Step 4: Output according to the requested flag or default
if flag == '-c':
    print(f"  {byte_count}{label}")
elif flag == '-l':
    print(f"  {line_count}{label}")
elif flag == '-w':
    print(f"  {word_count}{label}")
elif flag == '-m':
    char_count = len(content.decode('utf-8'))
    print(f"  {char_count}{label}")
else:
    # Default: lines, words, bytes
    print(f"  {line_count}  {word_count}  {byte_count}{label}")