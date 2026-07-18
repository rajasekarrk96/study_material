def admin_user(cursor):
    try:
        cursor.execute("create table if not exists admin_users (auid int primary key auto_increment, name varchar(50) unique, password varchar(10) not null,email varchar(50) unique, phone varchar(10) unique)")
        print("success")
    except Exception as e:
        print("admin user table error\n0",e)


def customer(cursor):
    try:
        cursor.execute("create table if not exists users (cid int primary key auto_increment, cname varchar(50) unique, cpassword varchar(10) not null,cemail varchar(50) unique, cphone varchar(10) unique, balance int not null default 0)")
        print("success")
    except Exception as e:
        print("customer table error\n0",e)