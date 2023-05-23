import pika, os, sys
from models import EnhancedVideoNotifyRequest


def send_notification_type(notify_request: EnhancedVideoNotifyRequest):
    pass


def notification_consumer(queue_name: str, routing_key: str, send_notification: send_notification_type):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.create_channel()

    exchange = "enhanced.video.notification"
    channel.exchange_declare(exchange=exchange, exchange_type="topic", durable=True)

    result = channel.queue_declare(queue=queue_name, durable=True)

    channel.queue_bind(exchange=exchange, queue=result.method.queue, routing_key=routing_key)

    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        notify_request = EnhancedVideoNotifyRequest.loads(body)
        try:
            send_notification(notify_request)
        except Exception as e:
            print("error sending notification", e)
            ch.basic_nack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_ack(delivery_tag=method.delivery_tag)
    
    channel.basic_consume(queue=result.method.queue, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    finally:
        connection.close()