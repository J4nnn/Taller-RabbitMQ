FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

ENV RABBITMQ_HOST=rabbitmq
ENV RABBITMQ_PORT=5672
ENV RABBITMQ_USER=guest
ENV RABBITMQ_PASSWORD=guest

EXPOSE 3001
CMD ["node", "server.js"]
