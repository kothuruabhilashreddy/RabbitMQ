try:
    import pika
    from pika.exchange_type import ExchangeType

except Exception as e:
    print(f"Missing Libraaries: {e}")

def on_message_received(ch, method, properties, body):
    print(f"Message received from producer: {body}")


try:
    conn_params = pika.ConnectionParameters('localhost')

    conn = pika.BlockingConnection(conn_params)

    channel = conn.channel()

    channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

    queue = channel.queue_declare(queue="", exclusive=True)

    channel.queue_bind(exchange="pubsub", queue = queue.method.queue)

    channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

    print('Consumer 1 started consuming....')

    channel.start_consuming()

except KeyboardInterrupt:
    print("Stopping consumer....")

except Exception as e:
    print(f"Exception Occured: {e}")






