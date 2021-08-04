from django.shortcuts import HttpResponse
#127.0.0.1:8000/test-post
def testPost(request):
    if request.method == 'POST':
        return HttpResponse('Hello')

from dataclasses import dataclass, asdict
import json

@dataclass
class Student:
    number: str
    name: str
    gender: str
    birthDate: str

student_list = [
    Student('1001', 'Nguyen Van An', 'M', '2000-01-01'),
    Student('1002', 'Nguyen Thi Binh', 'F', '2001-01-01'), #trailing comma
]

#127.0.0.1:8000/get-student-info/1001
def getStudentInfo(request, number):
    #data = request.GET
    #number = data.get('number', '')
    for st in student_list:
        if st.number == number:
            return HttpResponse(json.dumps(asdict(st)))

@dataclass
class Book:
    isbn: str
    name: str
    author: str
    published_year: int

book_list = [
    Book('12321321', 'Vòng quanh thế giới trong 21 ngày', 'Nhiều tác giả', 2050),
    Book('32432434', 'Làm giàu không khó', 'Nguyễn Nông Dân', 1945),
    Book('32132132', 'Cách mạng CN 4.0', 'Nguyễn Công Nhân', 1991),
]

# 127.0.0.1:8000/get-book-info?isbn=12321321
def getBookInfo(request):
    data = request.GET
    isbn = data.get('isbn')
    for book in book_list:
        if book.isbn == isbn:
            return HttpResponse(json.dumps({
                'isbn': book.isbn,
                'name': book.name,
                'author': book.author,
                'published_year': book.published_year,
            }))

# Viet script test test_get_book_info --> lay duoc thong tin sach
