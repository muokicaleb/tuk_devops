# Microservices Calculator Project

## Overview

This project is composed of four distinct microservices, each responsible for a basic arithmetic operation: addition, subtraction, multiplication, and division. Built with FastAPI, these microservices offer a scalable and efficient way to handle mathematical operations. An NGINX server is configured as a reverse proxy to route incoming requests to the appropriate microservice based on the request path.

## Services

- **Addition Service**: Provides an endpoint to add two numbers.
- **Subtraction Service**: Offers functionality to subtract one number from another.
- **Multiplication Service**: Enables multiplying two numbers.
- **Division Service**: Handles division of one number by another, including division by zero handling.

## Getting Started

### Prerequisites

To run this project, you will need Docker and Docker Compose installed on your machine. These tools will handle the containerization and orchestration of the microservices and NGINX server.

### Running the Services

Follow these steps to get your microservices up and running:

1. Clone the repository:
   ```bash
   git clone git@github.com:muokicaleb/tuk_devop
   ```

2. Use Docker Compose to build and start the services:
   ```bash
   docker-compose up --build
   ```

This command will build the Docker images for each microservice and the NGINX server, then start them in containers. NGINX will be configured to listen on port 80 and route requests to the appropriate microservice.

### Testing the Services

You can test the functionality of each microservice through the NGINX server using `curl` commands:

- **Addition**:
  ```bash
  curl -X POST http://localhost/add -H "Content-Type: application/json" -d '{"a": 10, "b": 5}'
  ```

- **Subtraction**:
  ```bash
  curl -X POST http://localhost/subtract -H "Content-Type: application/json" -d '{"a": 10, "b": 3}'
  ```

- **Multiplication**:
  ```bash
  curl -X POST http://localhost/multiply -H "Content-Type: application/json" -d '{"a": 4, "b": 5}'
  ```

- **Division**:
  ```bash
  curl -X POST http://localhost/divide -H "Content-Type: application/json" -d '{"a": 20, "b": 4}'
  ```

## Contributing

Contributions to this project are welcome. Please follow the standard fork and pull request workflow. Ensure you write or update tests as necessary for any code changes.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.

