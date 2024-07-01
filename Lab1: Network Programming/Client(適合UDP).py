import socket

server_address = '127.0.0.1'
server_port = 20213
message = b"This is a test from python client"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#UDP是無連結協定，因此connect()方法不是必須的，但可將socket「連接」到特定的遠端位址，即可使用send()和recv()而不是sendto()和recvfrom()，使程式碼簡潔。
#並不意味著建立了一個真正的連接，因為UDP本質上仍然是無連接的。
#對於TCP是必要的，TCP是面向連接通訊，要確保客戶端與伺服器的穩定連結，通過連結發送和接收數據。
sock.connect(("127.0.0.1",20213))

#傳送資料
print(f'Client sending: {message.decode("utf-8")}')
sock.send(message)

#接收資料
#解碼與列印
data = sock.recv(10240)
print(f'Client received: {data.decode("utf-8")}')

#關閉socket
print('Client closing socket')
sock.close()




'''
try:
    message = b'This is a test from python client'
    print(f'Client sending: {message.decode("utf-8")}')
    sock.sendto(message, (server_address, server_port))
    data, address = sock.recvfrom(20213)
    print(f'Client received: {data.decode("utf-8")}')

finally:
    print('Client closing socket')
    sock.close()

#錯誤處理：使用try-finally結構，確保即使在發生錯誤時也能正確關閉socket。
#傳送資料：使用sock.sendto(message, (server_address, server_port))來傳送資料。這通常用於無連接的協定（如UDP），其中指定了伺服器的位址和連接埠。
#接收數據：使用sock.recvfrom(20213)來接收數據，這同樣是針對無連接的協定設計的。 20213是指定的最大位元組數。
#解碼與列印：功能與第一段程式碼相同，接收的資料被解碼並列印。
#關閉socket：確保在finally區塊中關閉socket。
'''