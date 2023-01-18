import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "rps@123", database = "kpmg")

mycursor = mydb.cursor()

def insert():
    pid = int(input("Product ID : "))
    pname = input("Product Name : ")
    pprice = int(input("Product Price : "))
    pdes = input("Product Description : ")
    pcat = input ("Product Category : ")
    mycursor.execute(f"INSERT INTO  products_info VALUES({pid},'{pname}',{pprice},'{pdes}','{pcat}')")
    mydb.commit()
    print("Data has been inserted successfully")

def update():
    pid = int(input("Enter product Id for updating price : "))
    pPrice = int(input("Enter updated Price : "))
    mycursor.execute(f"UPDATE products_info set productPrice = {pPrice}  where productId = {pid}" )
    mydb.commit()

def delete():
    pid = int(input("Enter product Id for deleting data : "))
    mycursor.execute(f"DELETE FROM products_info where productId = {pid}" )
    mydb.commit()

def display():
    pid = int(input("Enter product Id to display data : "))
    mycursor.execute(f"SELECT * FROM  products_info where productId = {pid}" )
    result = mycursor.fetchone()
    print(result)

def displayall():
    mycursor.execute("select * from products_info")
    data = mycursor.fetchall()
    for row in data:
        print("ProductID : ",row[0])
        print("Product Name : ",row[1])
        print("Product Price : ",row[2])
        print("Product Description : ",row[3])
        print("Product Category : ",row[4])

print("Please select a number: \n 1. Add a product \n 2. Update a product \n 3. Delete a product by Id \n 4. Get ProductById \n 5. Get All Products ")
option = int(input("Enter your option number : ")) 
if option == 1:
    insert()

elif option == 2:
    update()

elif option == 3:
    delete()

elif option == 4:
    display()
        
elif option == 5:
    displayall()
