// 3. Functions
// Minimum
// arrow function
const min = (a, b) => a < b ? a : b;

console.log(min(0, 10));  // 0
console.log(min(0, -10));  // -10


// Recursion
// function value
const isEven = function (v) {
    if (v < 0) return isEven(-v);  // (v + 2)
    return v > 1 ? isEven(v - 2) : v == 0;
};

console.log(isEven(50));  // true
console.log(isEven(75));  // false
console.log(isEven(-1));  // false


// Bean counting
/* Function declarations
   are not part of the regular top-to-bottom flow of control.
   So I can put countChar below it's caller.
*/
function countBs(s) {
    return countChar(s, "B");
} 

function countChar(s, char) {
        let count = 0;
    for (i = 0; i < s.length; i++ ) {
        if (s[i] === char) count++;
    }
    return count;
}

console.log(countBs("BOB"));  // 2
console.log(countChar("kakkerlak", "k"));  // 4
