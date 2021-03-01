number=int(input('Give us a number: '))
def list_of_factorials(x):
   if x<0:
      print('Give us a positive integer: ')
   elif x==0 or x==1:
      return 1
   else:
      factorials=[]                    #creating list of all factorial values
      factorial_value=1                
      for i in range(1,x+1):          #calculating factorials for numbers upto x and appending into list 'factorials'
         factorial_value*=i
         factorials.append(factorial_value)
      return factorials    
    
def factorial_ascending(x):
   factorials=list_of_factorials(x)    #calling the function and saving the result value in factorials
   print('\nFor ascending order:\n')
   for j in range(1,x+1):
      print(f'Factorial of {j} is : {factorials[j-1]}')  #printing factorial values
def factorial_descending(x):
   print('\n\nFor descending order:\n')
   factorials=list_of_factorials(x)
   for j in range(x,0,-1):            #reversing the list elements and printing the factorial values
      print(f'Factorial of {j} is : {factorials[j-1]}')   

factorial_ascending(number)             
factorial_descending(number)