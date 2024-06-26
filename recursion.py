def nm(n):
    if n >0:
        nm(n-1)
        print(n, end= " ")
    
nm(3)

def nm_reverse(n):
    if n>0:
        print(n , end=" ")
        nm_reverse(n-1)

nm_reverse(3)

def odd_n(n):
    if n >0:
        odd_n(n-1)
        print((n-1)*2+1, end=" ")
        
odd_n(3)

def odd_n_reversed(n):
    if n >1:
        print((n-1)*2+1, end=" ")
        odd_n_reversed(n-1)
        
odd_n_reversed(3)

def even_n(n):
    if n >0:
       even_n(n-1)
       print(n*2, end=" ")

even_n(3)


def even_n_reversed(n):
    if n >0:
       print(n*2, end=" ")
       even_n_reversed(n-1)
       

even_n_reversed(3)




#class 2

