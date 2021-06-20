#Program: file_create
#Author: Brent Lang
#Date: 10/31/20
#Purpose: Program will take file name and it's contents from the user.
#         Save all the input from the user to the file that was created. 
#         Once user is done with providing the content, display the file content on the monitor.   

# Function writes the file using the name user specifies.
def write_user_file(user_file):
    file_handle = open(user_file, 'w')
    repeat_lines = 'y'
    
    while repeat_lines.lower() == 'y':
        user_input = input('Please enter a sentence: ')
        repeat_lines = input('Do you want to add more lines? (Y/N) ')
        if repeat_lines.lower() == 'y':
            file_handle.write(user_input)
            file_handle.write('\n')
        else:
            repeat_lines = 'n'
            break 

    file_handle.write(user_input)
    file_handle.write('\n')
    file_handle.close()

# Function prints the content user inputs into the file created.
def print_lines(user_file):
    file_handle = open(user_file)
    print(f"\nThis is what's entered into file {user_file}")
    print('=============================')
    
    for line in file_handle:
        print(line.rstrip())
    
    print('=============================')
    file_handle.close()

import re
# Main program tests filename for validity and calls write_user_file and print_lines functions.
# User is asked to repeat and program executes as instructed.
file_name = input('Please enter a filename: ')
repeat_program = 'y'

while repeat_program.lower() == 'y':
    file_extension = file_name.find('.')
    # Filename is checked for an extension.
    if file_extension == -1:
        print('File name needs to have an extension')
        file_name = input('Plese enter a proper filename: ')
        continue
    # Filename is checked to ensure it contains valid characters(Alphanumeric and underscore).
    if re.search(r'[\W]+', file_name[:file_extension]):
        print('Filename may only contain Alphabets, digits and "_"')
        file_name = input('Plese enter a proper filename: ')
        continue
    # Filename is checked to ensure it starts with a letter or underscore.
    if re.search(r'^\d', file_name[:file_extension]):
        print('Filename only can start with Alphabets or "_"')
        file_name = input('Plese enter a proper filename: ')
        continue
    # File extension is checked to ensure it contains valid characters(Alphanumeric and underscore).
    if re.search(r'[\W]', file_name[file_extension + 1:]):
        print('Filename may only contain Alphabets, digits and "_"')
        file_name = input('Plese enter a proper filename: ')
        continue
    
    write_user_file(file_name)
    print_lines(file_name)

    repeat_program = input('Do you want to create another file? (Y/N) ')

    if repeat_program.lower() == 'n':
        print('Thanks for playing!')
    else:
        print("Let's create another file.")
        file_name = input('Please enter a filename: ')
        continue
        
    


    
