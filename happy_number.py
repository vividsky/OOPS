def sum_of_num(sqdnumber):

   sqdnumber_result = 0             #to store the sum, eg for 23==>2^2+3^2=13

   for num in sqdnumber:            #loop through string 'sqdnumber' 
      sqr_of_num = int(num)**2      #convert num into int then take square of it
      sqdnumber_result+= sqr_of_num #add and store square value in sqdnumber_result
   return sqdnumber_result

def happy_number(sqdnumber):
   if sqdnumber == '1':
      return 'Yayy!!! it is a Happy Number. ' 
   return 'Sorry, it is not a Happy Number.'

def main():

   sqdnumber = input('Give us a number: ') #eg. '123' or '23'

   #calling sum_of_num function
   print(f'Sum of squares of individual numbers of {sqdnumber}: ',sum_of_num(sqdnumber))

   i=1
   while sqdnumber != '1' and i<=10:  
      sqdnumber = str(sum_of_num(sqdnumber))  #save it back to sqdnumber in 'str' form
      i+=1                                    #increasing i by 1
  #This while loop will run till either sqdnumber=='1' or i exceeds range(10) 
   print(happy_number(sqdnumber) )                   #calling happy_number function
main()

