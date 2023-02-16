from kafka import KafkaConsumer, consumer
from hdfs import InsecureClient
from time import sleep
import json
from time import sleep, time
import pandas as pd
import os


class MovieConsumer:
    broker = ""
    topic = ""
    group_id = ""
    logger = None

    def __init__(self, broker, topic, group_id):
        self.broker = broker
        self.topic = topic
        self.group_id = group_id
        self.hdfs_client = InsecureClient('http://localhost:9870', user='root')
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=[self.broker],
            group_id=self.group_id,
            consumer_timeout_ms=60000,
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda m: json.loads(m.decode('utf8'))
        )

    def activate_listener(self):
        consumer = self.consumer

        print("[*] consumer is listening....")
        try:
            
            # run consumer like a daemon
            while True:
                msg_pack = consumer.poll(10.0)
                if msg_pack is None:
                    continue
                for tp, messages in msg_pack.items():
                    data = []
                    tmp_path = f'films-{int(time())}.csv'
                    for message in messages:
                        print(f" [x] Receive film: {message.value.get('title') or 'NULL'}")
                        data.append(message.value)              

                        #committing message manually after reading from the topic
                        consumer.commit()
                
                    print(f' [x] Finish read {len(data)} messages from broker')

                    # save data to a temp file
                    df = pd.read_json(json.dumps(data))
                    df.to_csv(tmp_path)
                    
                    # upload file to hdfs
                    self.hdfs_client.upload('/', tmp_path, overwrite=True)
                    
                    # delete temp file
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
                    
                    print(' [x] Finish upload file to hdfs')
                    print('***')
                
                sleep(10)
            
        except KeyboardInterrupt:
            print("Aborted by user...")
        finally:
            consumer.close()
            


#Running consumers
broker = 'localhost:9092'
topic = 'film'
group_id = 'consumers'

consumer = MovieConsumer(broker,topic,group_id)
consumer.activate_listener()

# consumer2 = MessageConsumer(broker,topic,group_id)
# consumer2.activate_listener()
