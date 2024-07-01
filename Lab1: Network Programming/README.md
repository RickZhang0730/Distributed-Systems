# 第一部份 UDP
- 1.請依據課程投影片中的範例，寫作符合下列要求的「UDP Client與Server」，其中，Server 請以Node.js寫作，Client請以Python寫作。

- 2.Server的需求:
  - 以Node.js寫作
  - 傾聽本地端(127.0.0.1)的port 20213，接收Client傳來的訊息
  - 在console中印出所接收到的訊息
  - 將收到的訊息的最前面加上「XXXX:」再送回給Client，其中，XXXX是Client的port number。(client的port number請由node.js的API取得)
https://nodejs.org/docs/latest/api/dgram.html#dgram_event_message
提示: 使用server.send方法要嵌入在on message的call back function中，才會在收到訊息之後執行。
  - 印出後立即關閉連線(提示: server.close方法要嵌入在server.send方法中)

- 3.Client的需求:
  - 以Python寫作
  - 連接到本地端的UDP Server，port為20213
  - 送出訊息: 「This is a test from python client」，記得要先將訊息轉為binary: b”This is…..”
  - 在console中印出所接收到的回應訊息 (記得用message.decode(‘utf-8’)將binary轉回文字，正常的話應該會印出xxxxx:This is a test from python client，而不是b’xxxxx:This is a test form python client)
  - 收到後關閉連線
- 請將Server的程式碼則在下面:
- 請將Client的程式碼貼在下面:

## 第二部份 群播
- 1.執行multicastReceiver.js與multicaseSender.js，此時，multicastSender會每5秒送一個封包到群播位址，並被multicastReceiver所接收
- 2.請問它送到那一個群播位址(不含port)? 所傳送的內容為何?
- 3.使用wireshark，設定filter為udp.port==2391，抓取multicastSender送出的封包並觀察它UDP的Length欄位值為多少? UDP Payload的大小(值)為多少?
- 4.UDP Header中的Length欄位代表什麼意思? 為什麼它會比UDP Payload的大小多8 bytes?
