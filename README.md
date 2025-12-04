🗳️ Sistema de Votación en Tiempo Real

Backend con Django + Channels + WebSockets + MySQL + Redis (Dockerizado)

Este proyecto implementa un sistema de votaciones en tiempo real utilizando Django, Django REST Framework, Channels, WebSockets, Redis y MySQL, todo ejecutándose dentro de contenedores Docker.

Los usuarios pueden:

Crear encuestas (Polls)

Agregar opciones (Choices)

Emitir votos (Votes)

Ver la votación actualizándose en tiempo real gracias a WebSockets 🔥

Tecnologías utilizadas
Componente	Descripción
Django 5	Framework backend principal
Django REST Framework	API REST para polls y votos
Django Channels	Soporte WebSockets
Redis	Channel Layer para tiempo real
MySQL	Base de datos relacional
Docker + Docker Compose	Orquestación de servicios

Estructura del proyecto
sistema-votacion/
│── backend/
│   ├── polls/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── consumers.py
│   │   ├── admin.py
│   │   └── routing.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── ...
│
│── docker-compose.yml
│── Dockerfile
│── README.md

Cómo ejecutar el proyecto
1️⃣ Requisitos previos
Tener instalado Docker y Docker Compose.
2️⃣ Clonar el repositorio
git clone https://github.com/tuusuario/sistema-votacion.git
cd sistema-votacion
3️⃣ Crear y levantar los contenedores
docker-compose up -d --build
4️⃣ Aplicar migraciones de Django
docker exec -it voting_backend python manage.py migrate
5️⃣ Crear el superusuario
docker exec -it voting_backend python manage.py createsuperuser 
6️⃣ Acceder al panel de administración
👉 http://localhost:8000/admin/

Desde ahí podrás:
Crear encuestas (Polls)
Agregar opciones (Choices)
Ver usuarios y votos

Servicios incluidos en Docker Compose
voting_backend	8000	API + WebSockets
voting_db	3307	Base de datos MySQL
voting_redis	6379	Redis para Channels
