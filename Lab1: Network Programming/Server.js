//使用 'dgram'模組建立一個UDP Socket
//使用 createSocket() 方法，並傳入'udp4'參數來建立一個IPv4的Socket
const dgram = require('node:dgram');
const server = dgram.createSocket('udp4');

//處理錯誤
//印出錯誤訊息，然後關閉伺服器
server.on('error', (err) => {
    console.error(`server error:\n${err.stack}`);
    server.close();
});

//處理與回應訊息
//設定message事件的處理程序
//當收到客戶端發送的訊息時，會印出該訊息、客戶端的IP位址以及port number
server.on('message', (msg, rinfo) => {
    console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);

    //const responseMessage = JSON.parse(`${rinfo.port}:${msg.toString}`);
    const responseMessage = Buffer.from(`${rinfo.port}:${msg}`);

    server.send(responseMessage, rinfo.port, rinfo.address, (err) => {
        server.close();
    });
});

server.on('listening', () => {
  const address = server.address();
  console.log(`server listening ${address.address}:${address.port}`);
});

server.bind(("127.0.0.1", 20213));