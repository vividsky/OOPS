n=int(input('Give us a number: '))
num=n #used in ques l
#a
def a(n):
    print('part a')
    for i in range(1,n+1):
        for j in range(1,i+1):               
            print(j,end=' ')
        print()  
  
#c
def c(n):
    print('\n\npart c')
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=' ')
        print()

#d
def d(n):
    print('\n\npart d')
    for i in range(1,n+1):
        print(f'{i} '*i)

#e
def e(n): 
    print('\n\npart e')       
    k=1
    for i in range(k,n+1):
        print(' '*(k-1),end='')
        for j in range(k,n+1):
            print(j,end='')
        print()    
        k+=1

#f
def f(n):
    print('\n\npart f')
    for i in range(1,n+1):
        if i==1 or i==n:
            print('* '*n)
        elif 1<i<n+1:
            for j in range(1,n+1):
                if j==1: 
                    print('*',end=' ')
                elif 1<j<n:
                    print(' ',end=' ')
                elif j==n:
                    print('*')    

#g
def g(n):
    print('\n\npart g')
    for i in range(n):
        print('* '*n)

#h
def h(n): 
    print('\n\npart h')       
    if n%2==0:
        print('Give us an odd number: ')
    else:
        for i in range(1,n*2,2):
            print(' '*n,end='')
            print('*'*i)
            n-=1

            
#j
def j(n): 
    print('\n\npart j')       
    k=0
    if n%2==0:
        print('give us an odd number:')
    else:    
        for i in range(2*n-1,k,-2):
            print(' '*k,end=' ')
            print('*'*i)
            k+=1


#l
def l(n):
    print('\n\npart l')            
    if n%2==0:
        print('Give us an odd number: ')
    else:
        for i in range(1,n*2,2):
            print(' '*n,end='')
            print('*'*i)
            n-=1
        k=0
        n=num                   #here I have used the value of n from num 
        for i in range(n*2-3,k,-2):      #so that we can use original value of n even after above looping
                print(' '*(k+1),end=' ')
                print('*'*i)
                k+=1         
            

#m
def m(n):
    print('\n\npart m')            
    k=0
    for i in range(n,0,-1):
        print(' '*k,end='')
        print('$'*i)
        k+=1


#n    
def n_part(n):
    print('\n\npart n')
    for i in range(1,n+1):
        print(' '*n,end=' ')
        print('#'*i)
        n-=1
        
a(n),c(n),d(n),e(n),f(n),g(n),h(n),j(n),l(n),m(n),n_part(n)

            
                   
        
        
    
        
        

    

                

    
        
    
    
    
    
        
