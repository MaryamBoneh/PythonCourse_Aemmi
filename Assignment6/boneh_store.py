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
i = 0

# ___ filling the product list in dictionary format ___
while i < len(parts):
    info = parts[i].split(',')
    products.append({'ID': info[0], 'NAME': info[1],
                     'PRICE': info[2], 'COUNT': info[3], 'DELETED': info[4]})
    i += 1
print(Fore.LIGHTCYAN_EX + 'data loaded! \nwelcome dear user!')

# -----------------process-------------------


def addNewProduct():
    print(Fore.LIGHTWHITE_EX + '___ adding a product ___ \n***please enter the product details***')
    name = input('NAME: ')

    for i in range(len(products)):
        if name == products[i]['NAME']:
            print('this product exists in the store')
            break
    else:
        price = input('PRICE: ')
        count = input('COUNT: ')
        pid = int(products[len(products)-1]['ID']) + 1
        # ___ update csv file ___
        f = open('Assignment6/products.csv', 'a')
        f.write('\n' + str(pid) + ',' + name +
                ',' + price + ',' + count + ',0')
        f.close()
        # ___ update products list ___
        products.append({'ID': pid, 'NAME': name, 'PRICE': price, 'COUNT': count, 'DELETED': '0'})
        
        print(Fore.GREEN + 'Done!')
    menu()


def search():
    user_input = input('enter ID or NAME of product: ')
    for product in products:
        if product['ID'] == user_input or product['NAME'] == user_input:
            print(product)
            break
    else:
        print('not found')
        
    menu()


def edit():
    print(Fore.LIGHTWHITE_EX + '___ editing a product ___')
    name = input('enter name of product that you want to edit: ')
    for i in range(len(products)):
        if name == products[i]['NAME']:
            new_name = input('new name: ')
            new_price = input('new price: ')
            new_count = input('new count: ')
            num_line = int(products[i]['ID']) - 1000
            # ___ update csv file ___
            product_list = open('Assignment6/products.csv', 'r').readlines()
            product_list[num_line] = product_list[num_line].replace(products[num_line]['NAME'], new_name)\
                .replace(products[num_line]['PRICE'], new_price)\
                .replace(products[num_line]['COUNT'], new_count)
            out = open('Assignment6/products.csv', 'w')
            out.writelines(product_list)
            out.close()
            # ___ update products list ___
            products[num_line]['NAME'] = new_name
            products[num_line]['PRICE'] = new_price
            products[num_line]['COUNT'] = new_count
            break
    else:
        print(Fore.LIGHTCYAN_EX + 'this product is not exists in the store')

    menu()


def remove():
    print(Fore.LIGHTWHITE_EX + '___ deleting a product ___')
    name = input('please enter the product name: ')
    for i in range(len(products)):
        if name == products[i]['NAME']:
            print(Fore.LIGHTRED_EX +
                  'are you sure you want delete this product? \n  yes?  no? ')
            yORn = input()
            if yORn == 'yes':
                num_line = int(products[i]['ID']) - 1000
                # ___ update csv file ___
                product_list = open('Assignment6/products.csv', 'r').readlines()
                product_list[num_line] = product_list[num_line][:-2] + "1\n"
                out = open('Assignment6/products.csv', 'w')
                out.writelines(product_list)
                out.close()
                # ___ update products list ___
                products[num_line]['DELETED'] = '1'
                break
    else:
        print(Fore.LIGHTCYAN_EX + 'this product is not exists in the store')

    menu()


def buy():
    pass
    menu()


def showAll():
    for i in range(len(products)):
        if products[i]['DELETED'] == '0':
            print('ID: ' + products[i]['ID'] + ',  NAME: ' + products[i]['NAME'] +
                  ',  PRICE: ' + products[i]['PRICE'] + ',  COUUNT: ' + products[i]['COUNT'])
    menu()


def menu():
    print(Fore.LIGHTYELLOW_EX +
          '\n 1- add new product \n 2- search \n 3- edit \n 4- remove \n 5- buy \n 6- show all \n 7- exit')
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
    else:
        exit()


menu()
