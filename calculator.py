import re

print("Calculatron")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    # Pull global variables into function scope
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    # Provide a way to exit
    if equation == 'quit':
        print("\nQuitting...")
        run = False
    else:
        # use regex to protect against eval() injection
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print("You typed: ", previous)


while run:
    performMath()