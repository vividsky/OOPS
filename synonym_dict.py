# creating dictionary 
myDict=dict(meaning     = 'word',        
            synonym    = 'word',
            calm       = 'pacify',
            annihilate = 'destroy',
            wipeout    = 'destroy')

# synonym_dict without recursion
def synonyms(x):
   synonym_dict={}                     #empty dictionary to store synonyms
   for key,value in myDict.items():    #looping through myDict
      if value not in synonym_dict:    #append values as keys and keys as [values]
         synonym_dict[value]=[key]     #in synonym_dict
      else:
         synonym_dict[value].append(key)#append keys of same values in list [values]
   return synonym_dict                 #return synonym_dict
print('Dictionary of synonyms with iterative method is :\n',synonyms(myDict))

# synonym_dict with recursion  
def rec_synonyms(x):     
      if x=={}:                      #base case,where x is myDict
         return dict()               #when myDict=={} return empty dict
      else:
         ele=x.popitem()             #save last item of x in ele 'where ele is a    tuple with key at index 0 and value at index 1' using .popitem()
         synonym_dict=rec_synonyms(x)#calling rec_synonyms(x) with one less item in x
         
         if ele[1] not in synonym_dict: #append values as keys and keys as [values]  
            synonym_dict[ele[1]]=[ele[0]]
         else:                          #append keys with same values in list [values]
            synonym_dict[ele[1]].append(ele[0]) 
      return synonym_dict               #return synonym_dict
print('\n\nDictionary of synonyms with recursion method is :\n',rec_synonyms(myDict)) 




  

