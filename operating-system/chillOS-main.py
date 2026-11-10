# Define variables, lists, and import functions.

import math
import base64
from datetime import datetime, timedelta, timezone
from prompt_toolkit import prompt

files=[]
username = input("Enter a username: ")
pswrd = input("Enter a password: ")
utc_now = datetime.now(timezone.utc)
utc_time = utc_now.strftime("%Y-%m-%d %H:%M:%S")
foreverloop = True
lastcommand = "False"

#define all commands

#files here

def file_create():
    nam=input("File Name: ").lower()
    files.append(nam)
    print("File created")
def file_edit():
    titl=input("File name: ").lower()
    if titl in files:
        temp=chr((files.index(titl))+1)
        temp=prompt(default=temp)
    else:
        print("Not a valid file")

# misc here

def list_commands():
    return f"THERE ARE 28 TOTAL COMMANDS.\n\nTYPE: FILES\n\nfile_create(name)\tcreates a new file.\nfile_rename(previousname, newname)\trenames a file.\nsudo_file_delete(name, password)\tdeletes a file.\nfile_edit(name, edits)\tallows you to write to a file.\nfile_read(name)\tallows you to read a file's contents.\nsudo_privatefile_create(name, password)\tcreates a new private file, which requires a password to read and write to.\nsudo_privatefile_rename(previousname, newname, password)\trenames a private file.\nsudo_privatefile_delete(name, password)\tdeletes a private file.\nsudo_privatefile_edit(name, edits, password)\tallows you to write to a private file, but requires a password.\nsudo_privatefile_read(name, password)\tallows you to read a private file's contents, but requires a password to access.\nsudo_wipe(password)\tdeletes all files and data.\ndir\tshows directory with all filenames.\nstor\tShows amount of storage left (x/5 normal files & y/2 private files)\n\nTYPE: MISC\n\nlist_commands\tlists all available commands.\ndatetimef\treturns the date and time.\nsudo_newpswrd(oldpswrd, newpswrd)\tallows you to create a new password.\nsudo_renameuser(newname, password)\tallows the user to rename themselves.\nsudo ! !\truns the previous command.\nSudo * *\tPrints last command but does not run it *helpful if you made a long file edit and mistyped password.\n\nTYPE: FUNCTIONAL/CALCULATOR\n\nadd(x, y)\tadds 2 numbers\nsub(x, y)\tsubtracts one number from another\nmult(x, y)\tmultiplies 2 numbers.\ndiv(x, y)\tdivides one number by another.\nsqrt(num)\ttakes the square root of a number\nexp(x, power)\tmultiplies a number by itself a set amount of times.\nmod(x, y)\tfinds the remainder of a division equation.\nbase64(input)\tconverts an input to base64 binary.\n"

def datetimef():
    utc_now = datetime.now(timezone.utc)
    return utc_now.strftime("%Y-%m-%d %H:%M:%S")

def sudo_newpswrd(oldpswrd, newpswrd):
    global pswrd

    if oldpswrd == pswrd:
        pswrd = newpswrd
        print("password updated")
    else:
        print("password incorrect.")

def sudo_renameuser(pswrd, newuser):
    print("ok")

def info():
    return f"chiilOS copyright Zack & Jacob co 2026 Voorhees High School, Glen Gardener, NJ.\n\nJacob: File directories.\n\nZackary: system funtionality and misc commands."

#start OS

print(f"Hello, {username}, the time and date is {utc_time}.\n\nUse ‘list_commands’ for the command list!")

# command checker

while foreverloop ==  True:
    command = str(input(f"\nC:/chillOS/{username}@github.codespaces/shell: "))
    print(f"Your command: {command}\n")

    if command == "list_commands":
        print(list_commands())
    elif command == "datetimef":
        print(datetimef())
    elif "sudo_newpswrd" in command:
       parts = [part.strip() for part in command[14:].split(",")]
       sudo_newpswrd(parts[0], parts[1][:-1])
    elif "sudo_renameuser" in command:
        print("sudo_renameuser() command")
    elif command == "info":
        print(info())
    # elif command == "sudo ! !":
        
    elif command == "file_create":
        file_create()
        chr(len(files)+1) = ""
    elif command == "file_edit":
        file_edit()
        print(files)
    else:
        print("Error: command does not exist.")
