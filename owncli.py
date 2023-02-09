import os
import sys
from pathlib import Path
import subprocess
    
def writing_in_file(command, fp):
    if(command_array[0] == 'cd'):
        if os.path.isdir(command_array[1]):
            os.chdir(command_array[1])
            fp.write("Current working Directory after changing:")
            fp.write(os.getcwd())
            fp.write("\n")
        else:
            fp.write("The system cannot find the path specified.")
            fp.write("\n")
            
    elif(command[0:4] == 'help'):
        help =("cd <directory> - change the current default directory to <directory>. If the <directory> argument is not present, report the current directory. If the directory does not exist an appropriate error should be reported. This command should also change the PWD environment variable."
        '''
clr - clear the screen.
dir <directory> - list the contents of directory <directory>
environ - list all the environment strings
echo <comment> - display <comment> on the display followed by a new line (multiple spaces/tabs may be reduced to a single space)
help - display a list of all commands and their inputs/behaviors.
pause - pause operation of the shell until 'Enter' is pressed
quit - quit the shell
        ''')
        fp.write(help)
        fp.write("\n")
        
    elif(command[0:7] == 'environ'):
        for a, b in os.environ.items():
             fp.write(f'{a}:{b}')
        fp.write("\n")

    elif(command[0:3] == 'clr'):
        fp.write(str(os.system('cls||clear')))

    elif(command_array[0] == 'echo'):
        a = command_array[1:-1]
        b =  " ".join(a)+ "\n"
        fp.write(b)
            
    elif(command[0:5] == "pause"):
        b = input("press enter to continue.....")
        fp.write(b)

    elif(command_array[0] == 'dir'):
        directories = os.listdir(command_array[1])
        for b in directories:
            fp.write(str(b))
            fp.write("\n")

    elif(command[0:4] == 'quit'):
        fp.write(exit())
    fp.close()

    
while True:
    command = input(os.getcwd() + ">")
    command_array = command.split()
    if '>' in command:
         if '>>' in command:
            x = command.index('>>') + 2
            fp = open (command[x:],'a')
            writing_in_file(command,fp)
         elif '>' in command:
            x = command.index('>') + 1
            fp = open (command[x:],'w')
            writing_in_file(command,fp)
            
    elif command_array[0] == "cd":
        if os.path.isdir(command_array[1]):
            os.chdir(command_array[1])
            print("Current working Directory after changing:")
            print(os.getcwd())
            print("\n")
        else:
            print("The system cannot find the path specified.")
        
    elif command == "help":
        help =("cd <directory> - change the current default directory to <directory>. If the <directory> argument is not present, report the current directory. If the directory does not exist an appropriate error should be reported. This command should also change the PWD environment variable."
        '''
clr - clear the screen.
dir <directory> - list the contents of directory <directory>
environ - list all the environment strings
echo <comment> - display <comment> on the display followed by a new line (multiple spaces/tabs may be reduced to a single space)
help - display a list of all commands and their inputs/behaviors.
pause - pause operation of the shell until 'Enter' is pressed
quit - quit the shell
        ''')
        print(help)
        
    elif command == "environ":
        for a, b in os.environ.items():
             print(f'{a}:{b}')
        print("\n")
            
    elif command == "clr":
        os.system("cls||clear")
        
    elif command_array[0] == "echo":
        a = command_array[1:]
        b =  " ".join(a)+ "\n"
        print(b)
        
    elif command == "pause":
        input("Press enter to continue.....")
        
    elif command_array[0] == "dir":
        directories = os.listdir(command_array[1])
        for b in directories:
            print(b)
        print()
        
    elif command == "quit":
        break
    else:
        print("'" + command + "'"+" is not recognized as an internal or external command, operable program or batch file.\n")

