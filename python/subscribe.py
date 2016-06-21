"""This is an example of subscribe
@author:  renyu@huawei.com
@date: 2015-03-10
@version: v0.1
"""
import commands
import sys


def subscribe(ip, app_name, token, anonymous):
    """
    curl --insecure -X POST -H "Content-Type: application/json" -H "X-Auth-Token: 1b9373655f3142f58b56bb630b2695f9"
    https://10.177.192.239:9001/enabler/catalog/locationstream[anonymous]reg/json/v1.0 -d '{"APPID":"app1"}'
    """
    type = 'anonymous' if anonymous else ''
    cmd = 'curl --insecure -X POST -H "Content-Type: application/json" '\
        + '-H "X-Auth-Token: ' + token + '" '\
        + 'https://' + ip + ':9001/enabler/catalog/locationstream' + type + 'reg/json/v1.0 -d \'{"APPID":"' + app_name + '"}\''

    status, output = commands.getstatusoutput(cmd)

    if status != 0:
        print status, output
        return None

    target_string = '"Subscribe Information":'
    for line in output.split('\n'):        
        if -1 != line.find(target_string):
            try:
                queue_id = eval(line)['Subscribe Information'][0]['QUEUE_ID']
                return queue_id
            except Exception, e:
                print status, output
                print e
                return None
    
    print status, output
    return None


if __name__ == '__main__':
    if 4 == len(sys.argv) or ( 5 == len(sys.argv) and sys.argv[4] == 'a'):

        _ip = sys.argv[1]
        _app_name = sys.argv[2]
        _token = sys.argv[3]
        _anonymous = ( 5 == len(sys.argv) )

        _queue_id = subscribe(_ip, _app_name, _token, _anonymous)
        if _queue_id is not None:
            print 'subscribe success, queue_id:', _queue_id
        else:
            print 'subscribe failed'
    else:
        print 'Usage: subscribe.py ip app_name token [a]'
