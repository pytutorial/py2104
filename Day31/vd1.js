function sum(x, y) {
    return x + y;
}
console.log(sum(2, 3))

var sum2 = function(x, y) {
    return x + y;
}
var sum3 = (x, y) => x + y;
console.log(sum3(2, 3))