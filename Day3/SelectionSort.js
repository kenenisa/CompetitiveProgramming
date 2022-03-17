

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
 class Solution
 {
   select(arr,i){
      // code here such that selectionSort() sorts arr[]
      const n = arr.length
      let hold = i;
         for(let j = i+1; j < n; j++){
             if(arr[j] < arr[hold]) {
                 hold=j; 
             }
          }
      return hold
   }
 
   //Function to sort the array using selection sort algorithm.
   selectionSort(arr,n){
    //code here
    for(let i = 0; i < n;i++){
        const min = this.select(arr,i)
         if (min != i) {
              // Swapping the elements
              let tmp = arr[i]; 
              arr[i] = arr[min];
              arr[min] = tmp;      
         }
    }
    return arr;
    
   }
     
 }