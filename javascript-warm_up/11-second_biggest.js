#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  let max1 = 0;
  let max2 = 0;
  myArgs.forEach((x) => {
    if (parseInt(x) > max1) {
      max1 = parseInt(x);
    }
  });
  myArgs.forEach((x) => {
    if (parseInt(x) > max2 && parseInt(x) !== max1) {
      max2 = parseInt(x);
    }
  });
  console.log(max2);
}
