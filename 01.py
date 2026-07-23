# This file contains the first exercise of the Python book. It explores the print function and input function.
print ('Hello, World!')
print ('What is your name?')
myName = input() #gives the user option to input their name and save it in the myName variable. Remember, write the question first, then the input function.
print ('It is good to meet you, ' + myName) 
print ('The length of your name is:')
print (len(myName))
print ('What is your age?')
myAge = input() #here the myAge variable is stored as a string before being converted to an integer. This is because the input function always returns a string.
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')