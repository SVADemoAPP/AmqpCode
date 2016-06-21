"""This is an example of how to get token
@author:  renyu@huawei.com
@date: 2015-03-10
@version: v0.1
"""
import commands
import sys


def get_token(ip, app_name, pwd):
    """
    curl --insecure -X POST -H "Content-Type: application/json" -i
    -d '{"auth": {"identity":{"methods":["password"],"password":{"user":{"domain":"Api","name":"X","password":"X"}}}}}'
    https://10.177.192.239:9001/v3/auth/tokens
    """

    cmd = 'curl --insecure -X POST -H "Content-Type: application/json" -i '\
        + '-d \'{"auth": {"identity":{"methods":["password"],"password":{"user":{"domain":"Api","name":"'\
        + app_name + '","password":"' + pwd + '"}}}}}\' '\
        + 'https://' + ip + ':9001/v3/auth/tokens'

    status, output = commands.getstatusoutput(cmd)

    if status != 0:
        print status, output
        return None

    target_string = 'X-Subject-Token: '
    for line in output.split('\n'):
        if line[0:len(target_string)] == target_string:
            return line.split(' ')[1]

    print status, output
    return None


if __name__ == '__main__':
    if 4 == len(sys.argv):

        _ip = sys.argv[1]
        _app_name = sys.argv[2]
        _pwd = sys.argv[3]

        _token = get_token(_ip, _app_name, _pwd)
        if _token is not None:
            print 'get token success, token:', _token
        else:
            print 'get token failed'
    else:
        print 'Usage: get_token.py ip app_name pwd'
