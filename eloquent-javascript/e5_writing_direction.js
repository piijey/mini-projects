// Dominant writing direction
require("./05_higher_order/code/load")("./code/scripts.js");

function characterScript(code) {
  for (let script of SCRIPTS) {
    if (script.ranges.some(([from, to]) => {
      return code >= from && code < to;
    })) {
      return script;
    }
  }
  return null;
}

// console.log(characterScript(121));
// → {name: "Latin", …}

function dominantDirection(text) {
  const directions = {};
  for (let char of text) {
    let script = characterScript(char.codePointAt(0));
    if (script) {
      directions[script.direction] = (directions[script.direction] || 0) + 1;
    }
  }
  return Object.keys(directions).reduce((accumlator, current) =>
    directions[accumlator] > directions[current] ? accumlator : current
  );
}

console.log(dominantDirection("Hello!"));
// → ltr
console.log(dominantDirection("Hey, مساء الخير"));
// → rtl
