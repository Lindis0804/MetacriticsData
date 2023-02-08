from kafka import KafkaProducer
import json

class MovieProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)


    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic,msg)
            self.producer.flush()
            future.get(timeout=60)
            # print(msg)
        except Exception as ex:
            return ex


    def bootstrap(self):
        f = open('films.json', encoding="utf8")
        data = json.load(f)
        for i in data:
            self.send_msg(i)
        print("message sent successfully...")

# run producer
broker = 'localhost:9092'
topic = 'film'
producer = MovieProducer(broker, topic)
producer.bootstrap()





