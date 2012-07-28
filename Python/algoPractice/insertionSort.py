## Insertion sort demo
a = [5, 6, 1, 9, 4, 3, 10]
print 'Original sequence: ', a
for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = key
print 'Sorted sequence: ', a
