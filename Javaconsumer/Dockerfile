# Etapa 1: Construcción de la aplicación
FROM maven:3.9.6-eclipse-temurin-17 AS maven

COPY ./src ./usr/local/app/src

COPY ./pom.xml /usr/local/app

WORKDIR /usr/local/app

RUN mvn clean package -DskipTests

# Etapa 2: Creación de la imagen final con JDK
FROM eclipse-temurin:17

COPY --from=maven /usr/local/app/target/software3-taller1-consumer-0.0.1.jar /usr/share/app.jar

ENV JAVA_RABBITMQ_HOST=my-rabbitmq
ENV JAVA_RABBITMQ_PORT=5672
ENV JAVA_RABBITMQ_USERNAME=guest
ENV JAVA_RABBITMQ_PASSWORD=guest

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/usr/share/app.jar"]
