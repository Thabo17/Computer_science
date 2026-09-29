tax = input('Enter cost price:')
tax = float(tax)
if tax>10000:
    total1 = tax * 0.15
    print('Your road tax is',total1)
if tax>5000 and tax<=10000:
    total2 = tax * 0.10
    print('Your road tax is',total2)
if tax<=5000:
    total3 = tax * 0.05
    print('Your road tax is',total3)