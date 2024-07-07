try:
    import pika
    import time
    import random
except Exception as e:
    print(f'Missiong required libraries: {e}')

def on_msg_received_cc(ch, method, properties, body):
    processing_time = random.randint(1,6)
    print(f"Consumer started processing message: {body}")
    time.sleep(processing_time)
    print(f"Consumer stopped processing after {processing_time} seconds")
    ch.basic_ack(delivery_tag=method.delivery_tag)




conn_parms = pika.ConnectionParameters('localhost')

conn = pika.BlockingConnection(conn_parms)

channel = conn.channel()

channel.queue_declare(queue="messagequeue")

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="messagequeue", on_message_callback = on_msg_received_cc)

print("Consumer started consuming messages.....")

channel.start_consuming()