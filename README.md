# Risc Valor App
This is a Django app that creates a form for tracking intermediaries, clients, tariffs, and orders for Risc Valor, a valuation company. The form allows users to input and store this information in a PostgreSQL database. The main objective of this project is to provide an efficient and organized way for Risc Valor to keep track of their business operations.

## Getting Started
To use this app, you will need to have a running Django project and a PostgreSQL database set up. This are the commands you should use in Ubuntu Linux.

	- sudo bash script_install_postgresql.sh
	- sudo su postgres
	- createuser admin
	- createdb expedientes with owner admin
	- sudo python manage.py makemigrations
	- sudo python manage.py migrate
	- sudo python manage.py runserver 0.0.0.0:80

Use the form in your templates to input and view data.
## Prerequisites
	- Python
	- Django
	- PostgreSQL

