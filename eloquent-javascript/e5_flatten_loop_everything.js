// 5. Higher-Order Functions

// Flattening
let arrays = [[1, 2, 3], [4, 5], [6]];
console.log(arrays.reduce((a, b) => a.concat(b), []));  // [ 1, 2, 3, 4, 5, 6 ]


// Your own loop
function loop(value, test, update, body) {
    if (!test(value)) return;
    body(value);
    loop(update(value), test, update, body);
}

loop(3, n => n > 0, n => n - 1, console.log);


// Everything
function every1(array, predicate) {
    for (let element of array) {
        if (!predicate(element)) return false;
    }
    return true;
}

console.log(every1([1, 3, 5], n => n < 10));  // true
console.log(every1([2, 4, 16], n => n < 10));  // false
console.log(every1([], n => n < 10));  // true

function every2(array, predicate) {
    return !array.some((element) => !predicate(element));
}

console.log(every2([1, 3, 5], n => n < 10));  // true
console.log(every2([2, 4, 16], n => n < 10));  // false
console.log(every2([], n => n < 10));  // true
