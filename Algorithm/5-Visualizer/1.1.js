let values = [];
let states = []; // 0: default, 1: being sorted, 2: pivot

//>Generate Ramdom array
// In the p5.js version, I generate a random array where each element represents the height of a bar. For example, the code creates an array like:
function setup() {
  createCanvas(600, 400);
  values = new Array(width / 10);
  for (let i = 0; i < values.length; i++) {
    values[i] = random(height);
// This means every time you run it, you'll have a new array of random numbers (bar heights).
//<Generate Ramdom array
    states[i] = 0;
  }
  quickSort(values, 0, values.length - 1);
}

async function quickSort(arr, start, end) {
  if (start >= end) return;
  let index = await partition(arr, start, end);
  states[index] = 0;
  await Promise.all([
    quickSort(arr, start, index - 1),
    quickSort(arr, index + 1, end)
  ]);
}

async function partition(arr, start, end) {
  let pivotValue = arr[end];
  let pivotIndex = start;
  states[end] = 2; // Mark pivot

  for (let i = start; i < end; i++) {
    states[i] = 1;
    if (arr[i] < pivotValue) {
      await swap(arr, i, pivotIndex);
      pivotIndex++;
    }
    states[i] = 0;
  }
  await swap(arr, pivotIndex, end);
  states[end] = 0;
  return pivotIndex;
}

async function swap(arr, a, b) {
  await sleep(50);
  let temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function draw() {
  background(0);
  for (let i = 0; i < values.length; i++) {
    stroke(255);
    if (states[i] === 2) fill(255, 0, 0);
    else if (states[i] === 1) fill(0, 255, 0);
    else fill(255);
    rect(i * 10, height - values[i], 10, values[i]);
  }
}
