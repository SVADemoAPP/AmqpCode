all: get_token subscribe unsubscribe MQReceiver

get_token : get_token.cpp
	g++ -o get_token get_token.cpp


subscribe: subscribe.cpp
	g++ -o subscribe subscribe.cpp


unsubscribe: unsubscribe.cpp
	g++ -o unsubscribe unsubscribe.cpp


MQReceiver: MQReceiver.cpp
	g++ MQReceiver.cpp -o MQReceiver -I./include -L./lib/qpid -lqpidclient -lqpidmessaging -lqpidtypes -lqpidcommon -lqpid-proton -lboost_program_options -lboost_system  -L./lib/nss -lssl3 -lnss3 -lnssutil3 -lplds4 -Wl,-lrt,-rpath,'./lib/qpid/:./lib/nss/' -m32

clean:
	rm -rf get_token subscribe unsubscribe MQReceiver

