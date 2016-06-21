#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import sys
from qpid.messaging import *

if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(-1)
    print 'app name {}, broke ip {}, broker port {}, queue id {}'.format(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    broker = "{}/xxxx@{}:{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    address = "{}".format(sys.argv[4])
    conn_options = {
                    'transport'               : 'ssl',
                    'ssl_keyfile'             : "ssl_cert_file/MSP.Key.pem",
                    'ssl_certfile'            : "ssl_cert_file/MSP.pem.cer",
                    'ssl_trustfile'           : "ssl_cert_file/Wireless Root CA.pem.cer",
                    'ssl_skip_hostname_check' : True,
                    }
    connection = Connection(broker, **conn_options)

    try:
        connection.open()
        session = connection.session()
        receiver = session.receiver(address)
        print "session create success"
        while True:
            message = receiver.fetch()
            if len(sys.argv) == 6:
                if message.content.find(sys.argv[5]):
                    print "%r" % message.content
            else:
                print "%r" % message.content
            session.acknowledge()

    except MessagingError, m:
        print "MessagingError", m
    connection.close()