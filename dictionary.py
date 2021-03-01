user_list=[]
n=int(input('Number of elemets in the list: ')) #input from user
for i in range(1,n+1):
    element=int(input(f'{i}st : '))
    user_list.append(element)   #making list of user input   

def dictionary(user_list):
        position={}   #empty dictionary

        #using dictionary comprehension {key:value for key in input} to calculate frequency of elements:
        frequency={item:user_list.count(item) for item in user_list} 

        #for Position of elements in the user_list:
        for i in range(len(user_list)):
            if user_list[i] not in position:
                 position[user_list[i]]=[i+1]
                 #to add items in the empty "position" dictionary
            else:
                position[user_list[i]].append(i+1)
                #to append the values of existing keys in "position" dictionary

        print('The user input list is:\n',user_list,'\n') 
        print('Number\tFrequency')
        for i,j in frequency.items():#to make the output look organised using \t and \n
            print(i,'\t',j)
        print('Number\tPosition')
        for i,j in position.items():
            print(i,'\t',j)        

 #calling the function       
dictionary(user_list) 
    




        
        
    

