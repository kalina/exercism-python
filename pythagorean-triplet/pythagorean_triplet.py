#need to look at this as it should be refactored to be more efficient


from math import sqrt
from fractions import gcd

def primitive_triplets(n):
    out = []
    if n % 4 != 0:
        raise ValueError("Must be divisible by 4")
    for a in range(3,n+1):
        for b in range(4,n*n+1):
          if ((a-b) % 2) == 0 or a > b: continue
          cf = sqrt(a*a+b*b)
          c = int(cf)
          #if a == n:
            #  print a,b,c
          if c == cf and (a==n or b == n or c == n) and gcd(a,b) == 1 :
              out.append((a,b,c))

    return set(out)
def primitive_triplet(n):
    out = []
    if n % 4 != 0:
        raise ValueError("Must be divisible by 4")



def triplets_in_range(start, limit ):
    out = []
    for i in range(start, limit+1):
        #print i
        xx = i * i
        y = i + 1
        z = y + 1
        #print i, y, z
        while (z <= limit):
            zz = xx + y * y
            #print i, y, z, zz
            while(z * z < zz):
                z = z + 1
            #print z, zz
            if (z*z == zz and z <= limit):
                out.append((i,y,z))
                #print i,y,z
            y = y + 1
    return set(out)


def is_triplet(b):
    return (b[0] * b[0] + b[1] * b[1] == b[2] * b[2]
    or b[0] * b[0] + b[2] * b[2] == b[1] * b[1]
    or b[1] * b[1] + b[2] * b[2] == b[0] * b[0])
