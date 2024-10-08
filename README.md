# Microservices Platform for Hospital Solutions
**Snehal Awalekar, Bhavna Gupta, Abhilash Chaudhary**

## Introduction
The project aims to develop a microservices-based Hospital Management System that streamlines key functions like patient registration, appointment scheduling, and billing. Using Docker for containerization and Docker Compose for orchestration, the system ensures scalability, modularity, and real-time cloud connectivity to enhance operational efficiency and patient care in modern healthcare settings.

## Features
- **Doctor Service**: Manage doctor information, including specialties, availability, and updates.
- **Patient Service**: Manage patient information including registration, updates, and retrieval of medical records.
- **Appointment Service**: Facilitate scheduling, canceling, and managing doctor appointments.
- **Billing Service**: Manage patient billing and track payments.

## Technology Stack
- **Flask**: Python web framework for creating REST APIs for the services.
- **SQLAlchemy**: Database management for handling data models and operations.
- **SQLite**: Lightweight database for storing service data.
- **Docker**: Containerization for services.
- **Docker Compose**: Service orchestration and management.

## Prerequisites
- **Docker**: Ensure Docker is installed and running.
- **Docker Compose**: To orchestrate the microservices.

## Setup Instructions

### Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/2158374/hospital-management.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd hospital-management/appointment-service
    ```

3. **Build service**:
    ```bash
    docker build -t appointment-service:latest .
    ```
4. **Start the container**:
    ```bash
    docker-compose up -d
    ```

5. **Access the services at their respective endpoints**.

### How to Run the Project
The **Hospital Management System** is structured as independent microservices that communicate through HTTP APIs. Each service manages its respective database using **SQLite** and exposes RESTful endpoints to other services. **Docker Compose** handles service orchestration, making it easy to scale, maintain, and deploy the system in different environments.

### Services Endpoints
- **Patient Service**: `http://34.45.137.121:5001`
- **Doctor Service**: `http://34.45.137.121:5002`
- **Appointment Service**: `http://34.45.137.121:5003`
- **Billing Service**: `http://34.45.137.121:5004`

## Scalability and Upcoming Improvements
- **Horizontal scaling**: To accommodate increasing workloads, each service can be scaled separately.
- **Security Enhancements**: To improve security, include authorization and authentication methods (like OAuth).
