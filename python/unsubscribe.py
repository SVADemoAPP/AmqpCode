"""This is an example of unsubscribe
@author:  renyu@huawei.com
@date: 2015-03-10
@version: v0.1
"""
import commands
import sys


def unsubscribe(ip, app_name, token, anonymous):
    """
    curl --insecure -X DELETE -H "Content-Type: application/json" -H "X-Auth-Token: 1b9373655f3142f58b56bb630b2695f9"
    https://10.177.192.239:9001/enabler/catalog/locationstream[anonymous]unreg/json/v1.0 -d '{"APPID":"app1"}'
    """
    type = 'anonymous' if anonymous else ''
    cmd = 'curl --insecure -X DELETE -H "Content-Type: application/json" '\
        + '-H "X-Auth-Token: ' + token + '" '\
        + 'https://' + ip + ':9001/enabler/catalog/locationstream' + type + 'unreg/json/v1.0 -d \'{"APPID":"' + app_name + '"}\''

    status, output = commands.getstatusoutput(cmd)

    if status != 0:
        print status, output
        return False

    return True


if __name__ == '__main__':
    if 4 == len(sys.argv) or ( 5 == len(sys.argv) and sys.argv[4] == 'a'):

        _ip = sys.argv[1]
        _app_name = sys.argv[2]
        _token = sys.argv[3]
        _anonymous = ( 5 == len(sys.argv) )

        result = unsubscribe(_ip, _app_name, _token, _anonymous)
        if result is True:
            print 'unsubscribe success'
        else:
            print 'subscribe failed'
    else:
        print 'Usage: unsubscribe.py ip app_name token [a]'
