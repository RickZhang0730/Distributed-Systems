# Lab3: Remoting (SOAP+gRPC)
- 操作一: SOAP based Web Services 開發 平台: Node.
- 1.建立一個新的資料夾「lab remoting 」，在此目錄下，新建一個soap 目錄
- 2.在此lab remoting 目錄中建立一個新的package .json 檔案，內容如下:
```bash
{
"name": "dslab remoting",
"version": "
"dependencies":
"soap": "^ 0.36.0",
"@grpc/grpc js": "^1.2.2",
"@grpc/proto loader": "*"
}
```
- 3.在和package.json 同一個目錄下，於命令列執行npm install，安裝所需模組
- 4.確認Adder.wsdl 、AddMu.wsdl 、soapClient.js 與soapServer.js 等檔案存在lab remoting/soap 目錄中。
- 5.開啟並了解soapServer.js 程式碼的功能與意義:
(1)請將soapServer.js 中，含「讀入wsdl 檔」功能的敘述 請貼上整個statementstatement，也就是分號前的所有程式碼))，貼在下面「答」之後
(2)請將soapServer.js 中，含「實作add 並回傳x 和y 之和的實作」功能的敘述(請貼上整個statement)，貼在下面「答」之後
(3)在程式中，建立http server 後，指派給一個變數，該變數的名稱為何?這個http server 傾聽的通訊埠號(port number)為何?
(4)soap.listen(…) 中傳入了四個參數，包含http server 、此服務的掛載網址、WSDL 、及服務實作，請寫出此網址為何
- 6.開啟並了解soap Client .js 程式碼的功能與意義
(1)引入soap 函式庫後，程式呼叫了soap 的createClient 的方法，這個方法傳入二個參數，其中一個是SOAP Server 的WSDL 的位址。請問此位址為何
(2)由createClient 方法所傳入的回呼函式中有二個參數，分別為err與client，由client 我們可以直接呼叫client.add 來呼叫SOAP Server 上的加法函式。其中，args 指的就是傳入遠端add 呼叫的參數x 與yy，請問x 與y 的值各為何
- 7.切換目錄到/soap
- 8.執行node soapServer.js，在console 中應出現server initialized
- 9.執行node soap Client.js，觀察console 所印出的執行結果。
- 10.修改soapClient.js 中的args，試著藉由呼叫SOAP Server 計算x=10 ,y=20 的結果。將soapClient.js 所印出在console 中的SOAP 訊息貼在下面。

- 操作二 寫作新的SOAP 乘法 multiply 服務
- 1.請根據操作一中的觀察，修改soapServer.js，將引入的wsdl 檔案由Adder.wsdl 改為AddMul .wsdl 。
- 2.根據AddMul.wsdl 中的註解，參考add 服務的定義，定義乘法 multiply 服務的相關wsdl 宣告。將修改後的AddMul .wsdl 貼在答的下方 提示: 可參考AddMul.wsdl 中的註解
- 3.修改soapServer.js，在service 中新增multiply 服務與實作
- 提示
```bash
const service = {
CalculatorImplService: {
CalculatorImplPort: {
add: function (args) {
return {result: args.x + args.y};
m ultiply: function(args) {
};
```
- 4.修改soapServer.js，在修改存取網址為「AddMul 」
```bash
soap.listen(server, '/AddMul', service, xml,
function () {
console.log('server initialized');
});
```

- 5.關掉並重新執行soap Server.js，在console中應出現server initialized
- 修改soapClient.js，將url 改為http://localhost:8192/AddMul?wsdl,
  const url = 'http://localhost:8192/AddMul?wsdl';
- 7.修改soapClient.js js，將client.add 改為client.multiply
- 提示:
```bash
client.multiply(args, function (err, result, rawResponse, soapHeader,
rawRequest) {
if (err) console.log(err);
console.log(rawRequest);
console.log('');
console.log(rawResponse);
```
- 8.修改soapClient.js 中的argsargs，試著藉由呼叫SOAP Server 計算x=10, y=20 的結果。將soapClient.js 所印出在console 中的SOAP 訊息貼在下面。
- 9.結束後記得關閉soapServer.js
- ..........
