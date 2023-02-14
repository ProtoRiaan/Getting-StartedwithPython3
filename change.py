changeAmt = int(input("How much change do you need?"))

numQt = changeAmt //25
changeAmt = changeAmt % 25

numDimes = changeAmt // 10
changeAmt = changeAmt % 10

numNick = changeAmt // 5
changeAmt = changeAmt % 5

numPennies = changeAmt // 1
changeAmt = changeAmt % 1

print ("Quarters : ", numQt)
print("Dimes: %s" % numDimes)
print(f"Nickles: {numNick}")
print(f"Pennies: {numPennies}")
print(f" Final change amount: {changeAmt}")