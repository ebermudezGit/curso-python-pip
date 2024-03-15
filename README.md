# Game Proyect

Para correr el juego tienes que correr las instrucciones en la terminal

```sh
cd game
python main.py
```

# App Project
Para correr el proyecto por primera vez
```sh
git clone git@github.com:ebermudezGit/curso-python-pip.git
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requeriments.txt
```
En la carpeta app ejecutar el main.py
```sh
python3 main.py
```
las imagenes se crearan en ./app/imgs/


## Comisimientos usados
### Entornos Virtuales Python:

Verificar donde esta python y pip

- which python3

- which pip3

Si estas en linux o wsl (windows) instalar
```sh
sudo apt install -y python3-venv
```

Para crear un ambiente, entrar en cada carpeta.

```sh
python3 -m venv env
```

Activar el ambiente
```sh
source env/bin/activate
```

Salir del ambiente virtual
```sh
deactivate
```

Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
```sh
pip3 install matplotlib==3.5.0
```

Verificar las instalaciones
```sh
pip3 freeze | grep matplotlib
```
### Entornos Virtuales requirements.txt:

Crea el archivo requeriments.txt
```sh
pip3 freeze > requeriments.txt
```
Instalar usando el requeriments.txt
```sh
pip3 install -r requeriments.txt
```