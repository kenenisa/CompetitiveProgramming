/**
 * @param {string} s
 * @return {string}
 */
 var sortSentence = function(s) {
    const splitted = s.split(' ');
    const n = splitted.length
    const sortedArray = [];
  
    for(let i = 0; i < n;i++){
        sortedArray[Number(splitted[i].slice(-1)) - 1] = splitted[i].slice(0,-1);
    }
    return sortedArray.join(' ')
};