import socket

server_address = '127.0.0.1'
server_port = 20213
message = b"This is a test from python client"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#這段對於TCP是必要的，TCP是面向連接通訊，要確保客戶端與伺服器的穩定連結，通過連結發送和接收數據。
#才可以使用send()、recv()，而不是sendto()和recvfrom()，使程式碼簡潔。
sock.connect(("127.0.0.1",20213))

sock.send(message)
data = sock.recv(10240)
print(data.decode('utf-8'))

print('Client closing socket')
sock.close()

#傳送資料：使用sock.send(message)來傳送資料。這通常用於面向連接的協定（如TCP）。
#接收數據：使用sock.recv(20213)來接收數據，其中20213是指定的最大位元組數。這同樣適用於面向連線的協定。
#解碼和列印：接收到的資料被解碼為UTF-8字串並列印出來。
#關閉socket：最後關閉socket以結束會話。