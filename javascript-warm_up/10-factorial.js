#!/usr/bin/node
const myArgs = process.argv.slice(2);
const intarg = parseInt(myArgs[0]);
if (intarg) {
  console.log(fact(intarg));
} else {
  console.log(1);
}

function fact (n) {
  if (n === 0 || isNaN(n)) return 1;
  else {
    return n * fact(n - 1);
  }
}
