import faker as c
from random import *
import random_string as r
import random
import string
import sys
fake = c.Factory.create()
avail=['\'ITALIAN\'','\'CHINESE\'','\'INDIAN\'','\'MEXICAN\'','\'AMERICAN\'','\'INDIAN\'','\'THAI\'']
avg=[0,5,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
prange=['\'1-10\'','\'1-50\'','\'5-240\'','\'5-50\'','\'1-100\'','\'3-70\'','\'10-80\'','\'10-1000\'','\'3-10\'','\'100-20000\'','\'15-75\'']
print '\n\n##############->RESTAURANT v1.0<-##################\n'
print "Enter the Number of tuples you want to generate: "
setamount=int(raw_input())
print"Got it Thanks!!!"

t="hi"
i=0
text_file = open("Output.txt", "w")
text_file.write("VALUES")
while i < int(setamount):


    t='(\''+str(r.generate_word(random.randint(4,10)))+'\','+random.choice(avail)+','+random.choice(prange)+','+str(random.choice(avg))+',\''+str(fake.random_digit())+' ' +str(fake.street_name())+'\','+str(randint(0,1000))+')'
    text_file.write( t )
    i+=1
    if i != setamount:
        text_file.write(',\n')

    if i==setamount:
        text_file.write(';')
        break



print("CHECK Output.txt :)")

