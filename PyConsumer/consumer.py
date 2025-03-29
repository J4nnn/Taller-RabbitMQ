import os
import pika
import threading
from fastapi import FastAPI, HTTPException

# Environment variables configuration
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", 'pyqueue')
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8002))

# Function to connect to RabbitMQ
def connect_to_rabbitmq():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials
    )
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        print("RabbitMQ connection established")
        return connection, channel
    except Exception as error:
        print(f"Error connecting to RabbitMQ: {error}")


# Shared variable to store received messages
received_messages = []

# Function to process incoming messages
def callback(ch, method, properties, body):
    message = body.decode()
    received_messages.append(message)
    print(f"Mensaje recibido: {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Function to start consuming messages
def consume_messages():
    connection, channel = connect_to_rabbitmq()
    channel.basic_qos(prefetch_count=1000)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=False)
    channel.start_consuming()

# Initialize the FastAPI application
app = FastAPI()

# Endpoint to get received messages
@app.get("/messages")
def get_messages():
    return {"messages": received_messages}

# Run FastAPI in a separate thread
if __name__ == '__main__':
    # Create a thread to consume messages
    rabbitmq_thread = threading.Thread(target=consume_messages, daemon=True)
    rabbitmq_thread.start()

    # Start FastAPI in the main thread
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=FASTAPI_PORT)