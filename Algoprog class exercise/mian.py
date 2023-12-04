def Dry_Cured():
    amount = (input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 177.80
    print(total)

def Wagyu_Steaks():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 450.00
    print(total)

def Matsuke():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 272.00
    print(total)

def Kopi():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 306.50
    print(total)

def Moose():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 487.20
    print(total)

def White_Truffles():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 3600.00
    print(total)

def Blue_Fin():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 3603.00
    print(total)

def Bonnotte():
    amount = int(input('enter the pound of food : '))
    if (amount < 0):
        return
    total = amount * 270.81
    print(total)

    
print('Food List')
print('='*10)
print('Dry Cured Iberian Ham')
print('Wagyu Steaks')
print('Matsutake Mushrooms')
print('Kopi Luwak Coffe')
print('Moose Cheese')
print('White Truffles')
print('Blue Fin Tuna')
print('Le Bonnote Potatoes')

items = int(input('How many items will you order today? '))

if items <= 8:
    type_food = str(input('enter the items name : '))

    if (type_food == 'Dry Cured Iberian Ham'):
        Dry_Cured()

    elif (type_food == 'Wagyu Steaks'):
        Wagyu_Steaks()

    elif (type_food == 'Matsutake Mushrooms'):
        Matsuke()

    elif (type_food == 'Kopi Luwak Coffe'):
        Kopi()

    elif (type_food == 'Moose Cheese'):
        Moose()

    elif (type_food == 'White Truffles'):
        White_Truffles()

    elif (type_food == 'Blue Fin Tuna'):
        Blue_Fin()

    elif (type_food == 'Le Bonnote Potatoes'):
        Bonnotte()

else:
    print('Number of Items must be at least 1 and not over 8')
# def dry(Dry_Cured_Iberian_Ham):
#     amount = input('enter the amount of food: ')
#     total = amount * 177.80
# def wagyu(Wagyu_Steaks):
#     amount = input('enter the amount of food: ')
#     total = amount * 450.00

# def matsutake(Matsutake_Mushrooms):
#     amount = input('enter the amount of food: ')
#     total = amount * 272.00

# def kopi(Kopi_Luwak_Coffe):
#     amount = input('enter the amount of food: ')
#     total = amount * 306.50

# def moose(Moose_Cheese):
#     amount = input('enter the amount of food: ')
#     total = amount * 487.20

# def truffles(White_Truffles):
#     amount = input('enter the amount of food: ')
#     total = amount * 3600.00

# def blue(Blue_Fin_Tuna):
#     amount = input('enter the amount of food: ')
#     total = amount * 3603.00

# def bonnotte(Le_Bonnotte_Potatoes):
#     amount = input('enter the amount of food: ')
#     total = amount * 270.81   