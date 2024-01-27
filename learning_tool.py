'''
A LEARNING TOOL: The Functions of the Organs in the Human Body!

'''

# Name of learning tool
print("FUNCTIONS OF VITAL BODY ORGANS \n")

# Names of the organs available in the learning tool
print("Names of the Organs - Heart, Brain, Lungs, Kidneys \n ")

# Functions of the organs available in the learning tool
print("""Organ Functions:
1 - Pumps and helps circulate blood throughout the body.
2 - Acts as the control center of the body.
3 - Regulate excretion of water and other substances from the body.
4 - Responsible for gas exchange. \n""")

# Creating a list of the functions to enable easy indexing
org_func = [
"pumps and helps circulate blood throughout the body.",
"acts as the control center of the body.",
"regulate excretion of water and other substances from the body.",
"responsible for gas exchange."
]

# User is requested to choose the correct number from list 
# corresponding to the correct function for each question asked
while True:
    num1 = int(input("What is the function of the heart? \
    (Choose the correct number between 1-4 from list above) : "))

# Error message appears when the wrong answer is entered and the question repeats
    if num1 != 1:
        print("Wrong answer. Try again \n")
        continue

# When the correct answer is chosen, the loop breaks and the next question is triggered
    else:
        print("Correct! The heart", org_func[0])
        break
    
# the process continues as stated above for the rest of the questions until all questions 
# are answered correctly and the loop breaks

while True:
    num2 = int(input("\nWhat is the function of the kidneys? \
        (Choose the correct number between 1-4 from list above) : "))

    if num2 != 3:
        print("Wrong answer. Try again")
        continue

    else:
        print("Correct! The kidneys", org_func[2])
        break

while True:
    num3 = int(input("\nWhat is the function of the lungs? \
    (Choose the correct number between 1-4 from list above) : "))

    if num3 != 4:
        print("Wrong answer. Try again")
        continue

    else:
        print("Correct! The lungs are", org_func[3])
        break

while True:
    num4 = int(input("\nWhat is the function of the brain? \
    (Choose the correct number between 1-4 from list above) : "))

    if num4 != 2:
        print("Wrong answer. Try again")
        continue
    
    else:
        print("Correct! The brain", org_func[1])  
        break