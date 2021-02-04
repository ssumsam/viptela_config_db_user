## INTRODUCTION
This is a Python script to update the config-db user and password for one or more Viptela vManage devices running version 20.1.2 or later.

### CLI-equivalent command
request nms configuration-db update-admin-user 

>Enter current user name:*****</br>
>Enter current user password:******</br>
>Enter new user name:*****</br>
>Enter new user password:******</br>


## ASSUMPTIONS
The script assumes the following:</br>
1. All input vManages have the same user and password for SSH access.</br>
2. All input vManages are to use the same configuration-db admin user and password.</br>


## REQUIREMENTS
pip install pexpect</br>
pip install os</br>
pip install sys</br>
pip install pprint</br>

## SET ENV VARIABLES
export VMANAGE_USER='*******'</br>
export VMANAGE_PASSWORD='*******'</br>
export OLD_DB_USER='*********'</br>
export NEW_DB_USER='********'</br>
export OLD_DB_PASSWORD='********'</br>
export NEW_DB_PASSWORD='*********'</br>

## HOW TO USE
From Python shell</br>
python update_db_user.py <vmanage1> <vmanage2> <vmanage3>
