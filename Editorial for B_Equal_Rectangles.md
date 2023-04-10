##B. Equal Rectangles

### Input
The first line of the input contains one integer 𝑞
 (1≤𝑞≤500) — the number of queries. Then 𝑞
 queries follow.

The first line of the query contains one integer 𝑛
 (1≤𝑛≤100) — the number of rectangles.

The second line of the query contains 4𝑛
 integers 𝑎1,𝑎2,…,𝑎4𝑛
 (1≤𝑎𝑖≤104), where 𝑎𝑖
 is the length of the 𝑖
-th stick.

### Output
For each query print the answer to it. If it is impossible to create exactly 𝑛
 rectangles of equal area using given sticks, print "NO". Otherwise print "YES".

## Solution 

 The most optimal way to get rectangles out of all the given sticks is to sort the sticks in a non-decreasing way and check if the first and last pair of sticks area is equal to the second and second last, the third and third last areas etc...

 More formally, let's say after sorting a, the area calculated by `a[0]` * `a[n-1]` is `K` where a is the array of sticks length and n is the number of sticks and `K` the area. `a[2]` * `a[n-3]` should also be equal to `K`. The second condition we should look out for is if `a[0]` and `a[1]` are equal and `a[n-1]` and `a[n-2]` are equal this check guarantees us that we're getting rectangles with equal opposite sides. 
 
 If all of the corresponding pair are equal and taking pairs from each side of the extreme ends of the array yields the same area then the answer would be `"YES"` otherwise `"NO"`

First example ----
1
1 1 10 10
After sorting: 1 1 10 10

The first pair: 1 1 (`a[0]` and `a[1]` are equal)
The last pair: 10 10 (`a[n-1]` and `a[n-1]` are equal)
then doing `a[0]` * `a[1]` is 10 and since there are no other rectangles to be formed the answer is `"YES"`

-----
2
10 5 2 10 1 1 2 5
After sorting: 1 1 2 2 5 5 10 10

The first pair: 1 1 (`a[0]` and `a[1]` are equal)
The last pair: 10 10 (`a[n-1]` and `a[n-2]` are equal)
then doing `a[0]` * `a[n-1]` is 10 so K=10

The first pair: 2 2 (`a[2]` and `a[3]` are equal)
The last pair: 5 5 (`a[n-3]` and `a[n-4]` are equal)
then doing `a[2]` * `a[n-3]` is 10 so K=10

Since `K=10` for both of the 2 possible rectangles the answer is `"YES"`

-----
2
10 5 1 10 5 1 1 1
After sorting: 1 1 1 1 5 5 10 10

The first pair: 1 1 (`a[0]` and `a[1]` are equal)
The last pair: 10 10 (`a[n-1]` and `a[n-2]` are equal)
then doing `a[0]` * `a[n-1]` is 10 so K=10

The first pair: 1 1 (`a[2]` and `a[3]` are equal)
The last pair: 5 5 (`a[n-3]` and `a[n-4]` are equal)
then doing `a[2]` * `a[n-3]` is 10 so K=5

Since `K=10` for the first rectangle and `K=5` for the second the answer is `"NO"`

Complexity analysis
Time complexity: **O(Nlogn)**
Space complexity: **O(1)**