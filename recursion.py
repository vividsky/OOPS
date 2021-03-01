#sum of elements of list
list1=[1,2,3,4,5]
text='abcd'
def sum1(list1):
    if len(list1)==1:
        return list1[0]
    else:
        return list1[0]+sum1(list1[1:])      
print(sum1(list1))        


#calculating the length of a string:
def len_str(text):
    if text=='':
        return 0
    else:
        return 1+ len_str(text[1:])   
print(len_str(text))

#reversing the string:
def reverse(text):
    if text=='':
        return ''
    else:
        return text[-1]+ reverse(text[:-1])
print(reverse(text))

# check whether a string is palindrom or not:
def is_pal(text):
    if len(text)==0 or len(text)==1: 
        return True
    elif text[0]!=text[-1]:
        return False    
    else:
        return is_pal(text[1:-1])        
print(is_pal(text)) 

#sum of n terms:
n=4
def s(n):
    if n==1:
        return 1
    return n+s(n-1)  
print(s(n))       

# hand shake of n people:
def hand(n):
    if n==1:
        return 0
    else:
        return (n-1)+hand(n-1)
print(hand(n))

# consonants of text:
def cons(text):
    if len(text)==0:
        return 0
    elif text[0] not in 'aeiou':
        print(text[0],'is consonant')
        return 1+cons(text[1:])
    else:
        print(text[0],'is vowel')
        return cons(text[1:])        
print(cons(text))  
z=3
b=2
def prod(z,b):
   if z==0 or b==0:
      return 0
   else:
      return z+prod(z,b-1)       
print(prod(z,b))  

# list1=[1,2,3,4,5]
# list2=[[1,7],[2,3],4,[5,6]]
copy_list=[]
def list1Copy(list1):
    if list1==[]:
        return copy_list
    else:
        copy_list.append(list1[0])
        return  list1Copy(list1[1:])
print('\ncopy list of list1 is: \n',list1Copy(list1))
print('\nIs list1 is list1Copy: ',list1 is list1Copy(list1))

list2=[1,[2,3],4,[5,6]]
deep_copy=[]
flatten=[]

def deepCopy(list2):
    if list2==[]:
        return deep_copy
    else:
        deep_copy.append(list2[0])
        return deepCopy(list2[1:])        
print('\ndeep copy of list2 is :\n' ,deepCopy(list2))   
print('\nIs list2 is deepCopy: ',list2 is deepCopy(list2))         

def flatten_list(list2):
    if list2==[]:
        return flatten
    else:
        if type(list2[0])==list:
            flatten_list(list2[0])
        else:
            flatten.append(list2[0])
        return flatten_list(list2[1:])
print(flatten_list(list2))