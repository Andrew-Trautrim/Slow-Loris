#include <iostream>
#include <netinet/in.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>

using namespace std;

int main(int argc, char **argv) {

	if(argc != 4) {
		cout << "Usage: "<< argv[0] << "<target IP> <target port> <socket count>" << endl;
	}

	struct sockaddr_in target;
	const char* targetIP = argv[1];
	const unsigned short targetPort = atoi(argv[2]);
	const unsigned int socketCount = atoi(argv[3]);
	char buffer[1024];

	target.sin_family = AF_INET;
	target.sin_port = htons(targetPort);

	int connections[socketCount];

	return 0;
}
