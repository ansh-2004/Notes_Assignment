# File Handling 
# Dealing with text files 

# Dealing with text files is known as File Handling or even called as File I/O functions. 
# There are different functions involved, which helps to read, write , append , alter and perform many other functions. 

# ---

# Open ,read and write modes 

# Open mode 
# This mode is used whenever you want to open your text file for reading , writing or doing some other stuffs. 

# Read mode 
# This mode is used whenever you want to read the text which is already stored in your text file 

# Write mode 
# This mode is used whenever you want to write the text in your .txt file 


# open mode 

# f = open("C:/Users/ansh.gupta/Documents/Work/Notes_Assignment/16_text.txt")    # f is file pointer and open() is our file handling function in which we pass the name of our file 

# print(f) # output: <_io.TextIOWrapper name='C:/Users/ansh.gupta/Documents/Work/Notes_Assignment/16_text.txt' mode='r' encoding='cp1252'>

# read mode - "r"
# write mode - "w"

# opening file in read mode

# f = open("16_text.txt","r") # means open file in read mode          # if file is in same folder then just give name of file and if in other location then give full path as we done before

# content = f.read()  # file is being read and stored in content variable

# print(content) # output: This is the topic of file handling in python


# opening file in write mode 

# f = open("16_text.txt","w") # means open file in write mode

# print("f after opening",f) # output: f after opening <_io.TextIOWrapper name='16_text.txt' mode='w' encoding='cp1252'>

# f.write("I am learning file handling in python") # text we want to write in our file 

# f.close() # Now it is best practice to always close the file after opening it

# we don't get any output on console because we have written the text in our file
# If any previous text is there in our file then it will be deleted and this new text will be written

# -----------------

# Adding text , counting characters 

# Append function

# - Append function helps us to add the text in your .txt file.
# - The mode used is 'a' for appending means adding or writing some text to the file 
# - For adding text to the file in a new line use \n before writing the sentence to be added. 


# f = open("16_text.txt","a") # opening file in append mode
# add_text = f.write("\n This is append mode ")
# print(add_text) # output: 22 (it shows the number of characters added in the file)

# f.close()


# ----
# Len function 

# To count the characters in a text file len() is the function used.
# Firstly we open the file and read that using the functions. 
# And after the reading of the text len function is assigned with the variable to find the count of characters 

# f = open("16_text.txt","r") # opening file in read mode
# data = f.read() # reading the file and storing it in data variable
# total_count = len(data) # using len function to count the characters in the file
# print(total_count) # output: 59

# f.close()

# ---------------------------------------

# Readline functions 

# This readline function helps us to read the text line by line. 
# For using this function, firstly open file is needed and in read mode  . 
# Then accordingly use the readline function to read the lines accordingly in the form of line by line. 

# - currently this is written in my 16_text.txt file 

# ```
# I am learning file handling in python
# This is append mode 
# Topics are open , read and write mode 
# append function
# ``

# f = open("16_text.txt","r") 

# print(f.readline()) #output:- I am learning file handling in python
# print(f.readline()) #output:- This is append mode
# print(f.readline()) #output:- Topics are open , read and write mode



# if we use readlines() function then we get list of strings 
# print(f.readlines())  
# output :- ['I am learning file handling in python\n', 'This is append mode \n', 'Topics are open , read and write mode \n', 'append function']

# f.close() 


#---

# # WITH 
# The WITH statement in Python is a powerful and elegant way to manage resources like files , network connections , or locks. 

# The WITH statement is used to wrap the execution of a block of code with the methods defined by a context manager. It ensures that setup and cleanup actions are handled automatically. 
# For file handling , it means :
# - The file is opened. 
# - You do your opearations(read/write)
# - The file is automatically closed even if an error occurs 

# syntax :-
# with open("filename.txt","mode") as f:
#     # Do something with f 

# This is equivalent to :

# f = open("filename.txt","mode")
# try:
#     #Do something with f
# finally:
#     f.close()


# Multiple Contexts
# You can use multiple context managers in one line:

# python
# with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
#     for line in infile:
#         outfile.write(line.upper())


