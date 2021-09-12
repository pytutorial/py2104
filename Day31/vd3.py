productList = [
    {
        'name': 'IPhone X',
        'price': 10.5
    },
    {
        'name': 'IPhone 1',
        'price': 16.5
    },
    {
        'name': 'Nokia 6.1',
        'price': 4.5
    },
    {
        'name': 'IPhone 12',
        'price': 22.5
    }
]
priceMin = 10
priceMax = 20
for p in productList:
    if p['price'] >= priceMin and p['price'] <= priceMax:
        print(p['name'])


print([p['name'] for p in productList
    if p['price'] >= priceMin and p['price']<= priceMax])