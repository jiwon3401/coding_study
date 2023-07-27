import sys
input = sys.stdin.readline
s = input().strip()
String = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        String.add(s[i:j+1])

print(len(String))