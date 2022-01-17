# Ayomi Test technique

## Pour commencer
### Pré-requis :
Vous avez besoin de :
* Python3
* pip
* Git
* Django
* Bootstrap
* Docker Engine
* Docker Compose
* tout ce que le fichier .zip contient

### Installation :
1. Créer un dossier qui contiendra l'application.
2. Entrer dans le dossier grâce au terminal.
    ```
    ~$ cd chemin/vers/le_dossier
    ```
3. Créer un clone du dépôt ```ayomi_website_test``` suivant : 
[Liens vers le dépôt ayomi_website_test](https://github.com/micktymoon/ayomi_website_test.git)
    ```
    ~$ git clone https://github.com/micktymoon/ayomi_website_test.git
    ~$ cd ayomi_website_test/
    ```

4. Installer Docker Engine. https://docs.docker.com/engine/install/debian/
5. Installer Docker Compose version 1.29.2
   ```
   ~$ sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
   ~$ sudo chmod +x /usr/local/bin/docker-compose
   ```
6. Entrer dans le dossier ```ayomi_website_test```:
   ```
    ~$ cd ayomi_website_test/
   ```
7. Créer la base de donnée.
   ```
    ~$ sudo docker-compose up db
   ```
8. Lancer l'application.
   ```
    ~$ sudo docker-compose up
   ```
   
## Démarrage
Lancer l'application avec Docker Compose.
   ```
    ~$ sudo docker-compose up
   ```

## Fabriqué avec
* ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) - Pycharm - IDE Python.
* <img alt="Django" src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> - Framework open-source de développement web en Python.
* ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) - Framework de Front-end gratuit.
* <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/> - Plateforme de conteneurisation.
## Versions
<img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

Voici le lien vers la version stable : 
[Liens vers le dépôt ayomi_website_test.](https://github.com/micktymoon/ayomi_website_test.git)


## Auteurs

Céline PELLETIER alias @micktymoon

