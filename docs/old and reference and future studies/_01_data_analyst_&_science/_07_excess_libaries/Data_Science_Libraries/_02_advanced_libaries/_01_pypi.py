#this to install and understand what is packages and libraies

#pypi->python package index
#pip list->show list of installed pip


#pip install requests ->latest version will be installed
#pip install requests==2.9.0 ->version mentioned will be installed
#pip install requests==2.9.* ->version is 2.10.0 but it will install latest version of 2.9
#pip install requests~=2.9.0 ->same like above
#pip install requests==2.* ->latest version
import requests
res=requests.get("http://www.eduspheresolutions.com")
print(res)#response 200 means success

#in env search pyvenv.cfg
#it will have version and path details of the env

#in lib->site-package
#this have all the installed packages

#pip install pipenv ->combine pip and env(can install all packages and can run anywhere)

#then we can delete venv folder and can use
#pipenv install ___


#when copying this project to another pc
#have to give
#pipenv install ->this will install all the package in pipfile

#pipenv graph ->displays all the details of packages installed

#pipenv update --outdated ->this will install latest version of the packages we already have

#pipenv update pandas ->this will only update pandas

'''
pip install pipenv
pipenv install(will backup)
pipenv install (numpy,etc)
pipenv update (numpy,etc)
'''


'''publish our own packages'''

#have to install some things

# pip install setuptools wheel twine
#make a new director (project)
#then create folders data, test and your project name folder
#then create py files __init.py__,your files as many as your program need

#then in root of director
#create setup.py
#add code inside setup.py change the name according to your projects
#then create README.md
#can type anything that have to show in readme
#then create LICENSE
#can get content form choosealicense.com
# paste the content in the file

#then go to setup.py and add pathlib
#then check setup.py

# then go to the path of the project
# then given this command
# python setup.py sdist bdist_wheel
#this will create build distribution and source distribution

#upload this project

#create account in pypi.org
#in terminal
#twine upload dist/*

#enter api token then it will add in global package



import prime as p
p.prime()
