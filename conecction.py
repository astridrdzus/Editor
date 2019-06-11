import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tkinter import *

def table_creation():
  mydb = mysql.connector.connect(
    host="localhost",
    user="rooty@localhost",
    passwd="root",
    database = "bancoImagenes"
  )

  mycursor = mydb.cursor()
  #Creates database
  #mycursor.execute("CREATE DATABASE bancoImagenes")
  #mycursor.execute("CREATE TABLE ChichenImgs ( img_name VARCHAR(130) PRIMARY KEY, photo LONGBLOB , tags_file BLOB , tags VARCHAR(130))")

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(img_name,photo, tags_txt, tags):
    print("Inserting BLOB into ChichenImgs")

    try:
        connection = mysql.connector.connect(host='localhost',
                             database='bancoImagenes',
                             user='rooty@localhost',
                             password='root')

        cursor = connection.cursor(prepared=True)

        sql_insert_blob_query = "INSERT INTO ChichenImgs (img_name, photo, tags_file, tags) VALUES (%s,%s,%s,%s)"
        picture = convertToBinaryData(photo)
        tags_file= convertToBinaryData(tags_txt)
        # Convert data into tuple format
        insert_blob_tuple = (img_name, picture, tags_file,tags)
        result  = cursor.execute(sql_insert_blob_query, insert_blob_tuple) #INSERT
        connection.commit()
        print ("Image and file inserted successfully as a BLOB into python_employee table", result)
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def searchImg(tag, frame2):
    print('searching')
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='bancoImagenes',
                             user='rooty@localhost',
                             password='root')

        cursor = connection.cursor(prepared=True)

        tag = tag.get()
        sql_search_query = "SELECT img_name FROM ChichenImgs WHERE tags = '" + tag +"'"
        cursor.execute(sql_search_query)
        result= cursor.fetchall()
        results = []
        total = cursor.rowcount
        print("Número total de imágenes:  ", total)
        for i in range (total):
            imgName= result[i][0].decode()
            results.append(imgName)

        print(results)
        #frame2.geometry("100x100+500+100")
        listbox = Listbox(frame2)
        listbox.grid(row=3, column=2)

        for x in results:
            listbox.insert(END,x)



    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed search into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#searchImg('mujer')