import sys
import time
import pexpect
from os import environ


_VMANAGE_PROMPT = '#'
_NAME_COLON_STRING = 'name:'
_PASSWORD_COLON_STRING = 'assword:'


def main():
    vmanage_list = set(sys.argv[1:])
    if not vmanage_list:
        print('ERROR - No input devices!!!')
        return
    try:
        vmanage_user = environ['VMANAGE_USER']
        vmanage_password = environ['VMANAGE_PASSWORD']
        old_db_user = environ['OLD_DB_USER']
        new_db_user = environ['NEW_DB_USER']
        old_db_password = environ['OLD_DB_PASSWORD']
        new_db_password = environ['NEW_DB_PASSWORD']
    except KeyError:
        print('Missing one or more mandatory environment variables')
        return 

    output_dict = {}

    for host in vmanage_list:
        child = pexpect.spawn('ssh {}@{}'.format(vmanage_user, host))
        try:
            child.expect([_PASSWORD_COLON_STRING, _VMANAGE_PROMPT])
        except (pexpect.EOF, pexpect.TIMEOUT):
            output_dict[host] = 'Unable to connect to {}'.format(host)
            child.close()
            continue
	if child.after == _PASSWORD_COLON_STRING:
            child.sendline(vmanage_password)
            child.expect([_PASSWORD_COLON_STRING, _VMANAGE_PROMPT])
            if not child.after == _VMANAGE_PROMPT:
                output_dict[host] = 'Unable to log on {} - please check credentials'.format(host)
                child.close()
                continue
        # VMANAGE_PROMPT has been found.
        child.sendline('request nms configuration-db update-admin-user')
        child.expect([_NAME_COLON_STRING, _VMANAGE_PROMPT])
        if child.after == _VMANAGE_PROMPT:
            output_dict[host] = 'The command "request nms configuration-db update-admin-user" is not supported' 
            child.close()
            continue
        child.sendline(old_db_user)
        child.expect(_PASSWORD_COLON_STRING)
        child.sendline(old_db_password)
        child.expect(_NAME_COLON_STRING)
        child.sendline(new_db_user)
        child.expect(_PASSWORD_COLON_STRING)
        child.sendline(new_db_password)
        time.sleep(5)
        child.expect(_VMANAGE_PROMPT)
        if child.after == _VMANAGE_PROMPT:
            output_dict[host] = child.before 
            child.close()
            continue

    for host, host_output in output_dict.items():
        print('*** {} ***'.format(host))
        for line in host_output.splitlines():
            print(line)
    return

if __name__ == "__main__":
    main()
