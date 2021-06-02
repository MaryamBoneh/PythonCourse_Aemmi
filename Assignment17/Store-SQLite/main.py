import colorama
from colorama import Fore
from _sqlite3 import connect

# ------------------init--------------------
colorama.init()
print('Loading...')
# ___ connect to databes ___
try:
    con = connect('Assignment17/Store-SQLite/products.db')
    my_cursor = con.cursor()
    my_cursor.execute('SELECT * FROM products')
    products = my_cursor.fetchall()
    print(Fore.LIGHTCYAN_EX + 'data loaded! \nwelcome dear user!')

except Exception as e:
    print("error: ", e)
    exit()

cart = []

# -----------------process-------------------


def updateProductList():
    global products
    my_cursor = con.cursor()
    my_cursor.execute('SELECT * FROM products')
    products = my_cursor.fetchall()


def addNewProduct():
    print(Fore.LIGHTWHITE_EX +'________ adding a product ________ \n***please enter the product details***')
    name = input('NAME: ')
    for p in products:
        if name == p[1]:
            print('this product exists in the store')
            break
    else:
        price = input('PRICE: ')
        count = input('COUNT: ')
        my_cursor.execute(f"INSERT INTO products(NAME, COUNT, PRICE) VALUES('{name}', {count}, {price})")
        updateProductList()
        print(Fore.GREEN + 'Done!')
    menu()


def search():
    user_input = input('enter ID or NAME of product: ')

    if user_input.isnumeric():
        my_cursor.execute(f"SELECT * FROM products WHERE ID = {user_input}")
    else:
        my_cursor.execute(f"SELECT * FROM products WHERE NAME = '{user_input}'")
    print(Fore.WHITE + str(my_cursor.fetchone()))
    if not my_cursor:
        print(Fore.RED + 'not found')
    menu()


def edit():
    print(Fore.LIGHTWHITE_EX + '______ editing a product ______')
    user_input = input('enter name of product that you want to edit: ')

    for p in products:
        if user_input == p[1]:
            name = input('new name: ')
            price = input('new price: ')
            count = input('new count: ')
            my_cursor.execute(f"UPDATE products SET NAME = '{name}', COUNT = '{count}', PRICE = '{price}' WHERE name='{user_input}'")
            updateProductList()
            print(Fore.GREEN + 'Done!')
            break
    else:
        print(Fore.LIGHTCYAN_EX + 'this product is not exists in the store')
    menu()


def remove():
    print(Fore.LIGHTWHITE_EX + '______ Deleting a product ______')
    name = input('please enter the product name: ')

    if any(name == p[1] for p in products):
        my_cursor.execute(f"DELETE FROM products WHERE NAME = '{name}'")
        updateProductList()
        print(Fore.GREEN + 'Done!')
    else:
        print(Fore.LIGHTCYAN_EX + 'this product is not exists in the store')
    menu()


def buy():
    print(Fore.LIGHTWHITE_EX + '______  BUY  ______')

    while True:
        code = int(input('please enter the product code: '))
        for product in products:
            if code == product[0]:
                count = int(input('how many? '))
                if count <= int(product[3]):
                    cart.append(str(count) + '\t' + product[1])
                    my_cursor.execute(f"UPDATE products SET COUNT = {product[3] - count} WHERE ID = {code}")
                    updateProductList()
                else:
                    print(Fore.LIGHTCYAN_EX +
                          f"only {product[3]} of this product are available")
                break
        else:
            print(Fore.LIGHTCYAN_EX + 'this product is not exist in store')

        print(Fore.LIGHTWHITE_EX + 'do you want another product?\n y? n? ')
        yORn = input()
        if yORn != 'y':
            showCart()
            break


def showAll():
    for p in products:
        print(Fore.LIGHTMAGENTA_EX + f"ID: {p[0]},  NAME: {p[1]},  PRICE: {p[2]},  COUNT: {p[3]}")
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
    con.commit()
    print(Fore.LIGHTGREEN_EX + 'Thanx! Goodbye')
    exit()


def menu():
    print(Fore.LIGHTYELLOW_EX + '\n 1- add new product \n 2- search \n 3- edit \n 4- remove \n 5- buy \n 6- show all \n 7- show cart \n 8- save changes and exit')
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