

//User function Template for javascript

/**
 *
 * select
 * @param {number[]} arr
 * @param {number} i
 * @return {number}
 *
 * selectionSort
 * @param {number[]} arr
 * @param {number} n
 */
class Solution {
    select(arr, i) {
        // code here such that selectionSort() sorts arr[]
        const n = arr.length
        let hold = i;
        for (let j = hold + 1; j < n; j++) {
            if (arr[hold] > arr[j]) {
                hold = j;
            }
        }
        return hold
    }

    //Function to sort the array using selection sort algorithm.
    selectionSort(arr, n) {
        //code here
        for (let i = 0; i < n; i++) {
            const selected = this.select(arr, i)
            if (selected !== i) {
                let hold = arr[i];
                arr[i] = arr[selected];
                arr[selected] = hold;
            }
        }
        return arr;

    }

}