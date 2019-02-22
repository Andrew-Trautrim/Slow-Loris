#include <iostream>

using namespace std;

int main(int argc, char **argv) {

	if(argc != 4) {
		cout << "Usage: "<< argv[0] << "<target IP> <target port> <socket count>" << endl;
	}

	const char* targetIP = atoi(argv[1]);
	const unsigned short targetPort = atoi(argv[2]);
	const int = atoi(argv[3]);

	return 0;
}
