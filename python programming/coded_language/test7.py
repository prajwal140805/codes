
import os
print("_______________________________________________________________________________________________ ")
print("*********************************WELCOME TO CODED LANGUAGE*************************************!")
while (True):
    print("Choose an option:", end="")
    print("Choose an option:")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    print("_______________________________________________________________________________________________ ")

    choice =  (input())
    os.system('cls')

    if choice =='1':
        import subprocess
        subprocess.run(
            ["python", "python programming/coded_language/test7_encode.py"])
    elif choice =='2':
        from test7_decode import Decode
        Decode()

    elif choice =='3':
        print("Exitting the program.....")
         

        break
    else:
        print("Invalid choice! Please try again.....")
        print("_______________________________________________________________________________________________ ")
