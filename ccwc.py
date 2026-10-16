import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    
    with open(filename, 'rb') as f:
        content = f.read()
        
    line_count = content.count(b'\n')
    word_count = len(content.split())
    byte_count = len(content)
    
    print(f"  {line_count}  {word_count}  {byte_count} {filename}")

elif len(sys.argv) == 3:
    flag = sys.argv[1]
    filename = sys.argv[2]
    