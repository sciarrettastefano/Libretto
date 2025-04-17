import mysql.connector

class DBConnect:

    """@classmethod
    def getConnection(cls): # metodo "FACTORY" --> costruisce oggetti e li restituisce
        try:
            cnx = mysql.connector.connect(option_files='dao/connector.cnf')
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al database")
            print(err)
            return None"""

    def __init__(self):
        RuntimeError("Non creare una istanza di questa classe per favore!") # <---  per implementare il pattern come si deve questa
                                                                            #       classe non va istanziata
#pooling connection --> molto più efficiente che con connect come sopra
#                       molto più efficiente se facciamo molte query

    _myPool = None

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            # Creo una connessione e restituisco il metodo get_connection
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(pool_size=3,
                                                                          pool_name="myPool",
                                                                          option_files="dao/connector.cnf")
            except mysql.connector.Error as err:
                print("Something is wrong in dbconnect")
                print(err)
                return None
            return cls._myPool.get_connection()
        else:
            # Se il pool già esiste, restituisce direttamente la connessione
            return cls._myPool.get_connection()
