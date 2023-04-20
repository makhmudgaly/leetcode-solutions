/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let ans = []
    let idx = 0
    for(let elem of arr) {
        ans.push(fn(elem, idx))
        idx += 1
    }
    
    return ans
};