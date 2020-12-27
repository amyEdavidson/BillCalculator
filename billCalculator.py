#recieves subtotal from user
print("Enter the bill subtotal")
subtotal = input()
subtotal = int(subtotal)

print("Enter the desired tip percentage")
percentage = input()
percentage = float(percentage)/100

total = subtotal*percentage+subtotal

print("The total bill is", "${:.2f}".format(total))