// 2. Program Structure
// Looping a triangle
let row = "#";
while (row.length < 8) {
    console.log(row);
    row += "#";
}

console.log("-".repeat(10));

// FizzBuzz
for (let i = 1; i < 101; i++){
    let printString = "";
    if (i % 3 == 0) {
        printString = "Fizz";
    }
    if (i % 5 == 0) {
        printString += "Buzz";
    }
    console.log(printString || i);
}

console.log("-".repeat(10));

// Chessboard
size = 8;
let output = "";
for (let y = 0; y < size; y++){
    for (let x = 0; x < size; x++) {
        output += (x + y) % 2 ? " " : "#";
    }
    output += "\n";
}
console.log(output);

/*
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
*/

