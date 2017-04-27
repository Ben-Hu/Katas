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



