## INTRODUCTION
This is a Python script to update the config-db user and password for one or more Viptela vManage devices running version 20.1.2 or later.

### CLI-equivalent command
request nms configuration-db update-admin-user 

>Enter current user name:*****</br>
>Enter current user password:******
>Enter new user name:*****
>Enter new user password:******


## ASSUMPTIONS
The script assumes the following:
1. All input vManages have the same user and password for SSH access.
2. All input vManages are to use the same configuration-db admin user and password.


## REQUIREMENTS
pip install pexpect
pip install os
pip install sys
pip install pprint

## SET ENV VARIABLES
export VMANAGE_USER='*******'
export VMANAGE_PASSWORD='*******'
export OLD_DB_USER='*********'
export NEW_DB_USER='********'
export OLD_DB_PASSWORD='********'
export NEW_DB_PASSWORD='*********'

## HOW TO USE
From Python shell
python update_db_user.py <vmanage1> <vmanage2> <vmanage3>
