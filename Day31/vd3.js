// Cho 1 bang san pham
// Moi san pham co 2 truong: ten, gia
// Cho 1 khoang gia : priceMin - priceMax
// In ra cac san pham trong khoang gia tren

var productList = [
    {
        name: 'IPhone X',
        price: 10.5
    },
    {
        name: 'IPhone 11',
        price: 16.5
    },
    {
        name: 'Nokia 6.1',
        price: 4.5
    },
    {
        name: 'IPhone 12',
        price: 22.5
    }
];
var priceMin = 10;
var priceMax = 20;
var n = productList.length;
for(var i = 0; i < n; i++) {
    var p = productList[i];
    if(p.price >= priceMin && p.price <= priceMax) {
        console.log(p.name);
    }
}

var result = productList
                .filter(p => (p.price >= priceMin && p.price <= priceMax))
                .map(p => p.name);
console.log(result);