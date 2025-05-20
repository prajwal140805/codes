#run this code only to create the files
import os
a=29
b=51
c=10
d=31

for i in range(a,b):
    os.path.join('c++programming', f'test{i}.cpp')
    with open( os.path.join('c++programming', f'test{i}.cpp'), 'w') as file:
        file.write( "")   
#this is to delete the files created above
# for i in range(c,d):
#     os.remove (f'c++programming/test{i}.cpp') 
 
 