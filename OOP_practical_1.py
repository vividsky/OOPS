
a=input('Enter first integer: ')
b=input('Enter second integer: ')
c=input('Enter third integer: ')
def main(a,b,c):
    if a>b and a>c:
        print(a,'is largest integer.')
    elif b>a and b>c:
        print(b,'is largest integer.')
    elif c>a and c>b:
        print(c,'is largest integer.')
    else:
        print('All are same')
main(a,b,c)


#grade calculations
grade=input('marks you got: ')
if grade>=90:
    print('A')
elif grade>=80:
    print('A-')
elif grade>=70:
    print('B')
elif grade>=60:
    print('B-')
elif grade>=50:
    print('C')
elif grade>=40:
    print('C-')
else:
    print('you fail the exam')



for n in range(1,num):
    if n%num==0:
        print([n])
    else:
        print('not prime')
    
   
        
    
    

