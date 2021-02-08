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


## SET ENV VARIABLES
```
export VMANAGE_USER='*******'
export VMANAGE_PASSWORD='*******'
export OLD_DB_USER='*********'
export NEW_DB_USER='********'
export OLD_DB_PASSWORD='********'
export NEW_DB_PASSWORD='*********'
```

## HOW TO USE

pip install -r requirements.txt<br>
python update_db_user.py vmanage_1 vmanage_2 vmanage_3

```
$ python update_db_user.py testvmanage01
*** testvmanage01 ***
Successfully updated configuration database admin user
Successfully restarted NMS application server
```
