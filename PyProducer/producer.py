import os
import pika
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Environment variables configuration
# Reading RabbitMQ and FastAPI settings from environment variables
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", 'miFanoutExchange')
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", 'pyqueue')
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8001))

# Function to connect to RabbitMQ
def connect_to_rabbitmq():
    try:
        # Setting up RabbitMQ credentials and connection parameters
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials
        )
        # Establishing connection to RabbitMQ
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

        print("RabbitMQ connection established")
        return connection, channel
    except Exception as error:
        # Handling connection errors
        print(f"Error connecting to RabbitMQ: {error}")
        raise HTTPException(status_code=500, detail="Failed to connect to RabbitMQ")

# Function to send a message to RabbitMQ
def publish_message(channel, message):
    try:
        # Publishing the message to the specified exchange and queue
        channel.basic_publish(
            exchange=RABBITMQ_EXCHANGE,
            routing_key="",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)  # Making the message persistent
        )
        print(f"Message published: {message}")
    except Exception as error:
        # Handling errors during message publishing
        print(f"Error publishing message: {error}")
        raise HTTPException(status_code=500, detail="Failed to publish message")

# Initialize the FastAPI application
app = FastAPI()

# Data model for the message
class Message(BaseModel):
    content: str  # Defining the structure of the message

# Endpoint to send a message
@app.post("/send")
def send_message(message: Message):
    # Connecting to RabbitMQ and publishing the message
    connection, channel = connect_to_rabbitmq()
    publish_message(channel, message.content.strip())
    connection.close()  # Closing the connection after publishing
    return {"message": f"Message sent: {message.content}"}

# Run the application
if __name__ == '__main__':
    import uvicorn
    # Starting the FastAPI server
    uvicorn.run(app, host='0.0.0.0', port=FASTAPI_PORT)
