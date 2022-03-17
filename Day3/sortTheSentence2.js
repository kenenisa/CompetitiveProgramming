/**
 * @param {string} s
 * @return {string}
 */
 var sortSentence = function(s) {
    const sortedArray = [];
    let word = ''
    for(let i in s){
        if(s[i] == ' '){
            word = ''
        }else if(Number(s[i])){
            sortedArray[Number(s[i]) + 1] = word
        }else{
            word += s[i]
        }   
    }
    return sortedArray.join(' ').trim()
};