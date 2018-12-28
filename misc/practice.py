#sum of odd integers between 100-200
a = 4293
b = 8620 
subtract = b-a
print (subtract)
n = (b-a)+1
c = []
for i in range (n):
    if a %2 == 1:
        print ('a is'),a
        c.append(a)
        a = a+1        
    else:
        a = a+1
        print ('not an odd integer')
        
#print c
print ('the sum of odd integers is'),sum(c)
