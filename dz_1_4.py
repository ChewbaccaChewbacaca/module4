a = str(input())

x = len(a)

i = 0

x = x - 1

k = 0

while x-i >= 0:
    if a[x-i] == a[i]:
        i += 1
    else:
        k =0
        break
if k==1:
    print('False')
else:
    print('True')