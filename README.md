# Taller RabbitMQ: Despliegue de Contenedores Publish/Subscribe

Este taller tiene como objetivo desplegar la actividad de **publish/subscribe** utilizando RabbitMQ a través de contenedores Docker. Se trabajará en tres versiones, variando la distribución de los contenedores en uno, dos y tres hosts.

> **Nota:**  
> Para ejecutar los comandos de este taller es indispensable contar con una terminal de Linux y tener instalados [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/).

---

## Video
Se puede ver el video [aquí](https://youtu.be/hIbcy_wenq8)

---

## Participantes

- **Mauricio Marin - 2215634**
- **Jorge Gutierrez - 2215631**
- **Janer Vega - 2210048**

---

## Documento de Referencia

Para más detalles y la descripción completa de la actividad, consulta el siguiente documento:  
[Documento de la Actividad](https://docs.google.com/document/d/1hxfH0IAZEcZ8BVq8tEjB-FqElNGhuY01q0lclmWff9U/edit?usp=sharing)

---

## Estructura de la Actividad

La actividad consiste en levantar **7 contenedores** distribuidos de la siguiente forma:

- **3 Contenedores que actúan como consumidores.**
- **3 Contenedores que actúan como publicadores.**
- **1 Contenedor que actúa como broker de mensajería (RabbitMQ).**

> Las máquinas virtuales que se utilizarán son proporcionadas por la materia de Software 3.

---

## Versiones de Despliegue

### Versión 1: Despliegue en una Sola Máquina

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/J4nnn/Taller-RabbitMQ.git

2. **Navegar a la carpeta de la versión 1:**

   ```bash
   cd Taller-RabbitMQ/composes/version1

3. **Ejecutar Docker Compose:**

   ```bash
   docker compose up --build -d

Al finalizar la construcción de las imágenes, se levantarán y ejecutarán correctamente todos los contenedores en una misma máquina.

---

### Versión 2: Despliegue en Dos Máquinas
Esta versión se divide en dos componentes:

- **productsAndConsumers**
- **rabbitmq**

1. **Acceder a la primera máquina virtual (ejemplo: máquina del estudiante Mauricio):**
    
   ```bash
   ssh student@10.6.101.104
Contraseña: ```student104```
   
2. **Clonar el repositorio en la máquina:**

    ```bash
   git clone https://github.com/J4nnn/Taller-RabbitMQ.git

3. **Navegar a las carpetas correspondientes:**

* Para los contenedores de productos y consumidores, dirígete a:
```Taller-RabbitMQ/composes/version2/productsAndConsumers```

* Para el broker de mensajería, dirígete a:
```Taller-RabbitMQ/composes/version2/rabbitmq```

4. **Ejecutar Docker Compose en cada componente:**
Utiliza el siguiente comando para levantar los contenedores (por ejemplo, para el broker):

    ```bash
   docker compose up --build -d
   
> **Importante:** En el taller se utilizó el archivo 
> docker-compose.yml del componente rabbitmq para el despliegue.

### Versión 3: Despliegue en Tres Máquinas
En esta versión se distribuyen los contenedores en tres máquinas virtuales. 
Por ejemplo, para la máquina del estudiante Jorge:

1. **Acceder a la máquina virtual:**

    ```bash
   ssh student@10.6.101.99
Contraseña: ```student99```

2. **Clonar el repositorio en la máquina:**

    ```bash
   git clone https://github.com/J4nnn/Taller-RabbitMQ.git

3. **Navegar a la carpeta de la versión 3:**

    ```bash
   cd Taller-RabbitMQ/composes/version3

4. **Ejecutar Docker Compose en cada máquina según el rol asignado:**

* En cada host se ejecutarán los contenedores correspondientes a consumers, producers o rabbitmq usando el comando:

    ```bash
   cd Taller-RabbitMQ/composes/version3

Con estos pasos, al finalizar el despliegue en cada máquina, se habrá establecido la conexión de los 7 contenedores distribuidos entre tres hosts.
