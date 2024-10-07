// 4. Data Structures: Objects and Arrays

function deepEqual(objA, objB){
    if (objA === objB) return true;
    if (objA == null || objB == null || 
        typeof objA != typeof objB || typeof objA != "object") return false;

    if (Object.keys(objA).length != Object.keys(objB).length ) return false;
    for (k of Object.keys(objA)) {
        if (!Object.keys(objB).includes(k) ||
            !deepEqual(objA[k], objB[k])) return false;
    }
    return true;
} 

let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));  // true
console.log(deepEqual(obj, {here: 1, object: 2}));  // false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));  // true

console.log("---");
console.log(deepEqual(obj, {here: null, object: 2}));  // false
console.log(deepEqual({a: 1, b: 2}, {a: 1}));  // false
console.log(deepEqual({a: {b: 1, c: 2}}, {a: {b: 1}}));  // false
console.log(deepEqual({a: null}, {a: null}));  // true
console.log(deepEqual({}, {}));  // true
console.log(deepEqual([1, 2, 3], [1, 2, 3]));  // true
