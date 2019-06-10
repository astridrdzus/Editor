import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def table_creation():
  mydb = mysql.connector.connect(
    host="localhost",
    user="rooty@localhost",
    passwd="root",
    database = "bancoImagenes"
  )

  mycursor = mydb.cursor()

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


def searchImg(tag):
    print('searching')