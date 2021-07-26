import copy;

class Result:
   def __init__(self):
      self.res = []

def main(a, b, c):
    obj = {'a': a, 'b': b, 'c': c, 'curB': 0, 'curA': 0, 'actions': [], 'children': []};
    result = Result();
    genTree(obj, result, {});
    return "\n".join(result.res) + "\nsuccess";

def genTree(tree, result, dec = {}):
    if (len(result.res) < len(tree['actions']) and len(result.res) != 0):
        return False;
    if (tree['curB'] == tree['c']) :
        if (len(result.res) > len(tree['actions']) or len(result.res) == 0) :
            result.res = tree['actions'];
        return True;
    
    if (tree['curA'] == tree['c']) :
        eb = emptyB(tree);
        if (eb is None):
            return genTree(pourAB(tree), result, dec);
        else:
            return genTree(pourAB(eb), result, dec);
    
    if len(tree['actions']) > 0:
        if dec.get(str(tree['curB']) + "-" + str(tree['curA']) + tree['actions'][0]) is not None:
            return
        dec[str(tree['curB']) + "-" + str(tree['curA']) + tree['actions'][0]] = 1;
    fillA(tree);
    fillB(tree);
    pourAB(tree);
    pourBA(tree);
    emptyA(tree);
    emptyB(tree);
    for item in tree['children']:
        if genTree(item, result, dec):
            break

def fillA(obj):
    if (obj['curA'] == obj['a'] or obj['curB'] == obj['b'] or (len(obj['actions']) > 0 and obj['actions'][-1].startswith('pour') is False)):
        return None
    newObj = copy.deepcopy(obj)
    newObj['children'] = list()
    newObj['curA'] = newObj['a']
    newObj['actions'].append('fill A')
    obj['children'].append(newObj)
    return newObj

def fillB(obj):
    if (obj['curA'] == obj['a'] or obj['curB'] == obj['b'] or (len(obj['actions']) > 0 and obj['actions'][-1].startswith('pour') is False)):
        return None;
    
    newObj = copy.deepcopy(obj)
    newObj['children'] = list()
    newObj['curB'] = newObj['b'];
    newObj['actions'].append('fill B')
    obj['children'].append(newObj)
    return newObj;

def emptyA(obj):
    if (obj['curA'] == 0 or obj['curB'] == 0 or obj['b'] - obj['curA'] == obj['c']):
        return None;

    newObj = copy.deepcopy(obj)
    newObj['children'] = list()
    newObj['curA'] = 0;
    newObj['actions'].append('empty A')
    obj['children'].append(newObj)
    return newObj;

def emptyB(obj):
    if (obj['curA'] == 0 or obj['curB'] == 0):
        return None;
    newObj = copy.deepcopy(obj)
    newObj['children'] = list()
    newObj['curB'] = 0;
    newObj['actions'].append('empty B')
    obj['children'].append(newObj)
    return newObj;

def pourAB(obj):
    if (obj['curB'] == obj['b'] or obj['curA'] == 0 or obj['actions'][-1].startswith('pour')):
        return None;
    newObj = copy.deepcopy(obj)
    newObj['children'] = list()
    recNum = obj['b'] - obj['curB'];
    pourNum = recNum if obj['curA'] > recNum else obj['curA']
    newObj['curB'] += pourNum;
    newObj['curA'] -= pourNum
    newObj['actions'].append('pour A B')
    obj['children'].append(newObj)
    return newObj;


def pourBA(obj):
    if (obj['curA'] == obj['a'] or obj['curB'] == 0  or obj['actions'][-1].startswith('pour')):
        return None;
    newObj = copy.deepcopy(obj)
    newObj['children'] = list()
    recNum = obj['a'] - obj['curA'];
    pourNum = recNum if obj['curB'] > recNum else obj['curB']
    newObj['curA'] += pourNum;
    newObj['curB'] -= pourNum
    newObj['actions'].append('pour B A')
    obj['children'].append(newObj)
    return newObj;


print(main(3, 5, 4))
print(main(5, 7, 3))