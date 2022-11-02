#------------------------------------------
# Libraries and Modules Summative
# Nov. 1st, 2022
# Cole Patton
#------------------------------------------

# A simple calculator for adding, subtraction, multiplying, dividing, and powering

#----------------Modules Imported Here----------------
from arithmetic import primary # This is for addition and subtraction
from arithmetic import secondary # This is module for multiplying and dividing, Both come from library arithmetic
from exponentiation import exponent # This is module for calculating numbers to exponents. From the library exponentiation
from options import systems # This module is for viewing what this calculator can do from a list, from the library options


#----------Pre-Made Modules----------
import time


#------------------------------------------------------------------------------------
#-----------------Function Is Defined Here------------------

# Creates a list inside of this function that can be returned with the two numbers it gets
# Then it takes this list of the two numbers and does math with them, since they will always be in the same spot
# It may be possible to use a for loop with the list to add/multiply/divide/subtract as many numbers as you want
# But I am not sure, and not sure how I could really do it.
# I thought this was pretty good encapsulation though! :)

def find_nums(operation, that, word): #This function finds the numbers the user wants to use
    go = True
    while go == True:
        num1 = input("What number should we start with as a base?")
        if num1.isdigit():
            go = False
        
        else:
            print("That's not a number")
            time.sleep(0.5)
    go = True
    while go == True:
        num2 = input(f"What number do you want to {operation} {that} {word}")
        if num2.isdigit():
            go = False
            
        else:
            print("That's not a number")
            time.sleep(0.5)
        
    numbers = [num1, num2]
    return numbers
#-------------------------------------------------------------    

#----------------------Main Code----------------------------
    
systems.view() #Here I am calling the function that displays a list of all of the calculators options

time.sleep(3)

print('')

go = True
while go == True:
    choose = input("""What would you like to do?
1- Add
2- Subtract
3- Multiply
4- Divide
5- Exponents
6- Quit
""")
    
    # For the addition option
    if choose == '1':
        added = find_nums('add', 'that', 'with')
        total_addition = primary.add(int(added[0]), int(added[1]))
        print(f"That total sum is: {total_addition}!")
        time.sleep(2)
    
    #For the subtracting option
    elif choose == '2':
        subtracted = find_nums('subtract', 'from', 'that')
        total_subtraction = primary.subtract(int(subtracted[0]), int(subtracted[1]))
        print(f"That total sum is: {total_subtraction}!")
        time.sleep(2)
    
    #For the Multiplying option
    elif choose == '3':
        multiplied = find_nums('multiply', 'that', 'with')
        total_multiplied = secondary.multiply(int(multiplied[0]), int(multiplied[1]))
        print(f"That total sum is: {total_multiplied}!")
        time.sleep(2)
    
    #For the dividing option
    elif choose == '4':
        divided = find_nums('divide', 'into', 'that')
        total_divided = secondary.divide(int(divided[0]), int(divided[1]))
        print(f"That total sum is: {total_divided}!")
        time.sleep(2)
    
    # For the power/exponent option
    elif choose == '5':
        exponented = find_nums('power', 'that', 'to')
        total_exponented = exponent.power(int(exponented[0]), int(exponented[1]))
        print(f"That total sum is: {total_exponented}!")
        time.sleep(2)
    
    # Quitting out
    elif choose == '6':
        go = False
        print("Bye!")

    #And finally for user error!
    else:
        print("Try again! I don't know what that is.")
        time.sleep(0.5)