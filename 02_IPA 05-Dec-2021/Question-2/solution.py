
# Input:

# 3
# 3
# 1
# Halmet
# shakesphere
# 2
# Macbeth
# SHAKESPHERE
# 3
# othrllo
# Shakesphere
# A-10
# gomtinagar
# lucknow
# u.p.
# 201876
# 3
# 1
# A Christmas Carol.
# Charies Dickens
# 2
# Bleak House
# Charies Dickens
# 3
# Oliver Twist
# Charies Dickens
# A-770
# rajamandi
# agara
# u.p.
# 2018763
# 3
# 1
# The adventures of sherlock holmes
# sherlock holmes
# 2
# The return of sherlock holmes
# sherlock holmes
# 3
# The sign of the four
# sherlock holmes
# A-660
# Khairatabad
# lucknow
# u.p.
# 201876
# lucknow

class Book:
    def __init__(self,bookId,bookName,nameOfAuthor):
        self.bookId = bookId
        self.bookName = bookName
        self.nameOfAuthor = nameOfAuthor

class Library(Book):
    def __init__(self,bookLis,libraryAddress):
        self.bookLis = bookLis
        self.libraryAddress = libraryAddress

    def booksByAuthors(self):
        autDic = {}
        autLis = []
        for obj in self.bookLis:
            autLis.append(obj.nameOfAuthor.upper())
        authors = list(set(autLis))
        for aut in authors:
            autDic[aut] = autLis.count(aut)
        return autDic

def findbookType(city,libObj):
    books = []
    for obj in libObj:
        for k,v in obj.libraryAddress.items():
            if v == city:
                tempBooks=[]
                for book_obj in obj.bookLis:
                    tempBooks.append(book_obj.bookName)
                tempBooks.reverse()
                books = books + tempBooks
    return books

libObj = []
n = int(input())
for _ in range(n):
    bookList = []
    libraryAddress = {}
    for i in range(int(input())):
        bookId = int(input())
        bookName = input()
        nameOfAuthor = input()
        bookList.append(Book(bookId,bookName,nameOfAuthor))
    libraryAddress['street'] = input()
    libraryAddress['area'] = input()
    libraryAddress['city'] = input()
    libraryAddress['state'] = input()
    libraryAddress['zip'] = input()
    libObj.append(Library(bookList,libraryAddress))

city = input()
obj = libObj[0]
res = obj.booksByAuthors()
print(*res.keys(), *res.values())
books = findbookType(city,libObj)
print(books)
