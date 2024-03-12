
<p align="center">

![Image Alt text](/readme_images/initial.png)

</p>

<p align="center">
<img src="https://img.shields.io/badge/docker-25.0.3-blue"/>
<img src="https://img.shields.io/badge/docker--compose-2.24.6-9cf"/>
<img src="https://img.shields.io/badge/python-3.11-yellowgreen"/>
<img src="https://img.shields.io/badge/mongo-7.0.5-green"/>
<img src="https://img.shields.io/badge/postgres-16.1-lightgrey"/>
<img src="https://img.shields.io/badge/framework-fastAPI-brightgreen"/>
<img src="https://img.shields.io/badge/framework-django-green"/>
</p>

---

<h1 align="center">
   🚀 Exams Fraud Analyzer
</h1>
<p align="center">
    <em>
    Project that allows ingesting the data coming from the different sensors and detects when a specific person is committing fraud in exams
    </em>
</p>

Summary
=================

   * [Problem description](#problem-description)
   * [Specifications](#specifications)
   * [Schemas](#schemas)
   * [How it works](#how-it-works)
      * [Custom Templates](#custom-templates)
      * [Django Admin](#django-admin)
   * [Using the APIs](#using-the-apis)
   * [Makefile](#makefile)
   * [Requirements](#requirements)

---

## Problem description

![Image Alt text](/readme_images/problem.png)

---

## Specifications

The system consists of:

1. API Python FastAPI + MongoDB
2. WEB System Python Django + PostgreSQL
3. API Python FastAPI
4. Docker + Docker-compose

Organization:

1. sensor-receiver-api:

API responsible for input all data extracted from monitors. The API provides Swagger (OpenAPI) documentation.

_Runs in_: http://0.0.0.0:8001/docs

2. analysis-system-web:

WEB system responsible for managing the whole ecosystem.

_Runs in_: http://0.0.0.0:8000

3. consultive-api:

Secure API responsible for making data available. The data includes fraud details, fraud related to persons and fraud evidences. The API provides Swagger (OpenAPI) documentation.

_Runs in_: http://0.0.0.0:8002/docs

_Extra (DEVELOPER): mongo-express:_

_In order to make easier to interact with the stored data in this project, mongo-express runs in this project. It's possible to accesse this tool using the credencials:_
* _user: admin_
* _password: admin123_

_Runs in_: http://0.0.0.0:8081/

---

## Schemas

![Image Alt text](/readme_images/postgresql.png)

![Image Alt text](/readme_images/mongodb.png)

_Obs: The user / authorization related tables are not mentioned above, because it is using Django tables._

---

## How it works

1. Use the command "make setup" in this root project's terminal.

2. After a while, the project will ask you about super user credentials.

![Image Alt text](/readme_images/superuser.png)

3. Once the project is up, you are able to login in http://0.0.0.0:8000 and use all funcionalities.

![Image Alt text](/readme_images/django.png)

### Custom Templates

Once your logged in, the http://0.0.0.0:8000 will redirect you to

![Image Alt text](/readme_images/custompage.png)

1. After clicking in "START", the start button will freeze and the end button will start to be available. After clicking in "END" the system will calculate if there was a fraud between this two clicks time. If you dont click in "END", the event will not be registered.
2. The system will always return the results analysis, even if we don't have any data recorded in this meantime.
3. If some problem with the connection between the services occurs, the system will return an error page.

![Image Alt text](/readme_images/result.png)

![Image Alt text](/readme_images/error.png)

### Django Admin

The Django framework provides an admin tool that allow us to manage users access. Inside http://0.0.0.0:8000/admin we are able to create users. 

* Staff users can access both "Consultive API" and "Analysis System WEB".
* Non staff users can acess only "Consultive API".

![Image Alt text](/readme_images/admin.png)

---

## Using the APIs

* Inside the **sensor receiver API**, besides using the functionalities, we are able to run 2 mocks that create registers for a 4 minute event.

![Image Alt text](/readme_images/sensorapi.png)

* Inside the **consultive API**, we need to click in the "Authorize" button and use the credentials created in the setup process or inside the Django Admin's page.

![Image Alt text](/readme_images/consultiveapi.png)

---

## Makefile

This project have some Makefile commands. The main commands are:

* **_make setup_**: Setup the entire environment to run the projects. Only need to use this command once.
* **_make stop_**: Stop all containers.
* **_make start_**: Create containers.
* **_make test_**: Run all tests.

---

## Requirements

* **DOCKER-COMPOSE**: 2.24.6
* **DOCKER**: 25.0.3
