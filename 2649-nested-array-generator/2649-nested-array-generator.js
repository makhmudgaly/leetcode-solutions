/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    if (!Array.isArray(arr)) {
        yield arr
        return
    }
    
    for (let elem of arr) {
        yield* inorderTraversal(elem)
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */