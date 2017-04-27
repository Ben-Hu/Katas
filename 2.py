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
