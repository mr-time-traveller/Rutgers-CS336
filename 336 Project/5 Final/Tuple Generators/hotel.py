import faker as c
from random import *
import random_string as r
import random
import string
import sys
fake = c.Factory.create()
#avail=['yes','no']
print '##############->HOTEL v1.1<-##################\n\n\n'
print "Enter the Number of tuples you want to generate: "
setamount=int(raw_input())
print"Got it Thanks!!!"

t="hi"
i=0
text_file = open("Output.txt", "w")
text_file.write("VALUES")
while i < int(setamount):


    t='('+str(randint(50,500))+',\''+str(r.generate_word(random.randint(4,10)))+'\',\''+str(choice(['yes', 'no'])) +'\',\''+ str(fake.random_digit_or_empty())+' ' +str(fake.street_name())+'\','+str(randint(0,1000))+')'
    text_file.write( t )
    i+=1
    if i != setamount:
        text_file.write(',\n')

    if i==setamount:
        text_file.write(';')
        break



print("CHECK Output.txt :)")

