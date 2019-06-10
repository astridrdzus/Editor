import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(img_name, photo, tags_txt):
    print("Reading BLOB data from ChichenImgs")
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='bancoImagenes',
                             user='rooty@localhost',
                             password='root')

        cursor = connection.cursor(prepared=True)
        sql_fetch_blob_query = "SELECT * from ChichenImgs WHERE img_name = %s"
        cursor.execute(sql_fetch_blob_query, (img_name, ))

        record = cursor.fetchall()
        print("Record: ", record)
        for row in record:
            print("img_name = ", row[0],)
            image =  row[1]
            file = row[2]
            print("tags = ", row[3])
            print("Storing picture and txt_file on disk \n")
            write_file(image, photo)
            write_file(file, tags_txt)

    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to read BLOB data from MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

readBLOB("Chichen1", "/home/asteroid/Documentos/2_CANIETI/Editor/query_output/pir_chichen_1.jpg", "/home/asteroid/Documentos/2_CANIETI/Editor/query_output/pir_chichen_1.xml")
