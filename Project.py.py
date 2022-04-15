print('''******************************************************************************************************************************************
                                                              WELCOME TO RIY GENERAL STORE
**************************************************************************************************************************************************''')
print('admin name :kyumna14')
print('current password :Yumna1!\nNOTE:\nYou can change it later')
import sys
from datetime import date,datetime
today = date.today()
date=today.strftime("%d/%m/%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def home_page():
    print('''Login As:
1)User
2)Administrator
3)Exit''')
    login_as = int(input('Enter Your Choice :'))
    if login_as<1 or login_as>3:
        print('Invalid Entry!!!')
        home_page()
    else:
        if login_as == 1:
            us=user()
            o=inventory()
            print('''1)Login to your account
2)Create an account''')
            while True:
                choice = input('enter your choice : ')
                if choice<'1' or choice>'2':
                    print('Invalid entry!!!')
                else:
                    break
            if choice == '2':
                us.create_account()
            if choice == '1':
                o.login()
                o.read_from_file()
                o.features()
        if login_as == 2:
            a = admin()
            a.check_password()
        if login_as==3:
            sys.exit(0)
from abc import ABC,abstractmethod  

class abstract_user(ABC):
    @abstractmethod
    def read_user_info(self):
        pass
    @abstractmethod
    def create_account(self):
        pass
    @abstractmethod
    def update_user_file(self):
        pass
    @abstractmethod
    def read_shopping_history(self):
        pass
    @abstractmethod
    def writing_shop_history(self):
        pass
    @abstractmethod
    def write_current_cart(self):
        pass
    @abstractmethod
    def read_current_cart(self):
        pass
    @abstractmethod
    def remove_current_cart(self):
        pass

class abstract_inventory(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def update_cart(self):
        pass
    @abstractmethod
    def features(self):
        pass
    @abstractmethod
    def read_from_file(self):
        pass
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def select_product(self):
        pass
    @abstractmethod
    def check_quantity(self):
        pass
    @abstractmethod
    def update_file(self):
        pass
    @abstractmethod
    def Add_products(self):
        pass
    @abstractmethod
    def remove_from_cart(self):
        pass
    @abstractmethod
    def password_recovery(self):
        pass
    @abstractmethod
    def change_password(self):
        pass
    @abstractmethod
    def check_out(self):
        pass
    @abstractmethod
    def personal_info_review(self):
        pass
    @abstractmethod
    def view_history(self):
        pass
    @abstractmethod
    def view_current_cart(self):
        pass
    @abstractmethod
    def change_personal_info(self):
        pass
    @abstractmethod
    def logout(self):
        pass

class abstract_admin(ABC):
    @abstractmethod
    def check_password(self):
        pass
    @abstractmethod
    def display_admin_operations(self):
        pass
    @abstractmethod
    def add_stock(self):
        pass
    @abstractmethod
    def edit_price(self):
        pass
    @abstractmethod
    def delete_user(self):
        pass
    @abstractmethod
    def display_users(self):
        pass
    @abstractmethod
    def writing_shop_history(self):
        pass
    @abstractmethod
    def write_current_cart(self):
        pass
    

    

class list_of_users:
    user_list=[]

    @classmethod                                                                  #CLASS METHOD
    def users(cls):
        f=open('user_admin.txt','a+')
        f.seek(0)
        for i in f:
            lst=eval(i)
            list_of_users.user_list.append(lst[0])
        list_of_users.user_list.pop(0)

        
    

class user(abstract_user):                                                                      #CLASS USER
    dic = {}
    history={}
    current_cart={}

# Reading user information from the file

    def read_user_info(self,obj=None):
        if obj==None:
            obj=self
        f = open('user_admin.txt', 'a+')
        f.seek(0)
        for i in f:
            lst = eval(i)
            user.dic.update({lst[0]: lst[1]})
        f.close()

# Creating new user account

    def create_account(self):
        d = {}
        lst = []
        self.read_user_info()
        while True:
            try:                                                                                                 # EXCEPTION HANDLING
                f_name = input('Enter your first name in block letters :')
                if f_name.isupper() == False:
                    raise Exception
                break
            except:
                print('Enter name in block letters!!!')
        while True:
            try:                                                                                                   # EXCEPTION HANDLING
                l_name = input('Enter your last name in block letters :')
                if l_name.isupper() == False:
                    raise Exception
                break
            except:
                print('Enter name in block letters!!!')

        user_name = input('Enter user name :')
        while True:
            if user_name in user.dic:
                user_name = input('Enter another user name :')
            else:
                break
        DOB = input('Enter your date of birth :')
        phone_number = input('Enter your phone number :')
        city = input('Enter your city :')
        address = input('Enter your address :')
        email = input('Enter your email address :')
        print('''\nPassword must Alpha numeric with atleast one uppercase and lowercase letter
Minimum password length should be 6 characters
Maximum length of 8 characters
Must contain atleast one special character \n''')
        while True:
            password = input('Enter your password :')
            a=self.password_validation(password) 
            if a == True:
                break
        
        print('PROCESSING...')
        lst = [f_name, l_name, DOB, phone_number,city, address, email, password]

        d = {user_name: lst}
        f = open('user_admin.txt', 'w')
        user.dic.update(d)
        for j in user.dic.items():
            j = list(j)
            f.write(f"{j}\n")
        f.close()
        home_page()

# Checking if the password is valid or not

    @staticmethod                                                 #STATIC METHOD                                    
    def password_validation(password,obj=None):
        '''it takes 1 argument \'password\' and returns True if password is valid False otherwise'''
       
        valid = True
        while True:
            SpecialSym = ['$', '@', '!']
           
            if len(password) < 6:
                print('the length of password should be at least 6 char long')
                valid = False
                return False
            if len(password) > 8:
                print('the length of password should be not be greater than 8')
                valid = False
                return False
            if not any(char.isdigit() for char in password):
                print('the password should have at least one numeral')
                valid = False
                return False
            if not any(char.isupper() for char in password):
                print('the password should have at least one uppercase letter')
                valid = False
                return False
            if not any(char.islower() for char in password):
                print('the password should have at least one lowercase letter')
                valid = False
                return False
            if not any(char in SpecialSym for char in password):
                print('the password should have at least one of the symbols $@!')
                valid = False
                return False
            if '#' in password:
                print('You cannot use \'#\' in your password')
                valid = False
                return False
            else:
                return True
                break
            
#Updating user information in file

    def update_user_file(self,d,obj=None):
        f = open('user_admin.txt', 'w')
        user.dic.update(d)
        for j in user.dic.items():
            j = list(j)
            f.write(f"{j}\n")
        f.close()

# Reading user's shopping history from file

    def read_shopping_history(self,obj=None):
        f=open('shopping.txt','a+')
        f.seek(0)
        for i in f:
            lst=eval(i)
            user.history.update({lst[0]:lst[1]})
        f.close()

#Writing user's shopping history       

    def writing_shop_history(self,dic,user_name,obj):
        f=open('shopping.txt','w')
        lst1=[]
        lst=user.history.get(user_name)
        if user.history.get(user_name)==None:
            lst1.append(dic)
            user.history.update({user_name:lst1})
        else:
            lst.append(dic)
        for j in user.history.items():
            j=list(j)
            f.write(f'{j}\n')
        f.close()

#Saving current cart of user in file 

    def write_current_cart(self,user_name,cart,obj=None):
        f=open('current_cart.txt','w')
        lst1=[]
        lst=user.current_cart.get(user_name)
        if user.current_cart.get(user_name)==None:
            lst1.append(cart)
            user.current_cart.update({user_name:lst1})
        else:
            lst1.append(cart)
            user.current_cart.pop(user_name)
            user.current_cart.update({user_name:lst1})
        for j in user.current_cart.items():
            j=list(j)
            f.write(f'{j}\n')
        f.close()
        
#Reading current cart from file        

    def read_current_cart(self,user_name,obj=None):
        f=open('current_cart.txt','a+')
        f.seek(0)
        for i in f:
            lst=eval(i)
            user.current_cart.update({lst[0]:lst[1]})
        if user.current_cart.get(user_name)==None:
            return False
        else:
            lst1=user.current_cart.get(user_name)
            return lst1
        f.close()

#Removing current cart of user from file when the user checkouts

    def remove_current_cart(self,user_name,obj):
        user.current_cart.pop(user_name)
        f=open('current_cart.txt','w')
        for j in user.current_cart.items():
            j=list(j)
            f.write(f'{j}\n')
        f.close()
        
            
        
        
                                        
class inventory(abstract_inventory):                                         # CLASS INVENTORY
    products = {}
    unit_price = {}
    stock = {}
# Initializing instance variables

    def __init__(self):
        self.cart = {}
        self.u=user()                                                                         #ASSOCIATION
        self.history={}

#User login        

    def login(self):
        '''it reads the file and appends it to the dictionary '''
        self.u.read_user_info(self)
        while True:
            try:                                                                                #EXCEPTION HANDLING
                self.user_name = input('Enter Username :')
                if self.user_name not in user.dic:
                    raise Exception
                break
            except:
                print('Incorrect Username!!!')
        while True:
            self.password = input('Enter Password :')
            if self.password == user.dic.get(self.user_name)[7]:
                print('LOGGING IN...')
                print('HI',str(user.dic.get(self.user_name)[0]),str(user.dic.get(self.user_name)[1]))
                break
            else:
                print('Incorrect password!!!')
                P = input('Forgot Password?[Y/N]')
                if P == 'Y' or P == 'y':
                    self.password_recovery(self.user_name)
                else:
                    continue
        self.update_cart()
        
#Loading items of current cart from file in to the program

    def update_cart(self):
        a=self.u.read_current_cart(self.user_name,self)
        if a==False:
            return False
        else:
            for k in a:
                        for j in k:
                            self.cart.update({j:k.get(j)})
       
#Displaying features of application for user

    def features(self):
        print('''Select from the following option:
1)Shopping
2)View Shopping History
3)View Your Current Cart
4)Add products to your cart
5)Remove products from your cart
6)Check out
7)Settings
8)Logout''')
        choice=int(input('Enter Your Choice:'))
        if choice<1 or choice>8:
            print('Invalid entry!!!')
            self.features()
        else:
            if choice==1:
                
                if self.cart=={}:
                    self.display()
                else:
                    shopping=input('If you start shopping your previous order saved in cart will be removed\nDo you want to continue?[Y/N]')
                    if shopping=='y' or shopping=='Y':
                        self.u.remove_current_cart(self.user_name,self)
                        self.cart={}
                        self.display()
                    else:
                        self.features()
            if choice==2:
                self.view_history()
            if choice==3:
                self.view_current_cart()
                self.features()
            if choice==4:
                self.Add_products()
            if choice==5:
                self.remove_from_cart()
            if choice ==6:
                self.check_out()
            if choice==7:                              
                print('''1)Review your personal info.         
2)Change your personal info.
3)Change password
4)Delete credit card information''')
                while True:
                    settings=int(input('Enter your choice...'))
                    if settings<1 or settings>4:
                        print('Invalid Entry!!!')
                    else:
                        break
                if settings==1:
                    self.personal_info_review()
                    input('Press enter to continue...')
                if settings==2:
                    self.change_personal_info()
                if settings==3:
                    self.change_password(self.user_name)
                if settings==4:
                    self.del_credits()
                self.features()
            if choice==8:
                self.logout()
                home_page()

# Loading Data From The File

    def read_from_file(self):
        details = open('stock.txt', 'r')

# First line of the file is number of items

        number_of_items = int((details.readline()).rstrip("\n"))

# Adding products dictionary

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip("\n")
            o1, o2 = line.split('#')
            o1 = int(o1)
            o2 = o2
            inventory.products.update({o1: o2})

# Adding unit_price dictionary

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip("\n")
            o1, o2 = line.split('#')
            o1 = int(o1)
            o2 = float(o2)
            inventory.unit_price.update({o1: o2})

# Adding stock dictioanry

        for i in range(0, number_of_items):
            line = (details.readline()).rstrip('\n')
            o1, o2 = line.split("#")
            o1 = int(o1)
            o2 = int(o2)
            inventory.stock.update({o1: o2})

        details.close()
        return inventory.products

# Displaying products

    def display(self):
        print('DISPLAYING ALL ITEMS...')
        a='Product Nmuber'
        b='Items'
        c='Price'
        print(f'{a:^20}{b:^20}{c:^20}')
        print()
        for i in range(1, 13):
            print(
                f'{i:^20}{inventory.products.get(i):^20}{inventory.unit_price.get(i):^20}')
        self.select_product()

# Selection of products to enter in to the cart

    def select_product(self):
        selection = int(input('How many items do you want to order?'))
        print('Enter product number one by one')
        for o in range(0, selection):
            while True:
                try:                                                                                                                      #EXCEPTION HANDLING
                    product_number=int(input('Enter Product Number :'))
                    if product_number<1 or product_number>12:
                        raise Exception
                    break
                except:
                    print('Invalid product number!!!')
    
            if product_number in self.cart:
                while True:
                    try:                                                                                                                    #EXCEPTION HANDLING
                        print('Enter quantity of', inventory.products.get(product_number),' : ', end='')
                        again_quantity = int(input())
                        if again_quantity<0:
                            raise Exception
                        break
                    except:
                        print('Invalid Quantity!!!')
                self.check_quantity(again_quantity, product_number)
                new_quantity = self.cart.get(product_number)+again_quantity
                self.cart.pop(product_number)
                self.cart.update({product_number: new_quantity})
            
                continue
            while True:
                try:
                    print('enter quantity of', inventory.products.get(product_number),' : ', end='')  #EXCEPTION HANDLING
                    quantity = int(input())
                    if quantity<0:
                        raise Exception
                    break
                except:
                    print('Invalid Quantity!!!')
            a=self.check_quantity(quantity, product_number)
            if a == None:
                pass
            else:
                self.cart.update({product_number:a})
        continues = input('Do you want to continue shopping?[Y/N]')
        if continues == 'y' or continues == 'Y':
            self.display()
        else:
            a=self.u.read_shopping_history(self)

            self.u.write_current_cart(self.user_name,self.cart,self)
            self.features()

    def update_history(self):
        for i in self.cart:
            self.history.update({i:[inventory.products.get(i),self.cart.get(i),self.cart.get(i)*inventory.unit_price.get(i)]})
            self.history.update({'d':[date,current_time,self.paid_thuru]})
        self.u.writing_shop_history(self.history,self.user_name,self)
        
            
#Comparing the quantity entered by user with stock

    def check_quantity(self, quantity, product_number):
        '''it takes 3 arguments self,quantity and product_number \ncompare the quantity with stock and returns quantity'''
        if quantity <= inventory.stock[product_number]:
            value = inventory.stock.get(product_number)-quantity
            inventory.stock.pop(product_number)
            d2 = {product_number: value}
            inventory.stock.update(d2)
            return quantity

        if quantity > inventory.stock[product_number] and inventory.stock[product_number] != 0:
            print('Only', inventory.stock[product_number], ' packs are available')
            add = input('Do you want to add them[Y/N]')
            if add == 'y' or add == 'Y':
                print(inventory.stock[product_number], 'packs are added')
                inventory.stock.pop(product_number)
                d3 = {product_number: 0}
                inventory.stock.update(d3)
                return inventory.stock.get(product_number)

        if inventory.stock[product_number] == 0:
            print('OUT OF STOCK!!!')
        self.update_file()
        


# Updating the stock file


    def update_file(self):
        details = open('stock.txt', 'w')
        details.write('12'+'\n')
        for i in inventory.products:
            details.write(str(i)+'#'+inventory.products.get(i)+'\n')
        for i in inventory.unit_price:
            details.write(str(i)+'#'+str(inventory.unit_price.get(i))+'\n')
        for i in inventory.stock:
            details.write(str(i)+'#'+str(inventory.stock.get(i))+'\n')
        details.close()

#adding products to cart after shopping

    def Add_products(self):
        self.display()
        self.features()

#removing products from current cart after shopping

    def remove_from_cart(self):
        return_value=self.view_current_cart()
        if return_value==False:
            self.features()
            return
        remove = int(input('Enter product number you want to remove from your cart:'))
        if remove in self.cart:
            print('Are you sure you want to remove', inventory.products.get(remove), 'from your cart?[Y/N]', end='')
            confirmation = input()
            if confirmation == 'y' or confirmation == 'Y':
                new_value = inventory.stock.get(remove)+self.cart.get(remove)
                self.cart.pop(remove)
                inventory.stock.update({remove: new_value})
                self.update_file()
                print('PRODUCT SUCCESSFULY REMOVED FROM CART...')
            else:
                pass
        else:
            print('This product does\'nt exsist in your cart')
        
        self.u.write_current_cart(self.user_name,self.cart,self)
        input('Press enter to continue...')
        self.features()
        
#Checking out

    def check_out(self):
        if self.cart=={} and user.current_cart=={}:
            print('Your Cart Is Empty!!!')
            input('Press Enter To Continue...')
            self.features()
        
        else:
            sub_total = 0
            print('DISPLAYING YOUR CART...')
            self.view_current_cart()
            print('YOUR TOTAL IS:')
            
            for k in self.cart:
                total = inventory.unit_price.get(int(k))*self.cart.get(int(k))
                sub_total += total
            print(sub_total, 'Rs.')
            if sub_total<100:
                print('You can not place order of less than 100 Ruppees!!!')
                input('Press enter to continue...')
                self.features()
            else:
                print('PAYMENT METHOD...\n1)Credit Card\n2)Cash\nEnter your choice:', end='')
                payment_method = int(input())
                if payment_method == 1:
                    if len(user.dic.get(self.user_name))==8:
                        while True:
                            try:                                                            #EXCEPTION HANDLING
                                self.card_number = input('Enter card number:')
                                if len(self.card_number)==16:
                                    break
                                else:
                                    raise Exception
                            except:
                                print('Invalid Credit Card Number!!!')
                        while True:
                            try:                                                            #EXCEPTION HANDLING
                                self.CVC = input('Enter CVC:')
                                if len(self.CVC)==3:
                                    break
                                else:
                                    raise Exception
                            except:
                                print('Invalid CVC!!!')
                        saving=input('Do you want to save your credit card information?[Y/N] :')
                        if saving =='y' or saving=='Y':
                            lst=user.dic.get(self.user_name)
                            lst.append(self.CVC)
                            lst.append(self.card_number)
                            user.dic.pop(self.user_name)
                            user.dic.update({self.user_name:lst})
                            self.u.update_user_file(user.dic,self)
                        else:
                            pass
                    else:
                        c_n=user.dic.get(self.user_name)[9]
                        cvc=user.dic.get(self.user_name)[8]
                        print('Your credit card number is : ',c_n)
                        print('CVC : ',cvc)
                    self.paid_thuru='Paid through Credit Card'
                else:
                    self.paid_thuru='Cash on Delivery'

                print('Estimated Delivery Time is 25 minutes')
                input('Press enter to review payment and address')
                print('Address:',user.dic.get(self.user_name)[5])
                print('Delivery Fees: 50 Rs.')
                print('Subtotal',50+sub_total,'Rs.')
                print('CHECKING OUT...')
                self.u.remove_current_cart(self.user_name,self)
                self.update_history()
                self.cart={}
                input('Press enter to continue...')
                self.features()
        
#this function will change password 

    def change_password(self,user_name):
        old_password = input('Enter the current password :')
        if old_password == user.dic.get(user_name)[7]:
            print('''\nPassword must Alpha numeric with atleast one uppercase and lowercase letter
Minimum password length should be 6 characters
Maximum length of 8 characters
Must contain atleast one special character \n''')
            while True:
                new_password = input('Enter new password :')
                a=user.password_validation(new_password) 
                if a == True:
                    break
            print('Are you sure you want to change your password?[Y/N]', end='')
            confirmation = input()
            if confirmation == 'y' or confirmation == 'Y':
                user.dic.get(user_name)[7]= new_password
                self.u.update_user_file(user.dic)
                print('Password Changed Successfully...')
        else:
            print('You entered wrong password!!!\nForgot Password?[Y/N]', end='')
            forgot_password = input()
            if forgot_password == 'y' or forgot_password == 'Y':
                self.password_recovery(user_name)
            else:
                self.change_password(user_name)

#recovering password if the user forgets password while logging in

    def password_recovery(self,name):
        mobile_number = input('Enter your mobile number:')
        if mobile_number == user.dic.get(name)[3]:
            print('''Password must Alpha numeric with atleast one uppercase and lowercase letter
Minimum password length should be 6 characters
Maximum length of 8 characters
Must contain atleast one special character ''')
            while True:
                new_password = input('Enter new password :')
                a=self.u.password_validation(new_password,self) 
                if a == True:
                    break
            user.dic.get(name)[7] = new_password
            self.u.update_user_file(user.dic,self)
            print('Password Changed Successfuly!!!')
        else:
            print('The mobile number entered is wrong!!!')
            self.password_recovery(name)
        input('Press enter to continue...')

#displaying personal information of user


    def del_credits(self):
        if len(user.dic.get(self.user_name))==8:
            print('You have not stored any credit card information!!!')
        else:
            confirm=input('Are you sure you want to delete your credit card information?[Y/N] : ')
            if confirm =='y' or confirm =='Y':
                lst=user.dic.get(self.user_name)
                lst.pop(8)
                lst.pop(8)
                user.dic.pop(self.user_name)
                user.dic.update({self.user_name:lst})
                self.u.update_user_file(user.dic,self)
                print('Information deleted successfuly!!!')
            else:
                return

    def personal_info_review(self):
        print()
        print('*****************************************\n')
        print('First Name :',user.dic.get(self.user_name)[0])
        print('Last Name :',user.dic.get(self.user_name)[1])
        print('Date Of Birth :',user.dic.get(self.user_name)[2])
        print('Phone Number :',user.dic.get(self.user_name)[3])
        print('City :',user.dic.get(self.user_name)[4])
        print('Address :',user.dic.get(self.user_name)[5])
        print('Email :',user.dic.get(self.user_name)[6])
        print()
        print('******************************************')
        print()
        

#displaying shopping history of user

    def view_history(self):
        order=0
        self.u.read_shopping_history(self)
        lst=user.history.get(self.user_name)
        if lst == None:
            print('You don\'t have any shopping history!!!')
            input('Press enter to continue...')
        else:
            for i in lst:
                sub_total=0
                order+=1
                a='Product Number'
                b='Product'
                c='Unit Price'
                d='Quantity'
                e='Total'
                print()
                print('ORDER NO.',order)
                print(f'{a:^20}{b:^20}{c:^20}{d:^20}{e:^20}')
                print()
                
                details=i.get('d')
                i.pop('d')
                for j in i:
                    print(f'{j:^20}{inventory.products.get(j):^20}{inventory.unit_price.get(j):^20}{i.get(j)[1]:^20}{int(inventory.unit_price.get(j))*int(i.get(j)[1]):^20}')
                    sub_total+=int(inventory.unit_price.get(j))*int(i.get(j)[1])
                print('Sub Total =',sub_total)
                
                print('Dated : ',details[0])
                print('Time : ',details[1])
                print('Method of Payment : ',details[2])
                
                
                print()
                print('*******************************************************************************************************************************************')
                print()
        self.features()

#displaying current cart of user

    def view_current_cart(self):
        if self.cart=={}:
            print('You have\'nt saved any products in your current!!!')
            input('Press Enter to continue...')
            return False
        if self.cart!={}:
            print('Your current cart contains :')
            print()
            a='Product Number'
            e='Product Name'
            b='Quantity'
            c='Price'
            d='Total Price'
            print(f'{a:^22}{e:^20}{b:^20}{c:^20}{d:^20}')
            print()
            for i in self.cart:
                print(f'{i:^22}{inventory.products.get(int(i)):^20}{self.cart.get(int(i)):^20}{inventory.unit_price.get(int(i)):^20}{inventory.unit_price.get(int(i))*self.cart.get(int(i)):^20}')
            print()
            print('***************************************************************************************************')
            print()
#user can change his/her personal information

    def change_personal_info(self):
        lst=user.dic.get(self.user_name)
        self.personal_info_review()
        while True:
            print('''what do you want to change:
1)First Name
2)Last Name
3)Date of Birth
4)Phone Number
5)City
6)Address
7)Mail
8)Go Back''')
            changes=int(input('Enter Serial Number :'))
            if changes==1:
                name=input('Enter First Name :')
                lst[0]=name
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes==2:
                l_name=input('Enter Last Name :')
                lst[1]=l_name
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes==3:
                dob=input('Enter date of birth :')
                lst[2]=dob
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes==4:
                ph=input('Enter new phone number :')
                lst[3]=ph
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes==5:
                cou=input('Enter city :')
                lst[4]=cou
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes==6:
                add=input('Enter new address :')
                lst[5]=add
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes==7:
                mail=input('Enter new mail :')
                lst[6]=mail
                print('CHANGES DONE SUCCESSFULY!!!')
            if changes ==8:
                break
        self.features()

#logging out the user

    def logout(self):
        self.cart={}
        inventory.stock={}
        inventory.products={}
        inventory.unit_price={}
        user.dic={}
        user.history={}
        user.current_cart={}
        list_of_users.user_list={}

class admin(abstract_admin,inventory, user,list_of_users):                                                  #CLASS ADMIN
                                                                                                        
#admin login block

    def check_password(self):
        super().read_user_info()
        while True:
            self.name = input('Enter Admin name :')
            if self.name not in user.dic:
                print('Invalid Username!!!')
            else:
                break
        while True:
            self.password = input('Enter Password :')
            if self.password!=user.dic.get(self.name)[7]:
                print('Wrong Password!!!')
                forget=input('Forgot Password?[Y/N]')
                if forget=='y' or forget=='Y':
                    super().password_recovery(self.name)
                else:
                    continue
            else:
                print('LOGGING IN...')
                self.display_admin_operations()
    

#features that admin can use

    def display_admin_operations(self):
        print('''What do you want to do:
1)Add Stock
2)Edit Price
3)Remove User                                                                  
4)Change password
5)Display All Users
6)Logout''')
        operation = int(input('Enter your choice:'))
        if operation<1 or operation>6:
            print('invalid choice!!!')
            self.display_admin_operations()
        else:
            if operation == 1:
                self.add_stock()
            if operation == 2:
                self.edit_price()
            if operation==3:
                self.delete_user()
            if operation == 4:
                super().change_password(self.name)
                input('Press Enter to continue...')
                self.display_admin_operations()
            if operation==5:
                self.display_users()
            if operation==6:
                super().logout()
                home_page()

#adding stock and updating the file

    def add_stock(self):
        super().read_from_file()
        pr_no = int(input('Enter product number:'))
        stock = int(input('Enter stock:'))
        total_stock=stock+inventory.stock.get(pr_no)
        super().stock.update({pr_no:total_stock})
        super().update_file()
        print('Stock Added Successfuly')
        input('Press enter to continue...')
        self.display_admin_operations()

#editing the price of products and updating the file

    def edit_price(self):
        super().read_from_file()
        pr_no = int(input('Enter product number :'))
        new_price = float(input('Enter new price :'))
        super().unit_price.update({pr_no: new_price})
        super().update_file()
        print('Price Updated Successfuly ')
        input('Press enter to continue...')
        self.display_admin_operations()
       
#deleting a user

    def delete_user(self):
        
        user_no=0
        list_of_users.users()
        print()
        print('Displaying All Users')
        print()
        print('**********************************************************')
        print()
        for i in list_of_users.user_list:
            user_no+=1
            print('User No.',user_no)
            print(i)
            print()
            print('******************************************************')
            print()
        print('which user do you want to delete?\nEnter user name :',end='')
        user_name=input()
        super().read_shopping_history()
        super().read_current_cart(user_name)

        if user_name in list_of_users.user_list:
            indices=list_of_users.user_list.index(user_name)
            list_of_users.user_list.pop(indices)
            user.dic.pop(user_name)

            if user_name in user.history:
                user.history.pop(user_name)
                self.writing_shop_history()
                

            if user_name in user.current_cart:
                user.current_cart.pop(user_name)
                self.write_current_cart()

            f=open('user_admin.txt','w')
            for j in user.dic.items():
                j = list(j)
                f.write(f"{j}\n")
            f.close()
            print('User Removed Successfuly!!!')
            print()
            list_of_users.user_list=[]
            
            
        else:
            print('Any user does not contain the eneterd user name!!!')
        input('Press enter to continue...')
        self.display_admin_operations()

#displaying all the users with their complete information

    def display_users(self):

        users=1
        for j in user.dic:
            if j=='kyumna14':
                pass
            else:
                print('User No.',users)
                print('First Name :',user.dic.get(j)[0])
                print('Last Name :',user.dic.get(j)[1])
                print('Date Of Birth :',user.dic.get(j)[2])
                print('Phone Number :',user.dic.get(j)[3])
                print('City :',user.dic.get(j)[4])
                print('Address :',user.dic.get(j)[5])
                print('Email :',user.dic.get(j)[6])
                print('********************************************')
                users+=1
        input('press enter to continue...')
        self.display_admin_operations()

#updating history file after deleting user

    def writing_shop_history(self):                                                 #METHOD OVERRIDING
        w=open('shopping.txt','w')
        for k in user.history.items():
            k=list(k)
            w.write(f'{k}\n')
        w.close()

#updating current cart file after deleting user

    def write_current_cart(self):                                                   #METHOD OVERRIDING
        e=open('current_cart.txt','w')
        for o in user.current_cart.items():
            o=list(o)
            e.write(f'{o}\n')
        e.close()                

home_page()

