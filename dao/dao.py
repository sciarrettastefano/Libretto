import mysql.connector

from dao.dbConnect import DBConnect
from voto.voto import Voto

class LibrettoDAO:
    """def __init__(self):
        self.dbConnect= DBConnect()"""
    # E' classe stateless, ne usimao solo i metodi, che non ricevono
    # parametro il "self"
    # Possiamo chiamare direttamente i suoi metodi come fossero class methods
    # Lo facciamo perchè così è molto più efficiente se facciamo molte query

    @staticmethod
    def getAllVoti():
        """cnx= mysql.connector.connect(...)"""
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True) # Così ci restituisce i dati sottoforma di dizionario

        query = """select * from voti"""
        cursor.execute(query) # Converte automaticamente i tipi di mysql in tipi di python corrispondenti

        results = []
        for row in cursor:
            """materia = row['materia'] #str
            punteggio = row['punteggio'] #int 
            lode = row['lode'] #str
            data = row['data'] #datetime
            v =  Voto(materia, punteggio, data, lode)
            results.append(v)"""
            if row['lode'] == "False":
                results.append(Voto(row['materia'], row['punteggio'], row['data'].date(), False))
            else:
                results.append(Voto(row['materia'], row['punteggio'], row['data'].date(), True))

        cnx.close()

        return results
        """Ciò scritto sopra è l'uso std di un metodo del dao e dell'interfaccia al database.
        Quelo che cambia è la query solo, la struttura resta uguale."""

    @staticmethod
    def addVoto(voto: Voto):
        """cnx= mysql.connector.connect(...)"""
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor() # andrebbero gestiti gli errori con un try-catch

        query = """insert into
                 voti (materia, punteggio, data, lode)
                 values (%s, %s, %s, %s)"""

        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit()
        cnx.close()
        return

    @staticmethod
    def hasVoto(voto: Voto):
        """cnx= mysql.connector.connect(...)"""
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()

        query = """select * from voti v where v.materia = %s """

        cursor.execute(query, (voto.materia, ))
        res = cursor.fetchall() # perchè sennò ci dà errore per non aver usato tutti i risultati
        cnx.close()
        return len(res) > 0 # Dà indicazione se c'è il voto nel db o meno


if __name__ == '__main__':
    mydao = LibrettoDAO() # Creo istanza dao
    mydao.getAllVoti() # Uso il dao
