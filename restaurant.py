input("Do You Want To Split The Restaurant Bill\nTap enter to continue\n")
Total = float(input("Total Amount of Bill?\n"))
Tip = float(input("Do you want to tip the waiter? Write down the amount you want to tip, If not then write 0.(Don't write the % sign or anything other than number!!)\n"))
People = int(input("In how many peoples you want to split the bill?\n"))
Final_amt = Total + Tip
Per_head = (Final_amt/People)
print(f"You have to pay {Per_head}")
