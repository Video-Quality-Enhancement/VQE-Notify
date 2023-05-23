import pika, sys, os
import time


def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    result = channel.queue_declare(queue="720p_queue", durable=True)
    queue_name = result.method.queue
    print(queue_name)

    channel.queue_bind(exchange="video.enhance", queue=queue_name, routing_key="720p")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(2)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=0) # for our case 0 is best, as we never know which video is small and which is big
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def main():
    consumer()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)