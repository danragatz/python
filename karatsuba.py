from random import randint

def mult2(m, n):
    '''
    recursive multiplacation of 2 numbers
    one of the numbers should be small
    e.g., < 10
    '''
    
    if m == 0 or n == 0: 
        return 0
    elif m < n:
        return n + mult2(n, m-1)
    else:
        return m + mult2(n-1, m)

def karatsuba(x, y):
    '''
    karatsuba multiplication of 2 numbers
    of n length. When the length of n == 1
    for one of the numbers, no more karatsuba
    slicing can be done. finish the recursion 
    by calling a recursive multiplication 
    function
    '''
    
    lx = len(str(x))
    ly = len(str(y))
    
    # get smallest length
    n = min(lx,ly)
    #print n

    # base case: n == 1; could just return x*y, but
    # want to eliminate all multiplication calls
    # other than adding zeros
    if n == 1:
        return mult2(x, y)

    # get 1/2 n rounded up
    n = n//2 + n%2
    
    # split x & y into a, b, c, d components
    mb = 10**n
    a = x // mb
    b = x %  mb
    c = y // mb
    d = y %  mb
    #print a,b,c,d
    
    # get recursive components    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
    #print ac, bd, ad_plus_bc, mb
    
    return ac * mb * mb + bd + ad_plus_bc * mb  
    
for i in range(10):
    x = randint(1,1000000)
    y = randint(1,1000000)
    
    expected = x * y
    result = karatsuba(x, y)
    
    print( "%d and %d:" % (x,y))
    print( 'expected: ', expected)
    print( 'actual:   ', result)
    if result != expected:
        print( "Error with: " + str(x) + " " + str(y))
    print()
        
