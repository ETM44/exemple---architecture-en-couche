from abc import ABC

import mysql.connector

class BaseRepository(ABC):
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=3306,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None

    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connexion à la base de données fermée")