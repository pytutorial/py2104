from django.shortcuts import HttpResponse
#127.0.0.1:8000/test-post
def testPost(request):
    if request.method == 'POST':
        return HttpResponse('Hello')

from dataclasses import dataclass, asdict

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
#127.0.0.1:8000/get-student-info?number=1001
def getStudentInfo(request):
    data = request.GET
    number = data.get('number', '')
    for st in student_list:
        if st.number == number:
            return HttpResponse(st.name)

