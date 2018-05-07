import faker as c
from random import *
import random_string as r
import random
import string
import sys
fake = c.Factory.create()
#avail=['yes','no']
print '\n\n##############->CAR_RENTAL v1.0<-##################\n'
print "Enter the Number of tuples you want to generate: "
setamount=int(raw_input())
print"Got it Thanks!!!"

t="hi"
i=0
text_file = open("Output.txt", "w")
text_file.write("VALUES")
while i < int(setamount):


    t='('+'\''+str(r.generate_word(random.randint(4,10)))+'\','+str(randint(50,500))+','+str(randint(50,300))+',\''+str(fake.random_digit())+' ' +str(fake.street_name())+'\','+str(randint(0,1000))+')'
    #print t
    text_file.write( t )
    i+=1
    if i != setamount:
        text_file.write(',\n')

    if i==setamount:
        text_file.write(';')
        break



print("CHECK Output.txt :)")

