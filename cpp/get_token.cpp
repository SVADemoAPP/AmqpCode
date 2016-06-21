/*******************************************
This is an example of how to get token
author:  renyu@huawei.com
date: 2015-03-10
version: v0.1
*******************************************/

#include<stdio.h>
#include<errno.h>
#include<string.h>
#include<string>
#include<iostream>

std::string get_token(std::string ip, std::string app_name, std::string pwd)
{
    FILE *fstream = NULL;
	char buff[1024];
	memset(buff, 0, sizeof(buff));
	
    //curl --insecure -X POST -H "Content-Type: application/json" -i
    //-d '{"auth": {"identity":{"methods":["password"],"password":{"user":{"domain":"Api","name":"X","password":"X"}}}}}'
    //https://10.177.192.239:9001/v3/auth/tokens
    
    std::string cmd = "curl --insecure -X POST -H \"Content-Type: application/json\" -i -d '{\"auth\": {\"identity\":{\"methods\":[\"password\"],\"password\":{\"user\":{\"domain\":\"Api\",\"name\":\""
                    + app_name + "\",\"password\":\"" + pwd + "\"}}}}}\' "
                    + "https://" + ip + ":9001/v3/auth/tokens";
    if ( NULL == ( fstream = popen(cmd.c_str(),"r") ) )
	{
		fprintf(stderr,"execute command failed: %s",strerror(errno));
		return "";
	}
    
    const char *pattern = "X-Subject-Token: ";
    std::string token = "";
	while( NULL != fgets(buff, sizeof(buff), fstream) )
	{
        const char *start;
        if ( NULL != (start = strstr(buff, pattern)) )
        {
            start += strlen(pattern);
            token = std::string(start);
            pclose(fstream);
            return token;
        }
	}
	
	pclose(fstream);
    std::cout << buff << std::endl;
	return token;
}

int main(int argc, const char *argv[])
{
    if ( argc != 4 )
    {
        std::cout << "Usage: get_token ip app_name pwd" << std::endl;
        return 0;
    }
    
    const char *ip = argv[1];
    const char *app_name = argv[2];
    const char *pwd = argv[3];
    
    std::string token = get_token(ip, app_name, pwd);
    if ( "" == token )
    {
        std::cout << std::endl << "get token failed" << std::endl;
    }
    else
    {
        std::cout << std::endl << "get token success, token: " << token << std::endl;
    }
	return 0;
}
