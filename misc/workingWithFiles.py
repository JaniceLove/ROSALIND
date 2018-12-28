

 #stack Overflow (https://stackoverflow.com/questions/30551945/
 #how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po)       
with open('lesson5.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0: #this is the remainder operator
            print(line)
