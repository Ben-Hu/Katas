import math 
def string_chunk(string, n):
    res = []
    tmpstr = string
    for i in range(0, int(math.ceil(len(string) / float(n)))):
        res.append(tmpstr[:n])
        tmpstr = tmpstr[n:]
    return res

def pattern(n):
    res = ""
    arr = []
    for i in range(1, n + 1):
        res = res + str(i)
        arr.append(i)
    tres = res
    for i in range(0, len(arr) - 1):
        plen = len(str(arr[i]))
        res = res + '\n' + tres[plen:]
        tres = tres[plen:]
    return res

def pattern1(n):
    pat = map(str, xrange(1,n+1))
    return "\n".join("".join(pat[i:]) for i in xrange(n))

def total(arr):
    res = 0
    if len(arr) == 1:
        return res
    else:
        res = arr[0] + arr[1]
        res = res + total(arr[1:])
    return res

def pattern2(n):
    pat1 = map(str, xrange(1,n+1))
    res = ""
    for i in xrange(n):
        res = res + "\n"+ ("".join(pat1[i:] + pat1[:i])) 
    return res[1:]

def insert_dash(num):
    res = [int(i) for i in str(num)]
    i = 0
    while i < len(res) -1:
        if (res[i] % 2 != 0) & (res[i+1] % 2 != 0):
            t1 = res[:i+1]
            t2 = res[i+1:]
            t1.append("-")
            res = t1 + t2
            i += 1
        i += 1
    res = map(str, res)
    return "".join(res)
        
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def push(head, data):
    return Node(data, head)
  
def build_one_two_three():
    return Node(1(Node(2, Node(3))))

def multiplication_table(row, col):
    res = [range(1, col + 1)]
    for i in range(res[0][1], row + 1):
        res.append(map((i).__mul__, res[0]))
    return res

def multiplication_table2(r, c):
    return [range(1, c+1)]+[map((i).__mul__, range(1, c+1)) for i in range(2, r+1)]

def multiplication_table3(r, c):
    return [map((i).__mul__, range(1, c+1)) for i in range(1, r+1)]

def diamond(n):
    if n % 2 == 0: 
        return None
    else: 
        diamond = ''
        lvls = filter(lambda x: x%2 == 1, range(1,n+1) + list(reversed(range(1, n+1)))[1:])
        for i in range(0, n):
            diamond = diamond + lvls[i] * '*' + '\n'
    return diamond

def diamond2(n):
    return ''.join(map(lambda x: ('*'*x)+'\n', filter(lambda x: x%2 == 1, range(1,n+1) + list(reversed(range(1, n+1)))[1:])))

def diamond3(n):
    if n % 2 == 0 or n < 0: return None
    print ''.join(map(lambda x: (' '*((n-x)/2) + '*'*x)+'\n', filter(lambda x: x%2 == 1, range(1,n+1) + list(reversed(range(1, n+1)))[1:]))) 
    return ''.join(map(lambda x: (' '*((n-x)/2) + '*'*x)+'\n', filter(lambda x: x%2 == 1, range(1,n+1) + list(reversed(range(1, n+1)))[1:])))    

def retardmode(n):
    return ''.join(map(lambda x: (' '*((n-x)/2) + '*'*x)+'\n', filter(lambda x: x%2 == 1, range(1,n+1) + list(reversed(range(1, n+1)))[1:])))    


def dirReduc(arr):
    opps = {'NORTH':'SOUTH','SOUTH':'NORTH','EAST':'WEST','WEST':'EAST'}
    tarr = arr
    c = 0
    while c < len(tarr) and len(tarr) > 1:
        if opps[tarr[c]] == tarr[c+1]:
            tarr = tarr[:c] + tarr[c+2:]
            c = 0
        else:
            c = 1
    return tarr

def abbreviate(s):
    import re
    w = filter(lambda x: len(x) > 3, re.split('[-.,;:\'\" ]', s)) 
    return ''.join([w[i][0] + str(len(w[i][1:-1])) + w[i][-1] + '-' for i in range(0, len(w))])[:-1]
#sat'balloon; sat. double-barreled. mat-mat, cat. 
#Input: sat'balloon; sat. double-barreled. mat-mat, cat. : 's22e-b11t-m08 ' should equal "sat'b5n; sat. d4e-b6d. mat-mat, cat. "


#Input: 
#sits-a-monolithic-the-mat. monolithic-monolithic, : 
#'s02s-a00a-m08c-t01e-m13c-m10 ' should equal '
#s2s-a-m8c-the-mat. m8c-m8c, '


def abbreviate(s):
    import re
    w = filter(None, re.split(r'([-.,;:\'\" ])', s))
    return ''.join([w[i][0] + str(len(w[i][1:-1])) + w[i][-1] if len(w[i]) > 3 else w[i] for i in range(0, len(w))])
    
def rotate(arr, n):
    for i in range(abs(n)):
        arr = arr[n/-abs(n):] + arr[:n/-abs(n)] 
    return arr    

def f(n, m):
    import operator
    print map(lambda x: x % m, xrange(1, n + 1))
    return reduce(operator.add, map(lambda x: x % m, xrange(1, n + 1)), 0)

def foo():
    lineCount = 1
    #lambda x: x + 1
    def test():
        print 'test'
    if 1 == 69:
        print 'a'
    else:
        print 'b'
        
import dis 
dis.dis(foo)

import math
import operator
class Vector():
    def __init__(self, arr):
        self.arr = arr
        
    def add(self, x):
        return map((lambda y: y + x), self.arr)
        
    def subtract(self, x):
        return map((lambda y: y - x), self.arr)
    
    def dot(self, x):
        return map((lambda y: y * x), self.arr)
        
    def norm(self):
        return math.sqrt(reduce(operator.add, map(lambda y: y**2, self.arr), 0))
    
def lcm(*args):
    import fractions
    tlcm = 1
    for i in range(len(args)):
        tlcm = args[i] * tlcm // fractions.gcd(args[i], tlcm)
    return tlcm

if __name__ == "__main__":
    print lcm(5,15,3)
    print lcm(3,5)