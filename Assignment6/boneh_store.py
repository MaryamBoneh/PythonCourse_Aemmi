import colorama
from colorama import Fore

# ------------------init--------------------

colorama.init()
print('Loading...')
# ___ opening the databes file ___
try:
    f = open('Assignment6/products.csv')
except Exception as e:
    print("error: ", e)
    exit()
    
big_text = f.read()
parts = big_text.split('\n')
products = []
cart = []
i = 0

# ___ filling the product list in dictionary format ___
while i < len(parts):
    info = parts[i].split(',')
    if info[4] != '1':
        products.append({'ID': info[0], 'NAME': info[1], 'PRICE': info[2], 'COUNT': info[3], 'DELETED': info[4]})
    i += 1
print(Fore.LIGHTCYAN_EX + 'data loaded! \nwelcome dear user!')

# -----------------process-------------------


def addNewProduct():
    print(Fore.LIGHTWHITE_EX +
          '___ adding a product ___ \n***please enter the product details***')
    name = input('NAME: ')
    for i in range(len(products)):
        if name == products[i]['NAME']:
            print('this product exists in the store')
            break
    else:
        price = input('PRICE: ')
        count = input('COUNT: ')
        pid = str(int(products[len(products)-1]['ID']) + 1)
        # ___ update products list ___
        products.append({'ID': pid, 'NAME': name, 'PRICE': price, 'COUNT': count, 'DELETED': '0'})

        print(Fore.GREEN + 'Done!')
    menu()


def search():
    user_input = input('enter ID or NAME of product: ')
    for product in products:
        if product['ID'] == user_input or product['NAME'] == user_input:
            print(Fore.WHITE + str(product))
            break
    else:
        print(Fore.RED + 'not found')
    menu()


def edit():
    print(Fore.LIGHTWHITE_EX + '___ editing a product ___')
    name = input('enter name of product that you want to edit: ')
    for i in range(len(products)):
        if name == products[i]['NAME']:
            products[i]['NAME'] = input('new name: ')
            products[i]['PRICE'] = input('new price: ')
            products[i]['COUNT'] = input('new count: ')
            break
    else:
        print(Fore.LIGHTCYAN_EX + 'this product is not exists in the store')

    menu()


def remove():
    print(Fore.LIGHTWHITE_EX + '___ deleting a product ___')
    name = input('please enter the product name: ')
    
    for product in products:
        if name == product['NAME']:
            print(Fore.LIGHTRED_EX + 'are you sure you want delete this product? \n  y?  n? ')
            yORn = input()
            if yORn == 'y':
                product['DELETED'] = '1'
                break
    else:
        print(Fore.LIGHTCYAN_EX + 'this product is not exists in the store')

    menu()


def buy():
    print(Fore.LIGHTWHITE_EX + '___  BUY  ___')

    while True:
        code = input('please enter the product code: ')
        for product in products:
            if code == product['ID']:
                count = int(input('how many? '))
                if count <= int(product['COUNT']):
                    cart.append(str(count) + '\t' + product['NAME'])
                    product['COUNT'] = str(int(product['COUNT']) - count)
                else:
                    print(Fore.LIGHTCYAN_EX + f"only {product['COUNT']} of this product are available")
                break
        else:
            print(Fore.LIGHTCYAN_EX + 'this product is not exist in store')
                
        print(Fore.LIGHTWHITE_EX + 'do you want another product?\n y? n? ')
        yORn = input()
        if yORn != 'y':
            showCart()
            break

def showAll():
    for i in range(len(products)):
        if products[i]['DELETED'] == '0':
            print(Fore.LIGHTMAGENTA_EX + f"ID: {products[i]['ID']},  NAME: {products[i]['NAME']},  PRICE: {products[i]['PRICE']},  COUUNT: {products[i]['COUNT']}")
    menu()


def showCart():
    if cart == []:
        print(Fore.LIGHTCYAN_EX + 'your cart is empty')
    else:
        print(Fore.LIGHTGREEN_EX + 'count | name \n--------------------------')
        for i in cart:
            print(i)
    menu()
    

def saveAndExit():
    # ___ update csv file ___
    out = open('Assignment6/products.csv', 'w')
    for product in products:
        out.write(product['ID'] + ',' + product['NAME'] + ',' + product['PRICE'] + ',' + product['COUNT'] + ',' + product['DELETED'])
        if product != products[-1]:
            out.write('\n')
    out.close()
    print(Fore.LIGHTGREEN_EX + 'Thanx! Goodbye')
    exit()

def menu():
    print(Fore.LIGHTYELLOW_EX +
          '\n 1- add new product \n 2- search \n 3- edit \n 4- remove \n 5- buy \n 6- show all \n 7- show cart \n 8- save changes and exit')
    user_select = input('please enter the option you want: ')

    if user_select == '1':
        addNewProduct()
    elif user_select == '2':
        search()
    elif user_select == '3':
        edit()
    elif user_select == '4':
        remove()
    elif user_select == '5':
        buy()
    elif user_select == '6':
        showAll()
    elif user_select == '7':
        showCart()
    else:
        saveAndExit()


menu()
