function deepEqual(objA, objB){
    function recursiveEqual(oA, oB) {
        for (k of Object.keys(oA)) {
            if (oA[k] === oB[k]) {
                return true;
            } else if (oA[k] && oB[k] && typeof oA[k] == typeof oB[k] && typeof oA[k] === "object") {
                return recursiveEqual(oA[k], oB[k]);
            } else {
                return false;
            }
        }
    }
    return recursiveEqual(objA, objB);
} 

let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));  // true
console.log(deepEqual(obj, {here: 1, object: 2}));  // false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));  // true
console.log(deepEqual(obj, {here: null, object: 2}));  // false
