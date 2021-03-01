
user_list = []
list_no_copy=[]
list_freq=[]
list_of_multiples=[]
num = int(input("Enter number of elements : "))#asked user for num of elements in list
for i in range(0, num): 
    element = int(input()) #saving every input into empty user_list
    user_list.append(element)
#here we made list out of outputs

def no_copy(user_list):
    for i in user_list :
        if i not in list_no_copy:#appending unique num in initial empty list empty list
            list_no_copy.append(i)
        else:
            pass
    print(list_no_copy)

def frequency(user_list):
    list_freq.append(user_list[0]) #to save first entry without looping
    for j,i in zip(range(1,num+1),user_list[1:num+1]):#looks simoultaneously for j and i 
            list_freq.append(i+list_freq[j-1])       #in respective ranges
    #j loops from 1 to num, i loops within the user_list        
    print(list_freq)


no_copy(user_list),frequency(user_list)  #calling functions  


number=int(input('Give us a number: '))
def multiples(number):
    for i in range(1,number+1):
        a=[i*k for k in range(1,6)] #list comprehension to create list of multiples
        list_of_multiples.append(a)
        
    print(list_of_multiples)

multiples(number)    #calling function multiples



    








    
    
    
