# run this query in mysql work bench to activate password validity
import mysql.connector as mysql
from _02_create import admin_user,customer
from _03_admin_login import view_all,admin

con=None
def connect():
    try:
        global con
        con = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="ok_da",  # Replace with the actual database name
            port=3307,  # Specify the correct port here
            auth_plugin='mysql_native_password'  # Explicitly set the authentication plugin
        )
        global cursor
        cursor=con.cursor()
    except mysql.Error as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    connect()
    admin_user(cursor)
    customer(cursor)
    while True:
        op = input("1->admin login\n2->user login\n3->user sign in\n0->exit\nenter the option: ")

        if op.lower() == '1' or op.lower() == "admin login":
            try:
                # cursor.execute("select *from admin_users")
                # k = cursor.fetchall()
                # print(k)
                ph = input("enter your phone: ")
                pas = input("enter password: ")
                cursor.execute("select *from admin_users where phone=%s and password=%s;", (ph, pas,))
                if cursor.rowcount == 0:
                    print("No user found with the provided phone and password")
                else:
                    print(" in admin")
                    admin()
                    res = cursor.fetchall()
                    print(res)
                    print("admin login success")
                    view_all(con)

            except Exception as e:
                print("Fetching error in admin_users:", e)
        elif op.lower() == 'exit'or op=='0':
            con.close()  # Close the connection before exiting
            break





#created for module topic in _07_libary
def check():
    print("checked")


    '''
    1) admin login
        1) view all details
        2) change customer phone by using existing phone number
        3) view all transcration(user id, phone, previous balance, withdraw, deposit, current balance)(insert in trans, update in user detail)
        4) view particular customer transcration
    2) user sign in
    3) user log in
        1) balance
        2) withdraw
        3) deposit
        4) transction(cphone,c balance, withdraw,deposit, ch bala)
    '''