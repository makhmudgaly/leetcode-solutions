/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const group = this.reduce((acc, elem) => {
        const key = fn(elem)
        if (!acc.hasOwnProperty(key)) {
            acc[key] = []
        }
        
        acc[key].push(elem)
        return acc
    }, {})
    return group
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */