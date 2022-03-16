'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {
    // Write your code here 
    const hold = arr[n - 1]
    arr[n - 1] = arr[n - 2]
    let found = false
    for (let i = n - 2; i >= -1; i--) {
        if (i == -1) {
            arr[0] = hold
        } else {
            if (arr[i] > hold) {
                arr[i + 1] = arr[i]
            } else {
                arr[i + 1] = hold
                found = true
            }
        }

        let list = ''
        arr.forEach(a => list += ' ' + a);
        console.log(list.trim())
        if (found) break;
    }
    return;
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    insertionSort1(n, arr);
}
