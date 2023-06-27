## Sales API

### What is the project?
This project is an API that receives .txt data via an interface upload and processes the rows to insert them into a relational database. It leverages FastAPI, Alembic, Pydantic, and SQLAlchemy to provide a robust and scalable solution for handling the data ingestion and storage process.

### Minimum requirements for use
- Python 3.9 or higher
- Docker and Docker Compose (for running the application using the provided docker-compose.yml file)

### Installation

Clone the repository:

```bash
git clone git@github.com:paulorobsant/sales-parser-app.git
```

Change to the project directory:

```bash
cd api-project
```

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### How to run the application locally?
After installing the dependencies, follow the steps below.

Go to the SRC folder of the project:
```bash
cd src
```

Use the following command in the terminal to run the project:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### How to run the application via docker?
To run the application, we provide a docker-compose.yml file that sets up the required services and configurations. Follow the steps below to start the API using Docker Compose:

1. Make sure you have Docker Compose installed on your machine.
2. From the project directory, run the following command:

```bash
docker-compose up
```

This will build the Docker image and start the services defined in the docker-compose.yml file.

3. Once the containers are up and running, you can access the API at http://localhost:8000.

- Use the /upload_file/ endpoint to upload .txt files and trigger the data processing and storage.
- Additional API endpoints and their functionalities can be found in the API documentation available at http://localhost:8000/docs.

4. To stop the application, press Ctrl + C in the terminal, and then run the following command to bring down the containers:

```bash
docker-compose down
```

### Future improvements

**Switch to a MySQL or PostgreSQL database:** Currently, the project uses SQLite as the database backend. While SQLite is suitable for small-scale applications, migrating to a more robust and scalable database like MySQL or PostgreSQL might be beneficial for larger datasets and concurrent usage scenarios. These databases offer better performance, support advanced features, and provide stronger data integrity and security.

- To switch to MySQL: Update the DATABASE_URL in database.py to use the appropriate MySQL connection string. Install the necessary dependencies (pip install databases[mysql]), and modify the docker-compose.yml file to include a MySQL service configuration.

- To switch to PostgreSQL: Update the DATABASE_URL in database.py to use the appropriate PostgreSQL connection string. Install the necessary dependencies (pip install databases[postgresql]), and modify the docker-compose.yml file to include a PostgreSQL service configuration.

Remember to update the database connection details and ensure that the required database server is accessible and properly configured.

**Queuing mechanism:** Inclusion of a queuing mechanism (RabbitMQ, Kakfa or SQS) to control the processing of large amounts of data. This would help cope with the increased volume of data and ensure efficient and scalable processing.

**Improvement to sales_type column:** Currently only the sale type number is saved in the bank. In the future, it would be interesting to think of a more intelligent solution, such as: a relational table of sales type or an enum type for the type of sale.

>  This is a challenge by [Coodesh](https://coodesh.com/)