#!/usr/bin/node
if (isNaN(process.argv[2]) || (process.argv[2] === undefined)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  const x = Number(process.argv[2]);
  for (i; i < x; i++) {
    console.log('C is fun');
  }
}
