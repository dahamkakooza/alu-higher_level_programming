#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1; // Factorial of NaN or 0 is 1
  }
  return n * factorial(n - 1); // Recursive call
}

const [,, arg] = process.argv;
const num = parseInt(arg);
console.log(factorial(num));
