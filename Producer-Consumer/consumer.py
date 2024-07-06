try:
    import pika

except Exception as e:
    print(f"Missing libraries: {e}")

def on_message_received(ch, method, properties, body):
    print(f'Message received at Consumer end: {body}')

try:
    conn_parms = pika.ConnectionParameters('localhost')

    conn = pika.BlockingConnection(conn_parms)

    channel = conn.channel()

    channel.queue_declare(queue='messagequeue')

    channel.basic_consume(queue='messagequeue', auto_ack=True, on_message_callback= on_message_received)

    print("Consumer started consuming messages.....")

    channel.start_consuming()

except KeyboardInterrupt:
    print("Stopping Consumer")

except Exception as e:
    print(f"Exception Occured: {e}")

finally:
    try:
        conn.close()
    except Exception as e:
        print(f"Failed closing the connection: {e}")
