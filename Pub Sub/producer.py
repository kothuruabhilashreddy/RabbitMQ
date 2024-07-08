try:
    import pika
    from pika.exchange_type import ExchangeType
except Exception as e:
    print(f"Missing libraries: {e}")


try:
    conn_parms = pika.ConnectionParameters('localhost')

    conn = pika.BlockingConnection(conn_parms)

    channel = conn.channel()

    channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

    message = "Message broadcasted from producer"

    print("Producer started publishing message.....")

    channel.basic_publish(exchange="pubsub", routing_key="", body=message)

except Exception as e:
    print("Exception Occured: {e}")

finally:
    try:
        conn.close()
    except Exception as e:
        print(f"Failed closing connection: {e}")

