import pika
from pika.exchange_type import ExchangeType

#call back method
def on_message_received(ch, method, properties, body):
    print(f"Payments Service - received new message :{body}")

# create connection
connection_parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_parameters)

#create channel
channel=connection.channel()

#exchange
channel.exchange_declare(exchange='mytopicexchange',exchange_type=ExchangeType.topic)

#declare queue
queue=channel.queue_declare(queue='', exclusive=True)

#bind with routing key
channel.queue_bind(exchange='mytopicexchange',queue=queue.method.queue, 
    routing_key='#.payments')

#consume queue
channel.basic_consume(queue=queue.method.queue, auto_ack=True, 
    on_message_callback=on_message_received)

#check
print("Starting Consuming")

channel.start_consuming()