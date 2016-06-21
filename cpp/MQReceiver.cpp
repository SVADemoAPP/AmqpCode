/*******************************************
This is an example of receive AMQP message
author:  renyu@huawei.com
date: 2015-03-10
version: v0.1
*******************************************/

#include <stdlib.h>
#include <iostream>
#include <string>
#include <qpid/messaging/Connection.h>
#include <qpid/messaging/Message.h>
#include <qpid/messaging/Receiver.h>
#include <qpid/messaging/Sender.h>
#include <qpid/messaging/Session.h>

using namespace qpid::messaging;

int main(int argc, char** argv)
{
    if ( argc != 5 )
    {
        std::cout << "Usage: MQReceiver app_name ip port queue_id" << std::endl;
        return 0;
    }
    
    std::string app_name = argv[1];
    std::string ip       = argv[2];
    std::string port     = argv[3];
    std::string queue_id = argv[4];    
    
    std::string address      = queue_id;    
    std::string broker       = app_name + "/xxxx@" + ip + ":" + port;    
    
    try {
        setenv("QPID_SSL_CERT_DB", "cert_db", 1);

        Connection connection(broker);

        connection.setOption("sasl-mechanism", "PLAIN");
        connection.setOption("username", "msp_mq_access");
        connection.setOption("password", "xxxx");

        connection.setOption("ssl-cert-name", "msp");
        connection.setOption("transport", "ssl");

        connection.open();
        Session session = connection.createSession();
        
        Receiver receiver = session.createReceiver(address);
        receiver.setCapacity(1024);
        
        while(true)
        {
            Message message = receiver.fetch();            
            std::cout << message.getContent() << std::endl;            
            session.acknowledge();
        }
        
    } catch(const std::exception& error) {
        std::cerr << error.what() << std::endl;
        return 1;   
    }
}
