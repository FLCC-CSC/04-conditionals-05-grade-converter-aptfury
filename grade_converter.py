# FILE NAME - grade_converter.py

# NAME: Blake Lemarr
# DATE: 03/02/2026
# BRIEF DESCRIPTION: Program that automatically converts grade entered to their letter equivalent. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")

grade: int = int(input("Enter a numerical grade (1-100): "))

if grade > 100:
   print("A+")
elif grade >= 90:
   print("A")
elif grade >= 80:
   print("B")
elif grade >= 70:
   print("C")
elif grade >= 65:
   print("D")
else:
   print("F")

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Definitely to double check the way they organize their conditionals, as well as
the way that they check the values. For me personally, I prefer using the method I
displayed above to help simplify it.

'''
