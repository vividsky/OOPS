
#PRIME NUMBERS

prime_numbers=[]   #empty list    
def is_prime(num): #function to check whether a num is prime or not
    for i in range(2,num):
        if num%i==0: #will break if any int 'i' smaller thn num divide num    
            break       
    else:
        prime_numbers.append(num) #appending the numbers which are prime
def list_of_prime(num):
    for j in range(2,num+1):
        is_prime(j)     # calling the is_prime() function
    total_prime=len(prime_numbers)
    print('From 1 to ',num,'\nTotal Prime numbers  are: ',total_prime,'\n',prime_numbers) 
    #will print list of prime numbers smaller thn num
    # I/p=5 ==> O/p=[2,3,5]



#odd and even numbers less thn num:
odd=[]
even=[]
def even_odd(num):
    for i in range(1,num+1):
        if i%2==0:            #even numbers i.e. divisible by 2
            even.append(i)
        else:
            odd.append(i)     #odd numbers i.e. not divisible by 2
    print('Even numbers are ',even,'\nOdd numbers are ',odd)


#user input
num=int(input('Number upto which you want prime,odd,even numbers: '))
if num<=1:
    print('Give us a integer greater than 1:')#to filter numbers<=1
else:
    list_of_prime(num)
    even_odd(num)
print('\n\n')    


#pair of numbers whose sum is 'm'
pairs=[]
user_list=[]
no_repetition=[]
n=int(input('Number of elemets in the list: '))#input from user
for i in range(1,n+1):
    element=int(input(f'{i}st integer: '))
    user_list.append(element)#making list of input given by user    

m=int(input('Value of m: '))#input for the sum value
def pair(user_list):
    for i in user_list:
        if i not in no_repetition:
            no_repetition.append(i)     #to remove duplicates

    for j in no_repetition:
        for k in no_repetition:
           if j+k==m:    #to check for j,k such that j+k==m
              pairs.append([j,k]) #add the pair into list 'pairs'
              no_repetition.remove(j) #remove the number j from user_list to avoid repetition like [2,3],[3,2]
    print(pairs)
pair(user_list)  #calling pair function              
    
        
        
        



