chillOS is an linux inspired text-based operating ststem built in python.
We challenged ourselves not to use 'import os' in this project.

Commands:
    FILES:
        file_create(name)
            def file_create:
            name=input(“File Name: “).lower()
            files.append[name]
            print(“File created”)
        file_rename(previousname, newname)
        sudo_file_delete(name, password)
            Sudo first asks for a pre-entered password to execute the action.
        file_edit(name, edits)
            a=input(“Name of file: “).lower()
        file_read(name)
        sudo_privatefile_create(name, password)
        sudo_privatefile_rename(previousname, newname, password)
        sudo_privatefile_delete(name, password)
        sudo_privatefile_edit(name, edits, password)
        sudo_privatefile_read(name, password)
        sudo_wipe(password)
            Deletes all files and data
        dir
            Shows directory of all filenames
        Stor
            Shows amount of storage left (x/5 normal files & y/2 private files)
					
	MISC:
        list_commands
            Lists commands from eligible_commands_list and summarizes what they do.
        datetime
            Returns the date and time
        sudo_newpswrd(oldpassword, newpassword)
        sudo_renameuser(newname, password)
        info
            Shows credits and OS info
        sudo ! !
            Runs the previous command
            Can be done by storing each command in a variable when executed and then writing over it each time. Then, call that command when this is command is executed.
        Sudo * *
        Prints last command but does not run it *helpful if you made a long file edit and mistyped password.

	FUNCTIONAL/calculator: 
        add(x, y)
        sub(x, y)
        mult(x, y)
        div(x, y)
        sqrt(num)
        exp(x, power) 
        mod(x, y)
        Base64(input)


IO:
	Greeting message: 
		Hello, USER, the time is {time} on {date}. \n\n Use ‘list_commands’ for the command list! 
pswrd = input(“Please create a password before continuing: ”)
	
	After each edit/command: input(“C:\chillOS\user@github.codespaces\shell: ”)
