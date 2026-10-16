import sys
flag = sys.argv[1]
filename=sys.argv[2]
with open(filename, 'rb') as f:
    byte_count = len(f.read())
print(f"  {byte_count} {filename}")
