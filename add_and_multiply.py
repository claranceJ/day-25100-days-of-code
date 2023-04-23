# create a program to add and multiply two numbers
# create two functions add_numbers() multiply_numbers()
# compute the result and return them to the function call
# result printed outside the function

def add_number(num1,num2):
  addition=num1+num2
  return addition

def multiply_numbers(num1,num2):
  multiplication=num1*num2
  return multiplication

first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))

addition=add_number(first_number,second_number)
print(f"The sum of the two numbers is {addition}")

multiplication=multiply_numbers(first_number,second_number)
print(f"The total multiplication is {multiplication}")