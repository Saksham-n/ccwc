import sys

# ---------------------------------------------
# Part 1: Figure out what the user typed
# ---------------------------------------------
flag = None
filename = None

for arg in sys.argv[1:]:
    if arg.startswith("-"):
        flag = arg
    else:
        filename = arg

# ---------------------------------------------
# Part 2: Read the data (from file or pipe)
# ---------------------------------------------
if filename != None:
    with open(filename, "rb") as f:
        content = f.read()
else:
    content = sys.stdin.buffer.read()

# ---------------------------------------------
# Part 3: Calculate the counts
# ---------------------------------------------
line_count = content.count(b"\n")
word_count = len(content.split())
byte_count = len(content)

# ---------------------------------------------
# Part 4: Decide if we should show a filename
# ---------------------------------------------
if filename != None:
    name_to_print = " " + filename
else:
    name_to_print = ""

# ---------------------------------------------
# Part 5: Print the output
# ---------------------------------------------
if flag == "-c":
    print(f"  {byte_count}{name_to_print}")
elif flag == "-l":
    print(f"  {line_count}{name_to_print}")
elif flag == "-w":
    print(f"  {word_count}{name_to_print}")
elif flag == "-m":
    text_content = content.decode("utf-8")
    char_count = len(text_content)
    print(f"  {char_count}{name_to_print}")
else:
    print(f"  {line_count}  {word_count}  {byte_count}{name_to_print}")