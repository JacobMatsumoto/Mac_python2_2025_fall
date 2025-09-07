"""
Make Names Meaningful:
Replace single-letter variables with meaningful names.
Rename the function to reflect its purpose.
Add Comments:
Explain the purpose of the function.
Describe the purpose of each major block of code.
Improve Spacing and Indentation:
Ensure consistent use of indentation (4 spaces per level).
Add blank lines to separate different parts of the code.
Simplify the Code:
Reduce nesting levels by refactoring the logic.
Simplify conditionals where possible.
Add Docstrings:
Add a docstring to the function to describe its behavior.
Handle Errors Gracefully:
Add error handling for unexpected inputs.
Hand in your updated code by uploading it to GitHub and submitting the link.
"""
"""This function checks to see if there are more ducks then geese or vice verse """


def which_has_more(ducks, geese): #ducks is a and geese is b "fx" got changed to which_has_more 
   
#   if ducks > 0 and geese > 0: removing this because it is repetitive and unneeded.
    try:

        if ducks == 0 or geese == 0: #checks to see if either contains a zero.
            return "Zero found"
        
        elif ducks > geese: #checks if ducks is greater than geese then prints the number of ducks and returns 
            for i in range(geese): #geese minus ducks
                print(ducks)

            return geese - ducks
            
        elif geese > ducks: #changed this from a blanket else to exactly what it is checking for
                            # it then does the opposite of if ducks are greater than geese. by printing geese and returning ducks minus geese
            for i in range(ducks): #changed j to i to keep it standard and consistent
                print(geese)

            return ducks - geese
        
        # if ducks == 0 or geese == 0: moving this to a spot that makes more sense
        #     return "Zero found"
        
    except Exception as e:  # catches the unknown errors
            print(f"An error has occured{e}")

#   else:
#       if a < b:
#           return a - b
#       else:
#           return b - a
#moved these to be under existing checks of greater than or less than