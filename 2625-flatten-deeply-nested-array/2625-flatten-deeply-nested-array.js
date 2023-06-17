/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, depth) {    
    const stack = [...arr.map(el => [el, depth])];
    
    const answer = [];
    
    while (stack.length > 0) {
        const [elem, depth] = stack.pop()
        
        if (Array.isArray(elem) && depth > 0) {
            stack.push(...elem.map(subElem => [subElem, depth-1]));
        } else {
            answer.push(elem)
        }
    }
    
    return answer.reverse()
};