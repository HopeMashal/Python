""" In this app, I used if/elif/else statement """
""" Ask the user to enter the numbers and the operation """

Number_1 = input("Enter the first number: ")
Number_2 = input("Enter the second number: ")
operator = input("Enter the operator: ")

""" if/elif/else statement """
""" Print the equation and the result """ 

if operator == "+":
    print("The equation is:",Number_1,operator,Number_2)
    print("The result is:",float(Number_1)+float(Number_2))
elif operator == "-":
    print("The equation is:",Number_1,operator,Number_2)
    print("The result is:",float(Number_1)-float(Number_2))
elif operator == "/":
    print("The equation is:",Number_1,operator,Number_2)
    print("The result is:",float(Number_1)/float(Number_2))
elif operator == "*":
    print("The equation is:",Number_1,operator,Number_2)
    print("The result is:",float(Number_1)*float(Number_2))
elif operator == "%":
    print("The equation is:",Number_1,operator,Number_2)
    print("The result is:",float(Number_1)%float(Number_2))
else:
    print("PLEASE ENTER (+,-,*,/,%) !!!")

