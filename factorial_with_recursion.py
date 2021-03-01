def factorial_recursion(x):              
   if x>1:
      result=factorial_recursion(x-1)*x
      factorial_list.append(result)      #saving the result into list 'factorial_list'
   else:
      result=1 
      factorial_list.append(1)   
   return result
number=int(input('\nGive us a number: ')) #user input   
factorial_list=list()                     #to keep list in global frame so that functions can use it
def main():
   factorial_recursion(number)            #calling but not printing factorial_recursion()               

   print('\nFor ascending order:\n ')
   for i in range(1,number+1):            # printing the factorial values 
      print(f'Factorial of {i} is {factorial_list[i-1]}')   

   print('\n\nFor descending order:\n ')          
   for i in range(number,0,-1):           #reversing the list and printing the factorial values
      print(f'Factorial of {i} is {factorial_list[i-1]}')
if __name__=='__main__':
   main()      