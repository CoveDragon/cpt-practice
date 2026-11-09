from prompt_toolkit import prompt
files=[]
def file_create():
    nam=input("File Name: ").lower()
    files.append(nam)
    print("File created")
def file_edit(nam):
    a=prompt(default="")
    return a
file_create()
file_edit("lol")