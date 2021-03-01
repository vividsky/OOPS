string = input('Give us a string: ')  # input from user

list1 = []
dic = {'1': 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
       7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}  # dictionary of integers

for i in string:  # adding elements of string into list1
    list1.append(i)
encode = []

for i in list1:
    if i in '1234567890':  # making int into reversed string
        encode.append(dic[int(i)][::-1])
    elif i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        encode.append(str(ord(i)))  # changing str into ascii
    else:
        encode.append(i)  # appending the rest as it is
# joining the elemets of list encode with a whitespace
resulte = ' '.join(encode)
print('Encoded msg is:\n', resulte)
# printing the result
