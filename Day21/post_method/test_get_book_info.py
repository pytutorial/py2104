import requests
import json

text = requests.get('http://127.0.0.1:8000/get-book-info?isbn=12321321').text
print(text)
book = json.loads(text)
print(f'Tên: {book["name"]}, tác giả: {book["author"]}')