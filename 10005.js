function main(a, b, c) {
    const obj = { a, b, c, curA: 0, curB: 0, children: [], actions: []};
    const result = {res: []};
    genTree(obj, result);
    return result;
}

function genTree(tree, result, map = {}) {
    if (result.res.length < tree.actions.length && result.res.length != 0) {
        return;
    }
    if (tree.curA == tree.c || tree.curB == tree.c) {
        if (result.res.length > tree.actions.length || result.res.length == 0) {
            result.res = tree.actions.slice();
        }
        return true;
    }
    if (tree.curA == tree.c) {
        const eb = emptyB(tree);
        genTree(pourAB(eb || tree), result);
        return true
    }
    const fA = fillA(tree);
    const fB = fillB(tree);
    const pAB = pourAB(tree);
    const eA = emptyA(tree);
    const pBA = pourBA(tree);
    const eB = emptyB(tree);

    if (tree.curB == tree.b && tree.curA == tree.a) {
        return
    }
    // console.log(tree)
    tree.children.some(t => genTree(t, result));
}

function fillA(obj) {
    if (obj.curA == obj.a || obj.curB == obj.b || (obj.actions.length > 0 && !obj.actions[obj.actions.length - 1].startsWith('pour'))) {
        return null;
    }
    const newObj = { ...obj, children: [], actions: obj.actions.slice()};
    newObj.curA = newObj.a;
    newObj.actions.push('fill A')
    obj.children.push(newObj)
    return newObj;
}
function fillB(obj) {
    if (obj.curA == obj.a || obj.curB == obj.b || (obj.actions.length > 0 && !obj.actions[obj.actions.length - 1].startsWith('pour'))) {
        return null;
    }
    const newObj = { ...obj, children: [], actions: obj.actions.slice()};
    newObj.curB = newObj.b;
    newObj.actions.push('fill B')
    obj.children.push(newObj)
    return newObj;
}
function emptyA(obj) {
    if (obj.curA == 0 || obj.curB == 0 || obj.b - obj.curA == obj.c) {
        return null;
    }
    const newObj = { ...obj, children: [], actions: obj.actions.slice()};
    newObj.curA = 0;
    newObj.actions.push('empty A')
    obj.children.push(newObj)
    return newObj;
}
function emptyB(obj) {
    if (obj.curA == 0 || obj.curB == 0) {
        return null;
    }
    const newObj = { ...obj, children: [], actions: obj.actions.slice()};
    newObj.curB = 0;
    newObj.actions.push('empty B')
    obj.children.push(newObj)
    return newObj;
}

function pourAB(obj) {
    if (obj.curB == obj.b || obj.curA == 0 || obj.actions[obj.actions.length - 1].startsWith('pour')) {
        return null;
    }
    const newObj = { ...obj, children: [], actions: obj.actions.slice()};
    const recNum = obj.b - obj.curB;
    const pourNum = obj.curA > recNum ? recNum : obj.curA
    newObj.curB += pourNum;
    newObj.curA -= pourNum
    newObj.actions.push('pour A B')
    obj.children.push(newObj)
    return newObj;
}

function pourBA(obj) {
    if (obj.curA == obj.a || obj.curB == 0 || obj.actions[obj.actions.length - 1].startsWith('pour')) {
        return null;
    }
    const newObj = { ...obj, children: [], actions: obj.actions.slice()};
    const recNum = obj.a - obj.curA;
    const pourNum = obj.curB > recNum ? recNum : obj.curB
    newObj.curA += pourNum;
    newObj.curB -= pourNum
    newObj.actions.push('pour B A')
    obj.children.push(newObj)
    return newObj;
}

console.log(main(3, 5, 4))
