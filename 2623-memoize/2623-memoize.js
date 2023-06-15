/**
 * @param {Function} fn
 */
function memoize(fn) {
    let state = {}
    return function(...args) {
        const key = JSON.stringify(args)
        
        if (key in state) {
            return state[key]
        }
        
        const res = fn.apply(this, args)
        
        state[key] = res
        return res
        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */