# Pour faire marcher ce projet :

## Créer la base de donnée "library" et sa table "book" dans une base de données mySql:

CREATE DATABASE library;

USE library

CREATE TABLE book (
id INT AUTO_INCREMENT PRIMARY KEY,  
 title VARCHAR(255) NOT NULL,  
 author VARCHAR(255) NOT NULL,  
 genre VARCHAR(100),  
 published_date DATE,  
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
 updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

## Créer un utilisateur myuser avec le mot de passe mypassword:

CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';

## Donner les droits à notre utilisateur sur library:

GRANT SELECT, INSERT, UPDATE, DELETE ON library.\* TO 'myuser'@'localhost';

## Installer les dépendances suivantes sur le projet:

    pip install PyQt5
    pip install mysql-connector-python

## Installer PlanUML sur vscode

Pour voir le diagramme de classe aller sur classDiag.wsd et faire Alt + D

## Lancer le projet

python main.py
