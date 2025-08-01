first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number:" ))

operation = input("What operation? (+, -, *, /):")

if operation =="+":
    result = first_number + second_number

elif operation =="-":
     result = first_number - second_number

elif operation =="*":
     result = first_number * second_number

elif operation =="/":
     result = first_number / second_number

else:
     result = "That's not a valid operation" 
     
print("The answer is:" ,result)


