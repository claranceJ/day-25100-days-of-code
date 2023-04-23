def priceBook(number,amount):
  total=12.42*number
  difference=total-amount
  if amount < total:
    print(f"the total is {total} ksh, sorry that won't be enough, you need {difference} ksh more.")
  else:
    print(f"The total amount is {total} ksh, You have enough money, your balance is {difference} ksh")

numberBooks=int(input("How many books do you want to buy?: "))
amountAvailable=int(input("How much money do you have?: "))

priceBook(numberBooks,amountAvailable)
