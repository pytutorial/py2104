// Cho 1 day so, tim so chan dau tien

var lst = [ 3, 2, 1, 4, 5, 6]
var n = lst.length;
for(var i=0; i < n ; i++) {
    if(lst[i] % 2 == 0) {
        console.log(lst[i]);
        break;
    }
}

function isEven(x) {
    return x%2 == 0;
}

console.log(lst.find(isEven));     // one

console.log(lst.filter(x => x%2==0));  // multiple

// Tinh binh phuong cua cac phan tu trong day
var lst2 = []
for(var i = 0; i < n; i++) {
    var x = lst[i];
    lst2.push(x*x)
}
console.log(lst2)

var lst3 = lst.map(x => x*x);