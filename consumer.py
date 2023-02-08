from kafka import KafkaConsumer, consumer
from hdfs import InsecureClient
from time import sleep
import json


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

    def activate_listener(self):
        consumer = KafkaConsumer(bootstrap_servers=self.broker,
                                group_id=self.group_id,
                                consumer_timeout_ms=60000,
                                auto_offset_reset='earliest',
                                enable_auto_commit=False,
                                value_deserializer=lambda m: json.loads(m.decode('utf8')))

        consumer.subscribe(self.topic)
        print("consumer is listening....")
        try:
            data = []
            for message in consumer:
                print("received message = ", message)
                data.append(message.value)              

                #committing message manually after reading from the topic
                consumer.commit()
                
            print('Finish read messages from broker')

            # save data to a temp file
            with open('./tmp/data.csv', 'w') as outfile:
                outfile.write(json.dumps(data))
            
            # upload file to hdfs
            self.hdfs_client.upload('/', './tmp/data.csv', overwrite=True)
            print('Finish upload file to hdfs')
            
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
