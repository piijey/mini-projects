// 4. Data Structures: Objects and Arrays

// List
function arrayToList(array) {
    let list = null;
    for (let i = array.length -1 ; i >= 0; i--) {
        list = { value: array[i], rest: list};
    }
    return list;
}

function listToArray(list) {
    array = [];
    /*
    let v = true;
    while (true) {
        [v, list] = [list?.value, list?.rest];
        if ( !v ) break;
        array.push(v);
    }
    */
    for (let node = list; node; node = node.rest) {
        array.push(node.value);
    }
    return array;
}

console.log(arrayToList([10, 20]));  // { value: 10, rest: { value: 20, rest: null } }
console.log(listToArray(arrayToList([10, 20, 30])));  // [ 10, 20, 30 ]

const prepend = (v, r) => ({ value: v, rest: r });

console.log(prepend(10, prepend(20, null)));  // { value: 10, rest: { value: 20, rest: null } }

/*
function nth(list, n) {
    let v = undefined;
    for (let i = 0; i <= n && list; i++ ) {
        [v, list] = [list?.value, list?.rest];
    }
    return v;
}
*/

function nth(list, n) {
    if (!list) return undefined;
    if (n == 0) return list.value;
    else return nth(list.rest, n - 1);
}

console.log(nth(arrayToList([10, 20, 30]), 1));  // 20

