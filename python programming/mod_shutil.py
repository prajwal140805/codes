import shutil
import os 
for i in range(1 ):
   shutil.copy("python programming/sample.txt ", f"python programming/sample({i}).txt") 
os.remove("python programming/sample.txt")   