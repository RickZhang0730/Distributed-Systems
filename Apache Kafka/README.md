# Apache Kafka
## Kafka設計概念
- 最初目的：LinkedIn 解決吞吐量大的即時日誌 ( Event Logs )
- 現今主要角色：來處理大型公司可能擁有的所有即時 Big Data Streaming 的統一平臺
- 設計概念：
  - 發佈訂閱模型
  - 訊息的持久化、消息保留
  - 高吞吐量 ( 百萬等級 )
  - 對分散式與高擴展式的支持，代表高容錯率、高負載量

## Kafka應用場景
- Message Queuing
- Log Aggregation
- Stream Processing
- Web Activity Tracking
- Decoupling

## Kafka的重要性
- 如果沒有Kafka
  - 資料處理延遲
  - 監控和分析能力受限
  - 資料丢失風險提高
  - 擴展困難
  - 系統脆弱

## 相近技術比較：Kafka vs RabbitMQ
<div align = left><img width="550" height="320" src="https://github.com/RickZhang0730/Distributed-Systems/blob/main/Apache%20Kafka/Kafka_vs_RabbitMQ.jpg"></div>

## 比較下 Kafka 的優勢
- Kafka 在訊息傳輸容量方面優於 RabbitMQ，在處理大量資料方面表現出色
- Kafka 以極低的延遲串流式傳輸訊息，適合即時分析串流資料
- Kafka 適用於需要重新分析所接收資料的應用程式，可以在保留期間內多次處理串流資料，或收集紀錄檔案進行分析

## 可改善方向
- Kafka 部分程式語言的 Client Libraries，尚未支援所有功能， 故應持續增進功能的完整度。
- 利用順序寫入達到高吞吐量，若其中一台機器出問題可能造成訊息亂掉
- 僅保證單一分區有順序性，無法保證多分區的順序性

## 實作與Demo
- 步驟 1: 下載 Kafka
```bash
下載 Kafka: https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
解壓縮: $ tar -xzf kafka_2.13-3.7.0.tgz
進入 Kafka 資料夾: $ cd kafka_2.13-3.7.0
```
- 步驟 2: 啟動 Kafka 執行環境
```bash
注意! 需已先安裝好 Java 8
啟動 Zookeeper 服務: $ bin/zookeeper-server-start.sh config/zookeeper.properties
啟動 Kafka broker 服務: $ bin/kafka-server-start.sh config/server.properties
```
- 步驟 3: 建立 Topic 來儲存 Event
```bash
建立 Topic 與 Event:  $ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```
- 步驟 4: 寫入 Event 到 Topic 中
```bash
若以檔案系統作比喻，Topic 如同資料夾，Event 如同資料夾中的檔案
寫入 Event  到 Topic 中: $ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092 This is my first event This is my second event
```
- 步驟 5: 讀取 Event
```bash
讀取 Event: $ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
特性: Event 可重複被 Consumer 讀取
```
## DEMO
- Link: https://youtu.be/7E_Oevb6NDY


## Kafka的優勢、問題與貢獻
- Kafka 可以幫助即時的高吞吐串流數據處理
- 降低數據丟失風險、支持快速擴展系統
- 分析Uber每日要處理數百萬實時數據的大型系統
- 利用Kafka的分散式架構解決大流量問題以及支援水平擴展
- Kafka的分散式架構可透過增加伺服器來增加處理問題能力

## 小組分工
- 技術實作、Demo: 「張詠軒」、蔡典翰
- 架構解析: 賴廷恩, 羅仕欽, 陳彥維
- 評論、結語： 徐宇文、柯詠媃
- 目的核心，應用場景: 張聚洋、施瑋昱





