
def view_all(cursor):
    cursor.execute("select *from users")
    k=cursor.fetchall()
    print("viewing")
    for x in k:
        print(x)

def admin():
    pass

def ok():
    pass