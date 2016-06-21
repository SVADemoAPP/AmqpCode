/*******************************************
This is an example of subscribe
author:  renyu@huawei.com
date: 2015-03-10
version: v0.1
*******************************************/

#include<stdio.h>
#include<errno.h>
#include<string.h>
#include<string>
#include<iostream>

std::string subscribe(std::string ip, std::string app_name, std::string token, bool anonymous)
{
    FILE *fstream = NULL;
	char buff[1024];
	memset(buff, 0, sizeof(buff));
	
    //curl --insecure -X POST -H "Content-Type: application/json" -H "X-Auth-Token: 1b9373655f3142f58b56bb630b2695f9"
    //https://10.177.192.239:9001/enabler/catalog/locationstream[anonymous]reg/json/v1.0 -d '{"APPID":"app1"}'
    
    std::string type = anonymous ? "anonymous" : "";
    std::string cmd = "curl --insecure -X POST -H \"Content-Type: application/json\" -H \"X-Auth-Token: " + token + "\" "
                    + "https://" + ip + ":9001/enabler/catalog/locationstream" + type + "reg/json/v1.0 -d \'{\"APPID\":\"" + app_name + "\"}\'";

    if ( NULL == ( fstream = popen(cmd.c_str(),"r") ) )
	{
		fprintf(stderr,"execute command failed: %s",strerror(errno));
		return "";
	}
    
    const char *pattern = "\"QUEUE_ID\": \"";
    std::string queue_id = "";
	while( NULL != fgets(buff, sizeof(buff), fstream) )
	{
        const char *start;
        if ( NULL != (start = strstr(buff, pattern)) )
        {     
            start += strlen(pattern);
            const char *end = strstr(start, "\"");
            queue_id = std::string(start, end - start);
            pclose(fstream);
            return queue_id;
        }
	}
	
	pclose(fstream);
    std::cout << buff << std::endl;
	return queue_id;
}

int main(int argc, const char *argv[])
{
    if ( (4 == argc)
      || ((5 == argc) && ("a" == std::string(argv[4]))))
    {
        const char *ip = argv[1];
        const char *app_name = argv[2];
        const char *token = argv[3];
        bool anonymous = (5 == argc);
        
        std::string queue_id = subscribe(ip, app_name, token, anonymous);
        if ( "" == queue_id )
        {
            std::cout << std::endl << "subscribe failed" << std::endl;
        }
        else
        {
            std::cout << std::endl << "subscribe success, queue_id: " << queue_id << std::endl;
        }
    }
    else
    {
        std::cout << "Usage: subscribe ip app_name token [a]" << std::endl;
    }
    return 0;
}
