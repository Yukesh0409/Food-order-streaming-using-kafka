import json
import time
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_detail"
ORDER_LIMIT = 100000

producer = KafkaProducer(bootstrap_servers="localhost:29092")
print("Producer started")
print("Data will be sent after 10 seconds")
time.sleep(10)

for i in range(1,ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"yukesh_{i}",
        "total_cost": i,
        "items": "Biriyani, Fried rice",
    }
    producer.send("order_details", json.dumps(data).encode("utf-8"))
    print(f"Order {1} sent successfully!")
