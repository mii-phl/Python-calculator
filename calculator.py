sk1=int(input('ievadi sk1'))
sk2=int(input('ievadi sk2'))
elements = input('ierakstii savu darbibu +, -, /, *')

if(elements == '+'):
    print(sk1 + sk2)
elif(elements =='-'):
    print(sk1 - sk2)
elif(elements == '/'):
    print(sk1 / sk2)
elif(elements =='*'):
    print(sk1 * sk2)
else:
    print("Nepareizi")