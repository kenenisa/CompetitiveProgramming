/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function (itr) {
    const n = itr.length
    itr.sort((x, y) => x[0] - y[0])
    const result = [[itr[0][0], itr[0][1]]];
    for (let i = 1; i < n; i++) {
        const last = result.length - 1
        if (result[last][1] < itr[i][0]) {
            result.push(itr[i])
        } else {
            result[last][1] = result[last][1] > itr[i][1] ? result[last][1] : itr[i][1]
        }
    }


    return result
};

console.log(merge([[1,4],[4,5]]));
