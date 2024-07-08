try:
    import pika
except Exception as e:
    print(f"Missing libraries: {e}")

def on_message_received(ch, method, properties, body):
    print(f"Message received from producer to consumer: {body}")

try:
    conn_parms = pika.ConnectionParameters('localhost')
    
    conn = pika.BlockingConnection(conn_parms)

    channel = conn.channel()

    queue = channel.queue_declare(queue = "", exclusive=True)

    # Not binding it with pubsub exchange
    # channel.queue_bind(queue= queue.method.queue, exchange= "pubsub")

    channel.basic_consume(queue = queue.method.queue, auto_ack= True, on_message_callback = on_message_received)

    print("Consumer started consuming......")

    channel.start_consuming()

except KeyboardInterrupt:
    print("Stopping consumer........")

except Exception as e:
    print(f"Exception Occured: {e}")