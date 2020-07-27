# Whetu Ejercicio- back end
_Desarrollado en python utilizando Flask como microframework y MongoDB_
 
## Instalación 🔧 

 _🔧 Instalar [Python 3.8.2](https://www.python.org/downloads/)_ 
 * check instalación: python --version


_🔧 Instalar [MongoDB](https://www.mongodb.com/try/download/community)_

_🔧 Instalar las siguientes librerias desde la consola para poder trabajar con ambientes:_
```
pip3 install virtualenv
```
_🛠️ Instalar las librerias
pip3 install -r requirements.txt 

## Run services  🚀

_🚀 Run a la aplicación dentro de  agronome\services>_

```
export FLASK_APP = run.py
flask run

```

## API REST Documents 📖 
#  Usuario

## Signin Up user

	POST /user

### Body
```
{
    "name": string,
    "lastname": string,
    "password": string,
    "email": xxx@xxx.xxx,
}

```

# Login user

	GET /auth/login


### Success Response 
200 Ok
```
{
  "status": cod,
  "token": token_id,
}

```

# Obtain Users
    GET/user
   
### Header Autorización

    Authorization=bearer {token}

### Success Response 
200 Ok
```
{
  "status": cod,
  "message": {
        "name": string,
        "lastname": string,
        "password": string,
        "email": xxx@xxx.xxx,
        "is_admin": boolean
    }

}