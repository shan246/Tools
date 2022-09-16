#Dictionary generator
#The generation is based on pattern, the first and the last 2 characters of a string. Example:XXHackXX

#Importing modules & packages
import itertools
import os

#Print the line
print ("Dictionary Generator")
print ("This will generate a dictionary with 2 characters of prefix and suffix of the given word:-")

#Get user input
name = input("Enter a word : ")

#Using itertools
res = itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)

#Getting user input for the file name
myfile = open(input("Give a name to the output file with .txt: "),'w')

#Creating the dictonary with possible combinations
for i in res: 
    str = (''.join(i)+ name +''.join(i)+ '\n')
    myfile.write(str[2:-3] + '\n')

#Closing the file after writing to given file name
myfile.close()

#Print the line
print("The dictionary is generated")