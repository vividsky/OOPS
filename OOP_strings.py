

#### reverse of a string:####
def reverse(string):
    print(string[::-1])

####number of words in a string####
def words_in_a_string(string):
    lst_string=string.split() #split() convert the string into list
    print(len(lst_string))            

####count vowels,consonants and special characters####
def vcs(string):
    vowels=0
    consonants=0
    special_character=0
    for a in string:
        if a in '0123456789':
            pass
        elif a.lower() in'aeiou':
            vowels+=1
        elif a.lower() in'bcdfghjklmnpqrstvwxyz':
            consonants+=1
        elif a==' ':
            pass
        else:
            special_character+=1
    print(vowels,consonants,special_character)       

####return largest word in the string####
def largest_word(string):
    c=string.split()        
    max_length=0
    max_length_word=[]
    for word in c:
        if len(word)>max_length:
            max_length=len(word)
            max_length_word=[word]  #add the max length word into empty list
        elif len(word)==max_length:
            max_length_word.append(word)#add the other same length words into list
    print(max_length,max_length_word)       
        

####reverse each word of given string####

def reverse_each_word(string):
    string=string.split()
    for i in range(len(string)):
        string[i]=string[i][::-1] #reverse each element of the list 
        final_string=' '.join(string)#convert the list back into string
    print(final_string)

user_input=int(input('''1. reverse a string   
2. count number of words 
3. count vowels,consonants,special characters respectively  
4. the largest word in a string  
5. reverse each word in a string
1/2/3/4/5
'''))
if user_input==1:
    string=input('Give us a word: ')
    reverse(string)
elif user_input in range(2,6):
    string=input('Give us a string: ')
    if user_input==2:
        words_in_a_string(string)
    elif user_input==3:
        vcs(string)
    elif user_input==4:
        largest_word(string)
    elif user_input==5:
        reverse_each_word(string)

        
        
    






        

        
        
    
