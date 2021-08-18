from os import write
from pyfiglet import Figlet

def addkala():
    kala= open("database.txt", "a")
    print()
    
    kala = input("enter your add for  id kala:")
    name = input('name: ')
    price = input('price: ')
    count = input('count: ')
    productDict = {}
    productDict['id'] = kala
    productDict['name'] = name
    productDict['price'] = int(price)
    productDict['count'] = int(count)
    PRODUCTION.append(productDict)
    print(PRODUCTION) 

def editkala():

    kala = int(input("enter yor edit kala :"))
    
    PRODUCTION[kala]
    name = input('enter your name kala: ')
    if name!='d':
            PRODUCTION[kala]['name'] = name
    price = input('price: ')
    if price!='d':
            PRODUCTION[kala]['price'] = price
    count = input('count: ')
    if count!='d':
            PRODUCTION[kala]['count'] = count
    print('anjam shod')

def delkala():
    id= int(input("enter your id kala for delete :"))
    for i in range(len(PRODUCTION)):
        if PRODUCTION[i]["id"]==id:
            PRODUCTION.pop(i)
            print("hazf shod")
    print()        
def search():
    
        name = input("your name kala for jostojo :")

        for i in range(len(PRODUCTION)):
        
           if PRODUCTION[i]['name'] == name:
            print(PRODUCTION[i]) 
        print(" kala peida shod ")
                
            
       
        

def exit():
    myFile = open("database.txt", "w")
    for i in PRODUCTION:
        f= PRODUCTION[i]["id"]+","+PRODUCTION[i]["name"]+","+ PRODUCTION[i]["price"] +","+ PRODUCTION[i]["count"]
        myFile.write(str(f))
    myFile.close()        
def show_list():
    for i in range(len(PRODUCTION)):
        print(PRODUCTION[i] )

def show_menu():

    print("1- add product")
    print("2-edit product")
    print("3- delete product")
    print("4- search")
    print("5-show list")
    print("6-buy")
    print("7- exit")

def load():

        print("loading......")

        myfile=open("database.txt", "r")
        data= myfile.read()
        
        production_list=data.split("\n")
        
        for i in range (len(production_list)):
            production_info=production_list[i].split(",")
            mydict={}
            mydict["id"]=production_info[0]
            mydict["name"]=production_info[1]
            mydict["price"]=production_info[2]
            mydict["count"]=production_info[3]
            PRODUCTION.append(mydict)
        print("Wellcome")
PRODUCTION=[]
        
    
load()

f=Figlet(font="standard")
print(f.renderText("YASAMIN   STORE"))


while True:

    show_menu()
    choice= int(input("please choose a number : "))

    if choice ==1:
        addkala()
    elif choice==2:
        editkala()
    elif choice==3:
        delkala()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
        
    elif choice==6:
        pass
    elif choice==7:
        exit()
        a=input("save change ? (y/n")
        if a=="n":
            exit()
        elif a=="y":
            write.PRODUCTION()  
            exit()      