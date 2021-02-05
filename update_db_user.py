import sys
import pexpect
from os import environ
from pprint import pprint


_VMANAGE_PROMPT = '#'
_NAME_COLON_STRING = 'name:'
_PASSWORD_COLON_STRING = 'assword:'


def main():
    output = []
    vmanage_list = set(sys.argv[1:])
    if not vmanage_list:
        print('ERROR - No input devices!!!')
        return output
    try:
        vmanage_user = environ['VMANAGE_USER']
        vmanage_password = environ['VMANAGE_PASSWORD']
        old_db_user = environ['OLD_DB_USER']
        new_db_user = environ['NEW_DB_USER']
        old_db_password = environ['OLD_DB_PASSWORD']
        new_db_password = environ['NEW_DB_PASSWORD']
    except KeyError:
        output.append('Missing one or more mandatory environment variables')
        print(output)
        return output
    output = []

    for host in vmanage_list:
        child = pexpect.spawn('ssh {}@{}'.format(vmanage_user, host))
        try:
            child.expect([_PASSWORD_COLON_STRING])
        except (pexpect.EOF, pexpect.TIMEOUT):
            output.append('Unable to connect to {}'.format(host))
            child.close()
            continue
	# if 'assword' in child.after
        child.sendline(vmanage_password)
        child.expect([_VMANAGE_PROMPT, 'assword'])
        if not child.after == _VMANAGE_PROMPT:
            output.append('Unable to log on to {} - please check credentials'.format(host))
            child.close()
            continue
        # VMANAGE_PROMPT has been found.
        child.sendline('request nms configuration-db update-admin-user')
        child.expect(_NAME_COLON_STRING)
        child.sendline(old_db_user)
        child.expect(_PASSWORD_COLON_STRING)
        child.sendline(old_db_password)
        child.expect(_NAME_COLON_STRING)
        child.sendline(new_db_user)
        child.expect(_PASSWORD_COLON_STRING)
        child.sendline(new_db_password)
        child.expect(_VMANAGE_PROMPT)
        if child.after == _VMANAGE_PROMPT:
            output.append(child.before)
            child.close()
            continue
    print('^' * 10)
    pprint(output)
    print('^' * 10)
    return output

if __name__ == "__main__":
    main()
