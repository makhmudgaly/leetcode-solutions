/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    if (arr.length <= 1) return arr
    
  let mid = Math.floor(arr.length / 2)
  // Recursive calls
  let left = sortBy(arr.slice(0, mid),fn)
  let right = sortBy(arr.slice(mid),fn)
  return merge(left, right,fn)
};

function merge(left, right, fn) {
  let sortedArr = [] // the sorted items will go here
  while (left.length && right.length) {
    
    if (fn(left[0]) < fn(right[0])) {
      sortedArr.push(left.shift())
    } else {
      sortedArr.push(right.shift())
    }
  }
  
  return [...sortedArr, ...left, ...right]
}