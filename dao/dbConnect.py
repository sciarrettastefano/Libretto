import mysql

class DBConnect:

    @classmethod
    def getConnection(self): # metodo "FACTORY" --> costruisce oggetti e li restituiscce
        try:
            cnx = mysql.connector.connect(option_files='dao/connector.cnf')
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al database")
            print(err)
            return None
