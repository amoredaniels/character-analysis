#Amore' Daniels

#open the file
englishProse = open('text.txt')
#read the file contents using .realines()
#store file contents into a variable
content = englishProse.readlines()
#make list for stripped strings
newContent = []
#strip each sentence in the list
for sentence in content:
    sentence = sentence.strip()
    #add to list
    newContent.append(sentence)

#create and initialize counter variables to 0
#uppercase letters
uppercase = 0
#lowercase letters
lowercase = 0
#numbers
number = 0
#whitespace
whitespace = 0

#iterate through the variable assigned the contents of the file
for sentence in newContent:
    #iterate through each character in each sentence
    for ch in sentence:
        #identify if it is:
        #an uppercase letter
        if ch.isupper():
            #if it is increment counter by 1
            uppercase += 1
        #lowercase letters
        if ch.islower():
            #if it is increment counter by 1
            lowercase += 1
        #digits
        if ch.isdigit():
            #if it is increment counter by 1
            number += 1
        #whitespace
        if ch.isspace():
            #if it is increment counter by 1
            whitespace += 1

#print counters
print('There are',uppercase,'uppercase letters.')
print('There are',lowercase,'lowercase letters.')
print('There are',number,'numbers.')
print('There are',whitespace,'whitespaces.')