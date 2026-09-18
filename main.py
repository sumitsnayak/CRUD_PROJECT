from pathlib import Path


print("Current folder:", Path.cwd())

import os


def createfile():
    
    try:       
        name=input("Please tell your file name:-")
        path = Path(name)
        if not path.exists():
                 with open(path,"w") as fs:
                    data=input("What you want to write:-")
                    fs.write(data)
                    print("flie created successfully")
        else:
                    print("Error File name already exists")

    except Exception as err:
     print(f"An error occured as{err}")


def readfile():
    try: 
            name=input("please tell your file name:-")
            path=Path(name)
            if path.exists():
                with open(path,"r") as fs:
                 content=fs.read()
                 print(f"Your content is:-\n{content}")
    except Exception as err:
             print(f"Error occured as {err}")



def updatefile():
    try:
        name=input("please tell your file name:-")
        path=Path(name)
        if path.exists():
            print("Operations")
            print("1. Renaming the file")
            print("2. Appending the file")
            print("3. Overwriting the file")

            numb=int(input("Enter Your Option Number:-"))
            if numb==1:
                newname=input("Tell your new file name:-")
                newpath=Path(newname)
                if not newpath.exists():
                    path.rename(newpath)
                    print("Renamed Successfully")
                else: 
                    print("New file name already exists")

            elif numb==2:
                with open(path,'a') as fs:
                 data=input("What do you want to append:-")
                fs.write("\n"+data)
                print("Sucessfully Appended")

            elif numb==3:
                with open(path,'w') as fs:
                 data=input("What do you want to Overwrite:-")
                fs.write("\n"+data)
                print("Sucessfully Added")
    except Exception as err:
        print(f"An error occured as{err}")
                
                
        
def deletefile():
 try:
            name=input("Enter file name:-")
            path=Path(name)
            if path.exists():
                path.unlink()
                print("File deleted succesfully")
            else:
                print("No such file exists")
 except Exception as err:
      print(f"An error occured as{err}")
     
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

a=int(input("\nTell your response:-"))



if a==1:
    createfile()
if a==2:
    readfile()
if a==3:
    updatefile()
if a==4:
    deletefile()