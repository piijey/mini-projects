// 4. Data Structures: Objects and Arrays

// The sum of a range
function range(start, end, step = start < end ? 1 : -1) {
    let numbers = [];
    const endCondition = step > 0 ? (i) => i <= end : (i) => i >= end;
    for (let i = start; endCondition(i); i += step) {
        numbers.push(i);
    }
    return numbers;
}

function sum(array) {
    let result = 0;
    for (let element of array) result += element;
    return result;
}
console.log(range(1, 10));
console.log(range(5, 2, -1));
console.log(sum(range(1, 10)));


// Reversing an array
function reverseArray(inArray) {
    let outArray = [];
    for (let i = inArray.length -1 ; i >= 0; i--) {
        outArray.push(inArray[i]);
    }
    return outArray;
}

let myArray = ["A", "B", "C"];
console.log(reverseArray(myArray));  // [ 'C', 'B', 'A' ]
console.log(myArray);  // [ 'A', 'B', 'C' ]

function reverseArrayInPlace(inArray) {
    for (let i = 0; i < Math.floor(inArray.length / 2); i++) {
        // Keep It Simple, Stupid (KISS)
        // let a = inArray[i];
        // let b = inArray[inArray.length - 1 - i];
        // inArray[i] = b;
        // inArray[inArray.length - 1 - i] = a;
        // swap values by destructuring assignment
        [inArray[i], inArray[inArray.length - 1 - i]] = [inArray[inArray.length - 1 - i], inArray[i]];
    }
}

let arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
