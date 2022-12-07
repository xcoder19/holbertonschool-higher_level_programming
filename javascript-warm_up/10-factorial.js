#!/usr/bin/node
const myArgs = process.argv.slice(2);
const intarg = parseInt(myArgs[0]);
if (intarg) {
  console.log(fact(intarg));
} else {
  console.log(NaN);
}

function fact (n) {
  if (n === 0 || n === NaN) return 1;
  else {
    return n * fact(n - 1);
  }
}
