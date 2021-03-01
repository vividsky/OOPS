z=int(input('int 1 to product : '))  # input one from user
b=int(input('int 2 to product : '))  #input 2 from user
def prod(z,b):
   if z==0 or b==0:                 #base case when any of the number is zero
      return 0      
   elif b>0:                       #covering the case when z is negative
      return z+ prod(z,b-1) 
   elif z>0:                       #covering the case when b can be negative
      return b+ prod(b,z-1) 
   else:
      b=abs(b)                 #taking mod as -- =+ and calling the fun                
      z=abs(z)
      return prod(z,b)            
print('product of z and b is :',prod(z,b))

#calculating the length of a string:
text=input('text to check length and to reverse/is palindrome: ').strip()
def len_str(text):
    if text=='':             #base case when str is empty
        return 0
    else:
        return 1+ len_str(text[1:])  #adding one everytime and calling the function  
print('length of the string is :',len_str(text))

#reversing the string:
def reverse(text):
    if text=='':                   #base case when str got empty
        return ''
    else:
        return text[-1]+ reverse(text[:-1])   #concate last ele as first and calling the function again removing that last ele
print('reverse of the string is: ',reverse(text))

# check whether a string is palindrom or not:
def is_pal(text):
    if len(text)==0 or len(text)==1: 
        return True
    elif text[0]!=text[-1]:         #checking if first ele== last ele
        return False    
    else:
        return is_pal(text[1:-1])   #calling the func removing first last ele     
print('is the string palindrome?: ',is_pal(text))


list1=[[1,[0,2],7],2,3,4,[5,6]]
# flattening a list
copy_list=[]
flatten=[]
def flatten_list(list1):
    if list1==[]:                  #base case when list got empty
        return flatten
    else:
        if type(list1[0])==list:   #if ele is list recurse within that ele
            flatten_list(list1[0])
        else:
            flatten.append(list1[0])  #else append that ele in flatten list
        return flatten_list(list1[1:])  #recall the function from index 1 onward
print('\nFlattening the nested list1: ',flatten_list(list1))


#copy of a list
def list1Copy(list1):
   if list1==[]:                   #base case when list got empty
        return copy_list
   else:                           #append the ele at respective index to copy_list
        copy_list.append(list1[0])
   return  list1Copy(list1[1:])   #recall the function from index 1 onward
print('\ncopy list of list1 is: \n',list1Copy(list1))
print('\nMemory location of list1 and its copy ',id(list1[0][1]), id(copy_list[0][1]))
      #to cross check the memory location id of the elements

# DeepCopy of a list
def DeepCopy(list1):
    if list1==[]:                   #base case when list got empty
        return list()
    else:
        deep_copy=DeepCopy(list1[:-1])  
        if type(list1[-1])!=list:       
            deep_copy.append(list1[-1])
        else:
            deep_copy.append(DeepCopy(list1[-1]))    
    return deep_copy
deep=DeepCopy(list1)
print('\nDeepcopy of list1 :',deep)
print('\nMemory location of list1 and its deepcopy ',id(list1[0][1]), id(deep[0][1]))
'''
In deep copy, our list1 is [[1,[0,2],7],2,3,4,[5,6]],
after deep_copy=DeepCopy(list1[:-1]) , list1 is [[1,[0,2],7],2,3,4]
then [[1,[0,2],7],2,3] and soo on..
till list1=[]
then it will return empty list in deep_copy and at this point list1=[[1,[0,2],7]]
then we will check whether last ele of list1 is list or not if yes then repeat the same process else append the ele in deep_copy and return back deep_copy
continuing the same way it we traverse through each ele of the list1 and keep on appending the ele in deep_copy n at finally return the deepCopy
'''