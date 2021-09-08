// Cho 1 day so
// In ra cac so bang tong 2 so lien truoc
var lst = [1, 2, 4, 6, 7, 4, 3, 8, 2, 10];

var n = lst.length;
for(var i =0; i < n; i++) {
    if(lst[i] == lst[i-1] + lst[i-2]) {
        console.log(lst[i]);
    }
}