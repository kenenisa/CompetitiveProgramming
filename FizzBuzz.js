/**
 * @param {number} n
 * @return {string[]}
 */
 var fizzBuzz = function(n) {
    function FoB(i){
        if(i % 15 === 0){
            return "FizzBuzz"
        }else if(i % 3 === 0){
            return "Fizz"
        }else if(i % 3 === 0){
            return "Buzz"
        }
        return i + ''
    }
    var result = [];
    for(var i = 1; i <= n; i++){
        result.push(FoB(i))
    }
    return result
};