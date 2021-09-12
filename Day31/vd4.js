// Cho bang order san pham
// Tinh tong doanh so
var orderList = [
    {
        productName: 'IPhone X',
        qty: 1,
        priceUnit: 10.5
    },
    {
        productName: 'Nokia 6.1',
        qty: 2,
        priceUnit: 4.5
    },
    {
        productName: 'IPhone 12',
        qty: 1,
        priceUnit: 22.5
    }
];
var total = 0;
var n = orderList.length;
for(var i = 0; i < n; i++) {
    var o = orderList[i];
    console.log(o.qty, o.priceUnit);
    var subTotal = o.qty * o.priceUnit;
    total += subTotal;
}
console.log(total);