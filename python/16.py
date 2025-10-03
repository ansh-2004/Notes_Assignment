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

f = open("16_text.txt","r") # means open file in read mode          # if file is in same folder then just give name of file and if in other location then give full path as we done before

content = f.read()  # file is being read and stored in content variable 

print(content) # output: This is the topic of file handling in python 


