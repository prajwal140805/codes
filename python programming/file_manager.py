#run this code only to create the files
import os
a=20
b=31
c=10
d=31

for i in range(a,b):
    os.path.join('python programming', f'test{i}.cpp')
    with open( os.path.join('python programming', f'test{i}.cpp'), 'w') as file:
        file.write( "")   
#this is to delete the files created above
# for i in range(c,d):
#     os.remove (f'c++programming/test{i}.cpp') 

# with open ('python programming/test3.py', 'r') as f:
#     f.seek(0)
#     print(f.read( ))
    
    