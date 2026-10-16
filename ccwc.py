import sys
flag = sys.argv[1]
filename = sys.argv[2]
if flag == '-c':
    with open(filename, 'rb') as f:
        byte_count = len(f.read())
    print(f"  {byte_count} {filename}")
elif flag == '-l':
    with open(filename, 'rb') as f:
        line_count = f.read().count(b'\n')
    print(f"  {line_count} {filename}")
elif flag=='-w':
    with open(filename,'rb') as f:
        word_count=len(f.read().split())
    print(f"{word_count} {filename}")
    
        

