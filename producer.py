import pika
from pika.exchange_type import ExchangeType

# create connection
connection_parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_parameters)

#create channel
channel=connection.channel()

#declare exchange
channel.exchange_declare(exchange='mytopicexchange',exchange_type=ExchangeType.topic)

#message1
user_payments_message='A european user paid for something'
channel.basic_publish(exchange='mytopicexchange',routing_key='user.europe.payments',body=user_payments_message)
#check
print(f"sent message :{user_payments_message}")

#message2
business_order_message='A european business ordered goods'
channel.basic_publish(exchange='mytopicexchange',routing_key='business.europe.order',body=business_order_message)
#check
print(f"sent message :{business_order_message}")




#close connection
connection.close()