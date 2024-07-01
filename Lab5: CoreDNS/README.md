# Lab5: CoreDNS

操作一: 下傳並安裝CoreDNS
```bash
1.請依照您的作業系統下傳適合的CoreDNS版本 (請下傳1.10.x)。
例如: https://github.com/coredns/coredns/releases/tag/v1.10.1
Windows作業系統建議: coredns_1.10.1_windows_amd64.tgz
MacOS作業系統建議: (M1 or M2) coredns_1.10.1_darwin_arm64.tgz
                   (x86) coredns_1.10.1_darwin_amd64.tgz

2.解壓後，應該就可以獲得Coredns的可執行檔，請新建一個目錄並將它拷貝過去，例如c:\lab\coredns\。
3.設定Corefile: 請在coredns執行檔相同目錄下，建立一個名稱為「Corefile」的檔案(請留意大小寫)，其內容如下:
.:1053 {
    forward . 8.8.8.8:53
    errors
    log
}
nccu.lab:1053 {
    file db.nccu.lab
    errors
    log
}
上面這個設定會讓coredns在1053 port開啟一個dns服務，提供nccu.lab網域名稱的查詢，其中，nccu.lab的檔案會放在同目錄下的db.nccu.lab
4.設定Zonefile (db.nccu.lab): 請在coredns執行檔相同目錄下，建立一個名稱為「db.nccu.lab」的檔案(請留意大小寫)，其內容如下(如果有問題，請刪掉引號並手動重打一次引號):
@	 3600  IN	SOA sns.dns.icann.org. noc.dns.icann.org. (
				2017042745 ; serial
				7200       ; refresh (2 hours)
				3600       ; retry (1 hour)
				1209600    ; expire (2 weeks)
				3600       ; minimum (1 hour)
				)
      3600 IN A     127.0.0.1
3600 IN TXT   "hello nccu.lab"
www  3600 IN A     127.0.0.1
   3600 IN TXT   "hello www.nccu.lab"
在這個設定檔中，我們分別為預設網域名稱(nccu.lab)與www.nccu.lab加入了A與TXT的RR。其中，根據查詢的不同，dns client應該可得到不同的txt回應。請依據上面的設定，說明查詢 www.nccu.lab的TXT時，會回傳什麼內容? (提示: 完成操作二後，可以透過dig看到正確答案)

5.在命令列下執行coredns執行檔，它應該在port 1053啟動伺服器。正常的話，應該會顯示下列訊息。
```

操作二: 安裝與測試dig
```bash
1.如果您使用的是windows作業系統，請到moodle下傳dig-windows的zip檔案，解壓後依據: https://www.minwt.com/pc/19816.html 的指引進行安裝
2.如果您使用的是Mac或Linux，則作業系統應已經有dig程式了，請在命令列下測試看看: dig –h 
3.使用dig來取得nccu.lab的TXT，並將「ANSWER SECTION」的內容貼在「答」的下面。
指令提示: dig @localhost -p 1053 TXT nccu.lab
```

操作三: 寫作程式進行DNS查詢
```bash
1.使用您的開發工具，建立一個名為「corednslab」的空專案新增一個package.json。
提示: 若您的開發工具不支援產生package.json，可透過命令列: npm init來產生。
2.	請在package.json中的dependencies中加入下列library: 
"dns2": "^2.1.0"
提示: 
…,
   "dependencies": {
        "dns2": "^2.1.0"
  }, …

3.執行npm install，此時系統會自動安裝上述libraries到node_modules底下。
4.新增一個檔案:dnsclient.js，樣板內容如下，請修改(A)~(C)，來完成「取得nccu.lab的TXT」的動作。若運作正確，程式應輸出以下資訊:
提示: 如果程式執行後卡住沒回應，請確認coredns有在port 1053執行。

程式碼樣板如下，請將(A)~(C)取代為正確的值(提示: A是本地端coredns的IP; B是要查詢的伺服器domain name，C是type; B和C的作答配合上面紅字的部份):

const dns2 = require('dns2');
const { UDPClient } = require('dns2');
const resolve = UDPClient({
  dns:'(A)', port: 1053, recursive: false
});
(async () => {
  const response = await resolve('(B)', '(C)');
  console.log(response.answers);
})();

請將(A)(B)(C)的內容寫在「答」的下方
```
