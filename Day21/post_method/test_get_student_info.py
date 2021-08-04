import requests
import json

text = requests.get('http://127.0.0.1:8000/get-student-info/1001').text
print(text)
student = json.loads(text)
print(f'Tên: {student["name"]}, ngày sinh: {student["birthDate"]}')