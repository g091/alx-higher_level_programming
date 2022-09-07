#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let i = 0;
  const x = Number(process.argv[2]);

  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
