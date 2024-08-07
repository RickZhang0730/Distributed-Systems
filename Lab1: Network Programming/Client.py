import socket

server_address = '127.0.0.1'
server_port = 20213
message = b"This is a test from python client"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#UDP是無連結協定，因此connect()方法不是必須的，但可將socket「連接」到特定的遠端位址，即可使用send()和recv()而不是sendto()和recvfrom()，使程式碼簡潔。
#並不意味著建立了一個真正的連接，因為UDP本質上仍然是無連接的。
#對於TCP是必要的，TCP是面向連接通訊，要確保客戶端與伺服器的穩定連結，通過連結發送和接收數據。
sock.connect(("127.0.0.1", 20213))

#傳送資料
print(f'Client sending: {message.decode("utf-8")}')
sock.send(message)

#接收資料
#解碼與列印:接收到的資料被解碼為UTF-8字串並列印出來
#recv(bufsize)，bufsize:一次接收最大字數值，可自己設定
data = sock.recv(10240)
print(f'Client received: {data.decode("utf-8")}')

#關閉socket
print('Client closing socket')
sock.close()