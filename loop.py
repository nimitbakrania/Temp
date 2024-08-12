l = []
n=0
while n <72:
    for a in range(1,8):
        for b in range(a+1, 9):
            l.append((a+n,b+n))
    n +=8
    
i =0
while i < 63:
    for a in range(1,9):
        for b in range(a+1, 10):
            l.append((a+n+i,b+n+i))
    i +=9

r =0
while r <63:
    for a in range(1,9):
        for b in range(a+1, 10):
            l.append((a+n+i+r,b+n+i+r))
    r +=9

k =0
while k <96:
    for a in range(1,8):
        for b in range(a+1, 9):
            l.append((a+n+i+r+k,b+n+i+r+k))
    k +=8