Sur ubuntu : 

//Installer pyhton3
//Installer django
	
	sudo apt install python3-django
	
//Installer python env

	sudo apt install python3-venv
	
//créer l'environnement python et s'y connecter

	python3 -m venv env
	source env/bin/activate
	
//Installer django sur l'environnement virtuel
	
	pip install django
	
//créer le projet

	django-admin createproject <nom>
	
	cd <nom>
	
	python3 manage.py migrate
	
	python3 manage.py createsuperuser
	
	//password : ThisIsTheNewPasswordForASecureProjectAlphaBeta/!
	
	python3 manage.py runserver
	
	python3 manage.py startapp connect
	
