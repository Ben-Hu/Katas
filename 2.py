#lol
def pick_peaks(arr):
    pos = list(filter(lambda x: (arr[x] >= arr[x-1]) and (arr[x] >= arr[x+1]) and (arr[x] != arr[x-1]) and (set([arr[x]]) | set(arr[x:]) != set([arr[x]])) and (arr[x] > [arr[n] for n in range(x,len(arr)) if arr[n] != arr[x]][0]), range(1,len(arr)-1)))
    peaks = list(map(arr.__getitem__, pos))
    return {'pos': pos, 'peaks': peaks}

#function chaining
def add(n):
    return wat(n)
    
class wat(int):
    def __call__(self, n):
        return wat(self + n)

#zzz
def make_readable(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return str(hours).zfill(2) + ':' + str(mins).zfill(2) + ':' + str(secs).zfill(2)

#move zeros
def move_zeros(array):
    i = 0
    while i < len(array):
        if array[i] == 0 and str(array[i]) != 'False' and not array[i:].count(array[i]) == len(array[i:]):
            array.append(array.pop(i))
        else:
            i += 1
    return array

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

#integer paritions
import operator
import numpy

def part(n):
    partitions = get_parts(n)
    prods = []
    while len(partitions) > 0:
          cur_part = list(partitions.pop());
          prods.append(reduce(operator.mul, cur_part, 1))
    prods = sorted(prods)
    print(prods)
    return "Range: {0} Average: {1:.2f} Median: {2:.2f}".format(prods[-1] - prods[0], sum(prods) / float(len(prods)), numpy.median(numpy.array(prods))) 

def get_parts(n):
    cur_part = set()
    cur_part.add((n, ))
    for i in range(1, n):
        for sub_part in get_parts(n - i):
            cur_part.add(tuple(sorted((i, ) + sub_part)))
    return cur_part

#pig haha
pig_it(text):
    out = text.split()
    for i in range(0,len(out)):
        if out[i][0].isalpha():
            out[i] = out[i][1:] + out[i][0] + 'ay'
    return ' '.join(out)def move_zeros(array):
        i = 0
            while i < len(array):
                        if array[i] == 0 and str(array[i]) != 'False' and not array[i:].count(array[i]) == len(array[i:]):
                                        array.append(array.pop(i))
                                                else:
                                                                i += 1
                                                                    return array
