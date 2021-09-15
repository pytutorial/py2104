import requests, json, base64  

url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyBR8gU4Te36NCYlc2ZdynsOWQOS03lzWKc'

data = {
        'q': '''What's the weather like?''',
        'source': 'en',
        'target': 'vi',
        'format': 'text'
}

#headers = {"Content-Type" : "application/json"}
result = requests.post(url, data = json.dumps(data)).text
obj = json.loads(result)
print(obj)
print(obj['data']['translations'][0]['translatedText'])