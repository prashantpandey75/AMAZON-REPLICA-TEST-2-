import json
class Amazon():

    def registration(self):
        Type = input('Enter Type of Registration (Admin/Member) : ')
        if Type == 'Admin' or Type == 'admin' or Type == 'ADMIN':
            admin = Admin()
            return admin.register()

        elif Type == 'Member' or Type == 'member' or Type == 'MEMBER':
            member = Member()
            return member.register()

        else:
            print('NOT VALID INPUT')
            return 0;


    def Login(self):

        user_id = input('Enter user ID : ')
        password = input('Enter password : ')

        Type = input('Login As (Admin/Member): ')
        if Type == 'Admin' or Type == 'admin' or Type == 'ADMIN':
            admin = Admin()
            return admin.verification(user_id,password)

        elif Type == 'Member' or Type == 'member' or Type == 'MEMBER':
            member = Member()
            return member.verification(user_id,password)

        else:
            print('NOT VALID INPUT')
            return 0


class Admin():

    def __init__(self):
        self.p = Product()
        self.o = Order()

    def verification(self,user_id,password):
        login_list = []
        flag = 0
        with open('admin_log.json', 'r') as Lfile:
            for jsonobj in Lfile:
                logindict = json.loads(jsonobj)
                login_list.append(logindict)
        for i in login_list:
            if i['id'] == user_id and i['password'] == password:
                print('Login Sucessfull')
                flag = 1
                break
        if flag == 1:
            return self.show_options(user_id)
        else:
            print('Credentials not correct')
            return 0

    def register(self):
        print('No new admin registration allowed')
        return 0

    def show_options(self,user_id):
        while True:
            print('1 : Create Product')
            print('2 : View Product List')
            print('3 : View Order details')
            print('4 : Update Product')
            print('5 : Delete')
            print('6 : Logout')
            choice = int(input("What do you want to do? "))
            if choice == 1:
                print('****CREATE PRODUCT****')
                self.p.createProduct(user_id)

            elif choice == 2:
                print('****VIEW PRODUCT LIST****')
                plist=[]
                with open('product.json','r') as Pfile:
                    for i in Pfile:
                        pdetail = json.loads(i)
                        if pdetail['creator_id'] == user_id:
                            plist.append(pdetail)
                if len(plist) > 0:
                    for i in plist:
                        print(i)
                else:
                    print("No Product Available")


            elif choice == 3:
                print('\n')
                print('****VIEW ORDER DETAILS****')
                self.o.details(-1)


            elif choice == 4:
                print('**** UPDATE PRODUCT ****')
                product_id = input('Enter Product ID : ')
                name = input('Enter name product : ')
                manufacturer_name = input('Enter Manufacturer Name : ')
                price = float(input('Enter price of product : '))
                discount = float(input('Enter discount : '))
                total_stock = int(input("Enter Total stock : "))
                dict = {'product_id': product_id, 'Name': name,
                 'manufacturer_name': manufacturer_name,
                 'price': price, 'discount': discount,
                 'total_stock': total_stock,
                 'creator_id': user_id}
                self.p.updateProduct(product_id,dict,0)

            elif choice == 5:
                print('**** DELETE PRODUCT****')
                product_id = input('Enter Product ID : ')
                plist = []
                with open('product.json', 'r') as Pfile:
                    for i in Pfile:
                        pdetail = json.loads(i)
                        if pdetail['product_id'] != product_id:
                            plist.append(pdetail)
                fp = open('product.json', 'w')
                for i in plist:
                    json.dump(i, fp)
                    fp.write('\n')
                fp.close()


            elif choice == 6:
                print("GoodBye!!")
                return 0
            else:
                print("Not a valid option")




class Member():

    def __init__(self):
        self.p = Product()
        self.o = Order()

    def details(self,user_id):
        list=[]
        with open('member_reg.json','r') as op:
            for i in op:
                dict = json.loads(i)
                list.append(dict)
        for i in list:
            if i['id'] == user_id:
                return i
        return {}

    def update(self,user_id,new_details,choice):
        ulist = []
        if choice == 1:
            file = 'member_log.json'
            key = 'password'
        else:
            file = 'member_reg.json'
            key = 'address'
        with open(file, 'r') as Ufile:
            for i in Ufile:
                Udetail = json.loads(i)
                if Udetail['id'] == user_id:
                    Udetail[key] = new_details
                ulist.append(Udetail)
        fp = open(file, 'w')
        for i in ulist:
            json.dump(i, fp)
            fp.write('\n')
        fp.close()

    def verification(self,user_id,password):
        login_list = []
        flag = 0
        with open('member_log.json','r') as Lfile:
            for jsonobj in Lfile:
                logindict = json.loads(jsonobj)
                login_list.append(logindict)
        for i in login_list:
            if i['id'] == user_id and i['password'] == password:
                print('Login Sucessfull')
                flag = 1
                break
        if flag == 1:
            self.show_options(user_id)
        else:
            print('Credentials not correct')
            return 0


    def register(self):
        user_id = input('Enter User ID : ')
        password = input('Enter password : ')
        login_list = []
        flag = 0
        with open('member_log.json', 'r') as Lfile:
            for jsonobj in Lfile:
                logindict = json.loads(jsonobj)
                login_list.append(logindict)
        for i in login_list:
            if i['id'] == user_id :
                print('Same UserId Exist, try something different')
                flag = 1
                break
        if flag == 1:
            self.register()
        else :
            name = input('Enter name : ')
            email = input('Enter E-mail address : ')
            address = input('Enter Full Address : ')
            detail = {'id':user_id,'name':name,'email':email,'address':address}
            login_details = {'id':user_id,'password':password}
            with open('member_reg.json','a') as Dfile:
                json.dump(detail,Dfile)
                Dfile.write('\n')
            with open('member_log.json','a') as Lfile:
                json.dump(login_details,Lfile)
                Lfile.write('\n')
            print('Registration Sucessfull')
            return 0

    def show_options(self,user_id):
        while True:
            print('1 : Create New Order')
            print('2 : View Order history')
            print('3 : Update Profile')
            print('4 : Logout')
            choice = int(input("What do you want to do? "))
            if choice == 1:
                print('**** CREATE NEW ORDERS ****')
                self.p.display()
                product_id = input('Enter product ID : ')
                quantity = int(input('Enter quantity : '))
                member_details = self.details(user_id)
                if member_details == {}:
                    print('CANNOT FIND USER DETAILS')
                else:
                    product_details = self.p.details(product_id)
                    if product_details == {}:
                        print("CANNOT FIND PRODUCT")
                    else:
                        self.o.createOrders(member_details,product_details,user_id,quantity)
                        self.p.updateProduct(product_id,[],quantity)

            elif choice == 2:
                print('**** VIEW ORDER HISTORY ****')
                self.o.details(user_id)

            elif choice == 3:
                print('**** UPDATE PROFILE ****')
                print('1 : Update Password')
                print('2 : Update Address')
                choice = int(input("What do you want to update?"))
                if choice == 1 or choice == 2:
                    new_details = input("Enter your updated Details")
                    self.update(user_id,new_details, choice)
                else:
                    print("WRONG INPUT")

            elif choice == 4:
                print("GoodBye!!")
                return 0
            else:
                print("Not a Valid Option")




class Product():
    def details(self,product_id):
        list=[]
        with open('product.json','r') as op:
            for i in op:
                dict = json.loads(i)
                list.append(dict)
        for i in list:
            if i['product_id'] == product_id:
                return i
        return {}

    def display(self):
        list = []
        with open('product.json', 'r') as op:
            for i in op:
                dict = json.loads(i)
                if dict['total_stock'] > 0:
                    list.append(dict)
        c = 0
        for i in list:
            c+=1
            print("****Product ",c,"****")
            print("ProductId : ", i['product_id'])
            print("Name : ", i['Name'])
            print("Price : ", i['price'])
            print("Discount : ", i['discount'])
            print("Stock Available : ", i['total_stock'])


    def createProduct(self,adminid):
        name = input('Enter name product : ')
        manufacturer_name = input('Enter Manufacturer Name : ')
        price = float(input('Enter price of product : '))
        discount = float(input('Enter discount : '))
        total_stock = int(input("Enter Total stock : "))
        product_id = name[:3] + str(hash(name + manufacturer_name) % 100000)
        details = {'product_id': product_id, 'Name': name, 'manufacturer_name': manufacturer_name, 'price': price,
                   'discount': discount, 'total_stock': total_stock, 'creator_id': adminid}
        with open('product.json', 'a') as Pfile:
            json.dump(details, Pfile)
            Pfile.write('\n')

    def updateProduct(self,product_id,productDetails,quantity):
        plist = []
        if productDetails == []:
            productDetails = self.details(product_id)
            productDetails['total_stock'] = productDetails['total_stock']-quantity
        with open('product.json', 'r') as Pfile:
            for i in Pfile:
                pdetail = json.loads(i)
                if pdetail['product_id'] == product_id:
                    pdetail = {'product_id': product_id, 'Name': productDetails['Name'], 'manufacturer_name': productDetails['manufacturer_name'],
                               'price': productDetails['price'], 'discount': productDetails['discount'], 'total_stock': productDetails['total_stock'],
                               'creator_id': productDetails['creator_id']}
                plist.append(pdetail)
        fp = open('product.json', 'w')
        for i in plist:
            json.dump(i, fp)
            fp.write('\n')
        fp.close()




class Order():
    def details(self,userid):
        Olist = []
        with open('orders.json', 'r') as Ofile:
            for i in Ofile:
                Odetail = json.loads(i)
                if userid == -1 or Odetail['user_id'] == userid:
                    Olist.append(Odetail)
        if len(Olist) > 0 :
            c=0
            total_cost = 0
            for i in Olist:
                c+=1
                print("*****Order:",c,"*****")
                print("Member Name : ",i['user_info']['name'])
                print("Member Address : ",i['user_info']['address'])
                print("Member Email : ", i['user_info']['email'])
                print("ProductId : ", i['product_info']['product_id'])
                print("Name : ", i['product_info']['Name'])
                print("Price : ", i['product_info']['price'])
                print("Discount : ", i['product_info']['discount'])
                print("Quantity : ", i['quantity'])
                price = i['quantity']*i['product_info']['price']*(1-i['product_info']['discount'])
                total_cost += price
                print("TotalPrice : ", (price))
            print("Total Order Costs : ",total_cost)
        else:
            print(" No Orders available ")

    def createOrders(self,member_details,product_details,user_id,quantity):
        detail = {'user_info': member_details, 'quantity': quantity,
                  'product_info': product_details, 'user_id': user_id}
        with open('orders.json', 'a') as Pfile:
            json.dump(detail, Pfile)
            Pfile.write('\n')


A=Amazon()
while True:
    print('1 : LOGIN ')
    print('2 : REGISTRATION')
    print('3 : EXIT')
    l=int(input('What to do: (1/2/3) '))
    if l == 1:
        exit = A.Login()
    elif l == 2:
        exit = A.registration()
    elif l == 3:
        print("Goodbye :-) ")
        break
    else:
        print('Wrong Input')

