import sys
input = sys.stdin.readline

n = int(input())
books = {}

for i in range(n) :
    newBook = input().strip()
    if newBook in books :
        books[newBook] += 1
    else :
        books[newBook] = 1

books = list(books.items())

print(sorted(books, key = lambda x : (-x[1], x[0]))[0][0])