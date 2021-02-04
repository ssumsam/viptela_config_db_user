import pexpect
import sys
from os import environ
from pprint import pprint


_VMANAGE_PROMPT = '#'


def main():
    output = []
    vmanage_list = set(sys.argv[1:])
    if not vmanage_list:
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

    for host in vmanage_list:
        child = pexpect.spawn('ssh {}@{}'.format(vmanage_user, host))
        try:
            child.expect(['assword'])
        except (pexpect.EOF, pexpect.TIMEOUT):
            output.append('Unable to connect to {}'.format(host))
            child.close()
            continue

        child.sendline(vmanage_password)
        child.expect([_VMANAGE_PROMPT, 'assword'])
        if not child.after == _VMANAGE_PROMPT:
            output.append('Unable to log on to {} - please check credentials'.format(host))
            child.close()
            continue
        # VMANAGE_PROMPT has been found.
        child.sendline('request nms configuration-db update-admin-user')
        child.expect('name:')
        child.sendline(old_db_user)
        child.expect('assword:')
        child.sendline(old_db_password)
        child.expect('name:')
        child.sendline(new_db_user)
        child.expect('assword:')
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
