// Cho truoc 1 so K > 0
// Tim n nho nhat de:
//  1 + 2 + 3 + .. n > K
const K = 1000;
var n = 0;
var S = 0;

while(S <= K){
    n += 1;
    S += n;
}
console.log(n, S)