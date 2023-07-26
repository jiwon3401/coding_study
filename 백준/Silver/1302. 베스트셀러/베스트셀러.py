import sys
input = sys.stdin.readline

N = int(input())
book={}
for i in range(N):
    b = input().strip()
    if b not in book:
        book[b] = 1
    else:
        book[b] = book.get(b,0)+1

print(max(dict(sorted(book.items())), key=book.get))
#[k for k,v in book.items() if max(book.values())==v]