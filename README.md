# Pour faire marcher ce projet :

## Créer la base de données "library" et sa table "book" dans une base de données mySql:

```SQL
CREATE DATABASE library;

USE library;

CREATE TABLE book (
id INT AUTO_INCREMENT PRIMARY KEY,
 title VARCHAR(255) NOT NULL,
 author VARCHAR(255) NOT NULL,
 genre VARCHAR(100),
 published_date DATE,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

Par sécurité, la base de données pourra porter un autre nom que "library".

## Créer un utilisateur myuser avec le mot de passe mypassword:

```SQL
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
```

Par sécurité, vous pouvez placer d'autres valeurs que "myuser", "localhost" et "mypassword".

## Donner les droits à notre utilisateur sur library:

```SQL
GRANT SELECT, INSERT, UPDATE, DELETE ON library.* TO 'myuser'@'localhost';
```

Faire attention à remplacer "library", "myuser" et "localhost" par les valeurs que vous avez choisie.

## Installer les dépendances suivantes sur le projet:

    pip install PyQt5
    pip install mysql-connector-python
    pip install python-dotenv

## Définir les variables d'environnement:

- Renommer le fichier ".env-sample" en ".env".
- Adapter les variables d'environnement dans ".env" à la configuration de votre base de données.

## Installer PlantUML sur vscode

Pour voir le diagramme de classe aller sur classDiag.wsd et faire Alt + D

## Lancer le projet

    python main.py
