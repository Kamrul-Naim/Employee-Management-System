import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host='localhost',user='root',password='')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong')
        return
    
    mycursor.execute('CREATE DATABASE IF NOT EXISTS ems')
    mycursor.execute('USE ems')
    # mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(30),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(20),Salary VARCHAR(15))')


def insert(id,name,phone,role,gender,salary):
    mycursor.execute('insert into data values(%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()


def id_exists(id):
    mycursor.execute('select count(*) from data where id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('Select * from data')
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('update data set name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(id):
    mycursor.execute('delete from data where id=%s',id)
    conn.commit()

def search(option,value):
    mycursor.execute(f'select * from data where {option}=%s',value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('truncate table data')
    conn.commit()

connect_database()