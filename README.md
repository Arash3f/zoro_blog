# Zoro Blog 
>Note : This project is not over yet. 

Zorro Blog is a professional blog which developed by Django framework.
The Bootstrap framework is used in the frontend.
For this project, some free templates have been used, which parts of it have been customized and added.


- [Features](https://github.com/Arash3f/zoro_blog#features)
- [How to Deploy ?](https://github.com/Arash3f/zoro_blog#how-to-deploy)

## Features

- Portfolio Features : about me / skills / experiences / services / projects / papers
- Paper Features : Paper page / view counter  / comments / tag 
- Pages :  about me / services / project / paper / blog / portfolio / dashboard

## How to Deploy
**Clone project :**

- `git clone https://github.com/Arash3f/zoro_blog.git`

- `cd zoro_blog`


**Create environment**

- `python3 -m venv venv`

**Active environment**

- linux : `source venv/bin/activate`

- windows : `.\venv\Scripts\activate`

**Install libraries**

- `pip3 install -r requirements.txt`

**makemigrations/migrate**

- `python3 manage.py makemigrations`

- `python3 manage.py migrate`

**run project**

- `python manage.py runserver`

> **Note** :  The [python-decouple](https://github.com/henriquebastos/python-decouple "python-decouple") library is used for the environment variables section. 

 
