try:
    import pika
    import random
    import time
except Exception as e:
    print(f'Missing libraries: {e}')

try:
    conn_parm = pika.ConnectionParameters('localhost')

    conn = pika.BlockingConnection(conn_parm)

    channel = conn.channel()

    channel.queue_declare(queue='messagequeue')

    messageId = 1

    while(True):
        message = f"This is the published message - {messageId}"
        channel.basic_publish(exchange="", routing_key="messagequeue", body=message)
        print(f"message sent: {messageId}")
        time.sleep(random.randint(1,3))
        messageId += 1

except Exception as e:
    print(f"Exception Occured: {e}")

finally:
    try:
        conn.close()
    except Exception as e:
        print(f"Failed to connect: {e}")
    