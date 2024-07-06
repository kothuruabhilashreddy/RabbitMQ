try:
    import pika

except Exception as e:
    print(f"Missing libraries: {e}")

try:
    conn_params = pika.ConnectionParameters('localhost')

    conn = pika.BlockingConnection(conn_params)

    channel = conn.channel()

    channel.queue_declare(queue="messagequeue")

    message = "First Message - TEST"

    channel.basic_publish(exchange='', routing_key='messagequeue', body=message)

    print('Message sent from Producer end:', message)

except Exception as e:
    print(f"Exception Occured: {e}")

finally:
    try:
        conn.close()
    except Exception as e:
        print(f"Failed to close connection: {e}")

