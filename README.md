## Sales Parser App - Fullstack Pleno Challenge

### What is the project?

This project consists of an application that aims to load sales data in TXT format to be transformed, in the future, into information for decision making in a store.

The goal of this project is to facilitate the process of analyzing sales data for a store, allowing the information to be extracted from TXT files and transformed into relevant data to assist strategic decisions. With this application, raw data can be loaded quickly and efficiently, saving time and effort.

The transformation of raw data into useful information is a crucial step in the success of any business. By using this application, sales data can be processed and analyzed to identify trends, patterns, and valuable insights. This will enable store managers to make decisions based on hard data, driving business growth and efficiency.

### Project description

A new urgent demand has arisen and we need a dedicated area to upload a
upload a file of the transactions made in the sale of products by our
by our customers.
Our platform works on the model creator-affiliate, so a creator
sell their products and have 1 or more affiliates also selling these products
products, provided that a commission is paid per sale.
Your task is to build a web interface that makes it possible to upload a
normalize the data and store it in a relational database.
relational database.
You must use the file sales.txt to test the
the application. The format is described in the section "Input File Format".

### Installation

Clone the repository:

```bash
git clone git@github.com:paulorobsant/sales-parser-app.git
```

Enter the respective folders of the backend and frontend and follow the individual installation for each case or use docker explained below.

### How to run the application?

To run the application, we provide a docker-compose.yml file that sets up the required services and configurations. Follow the steps below to start the API using Docker Compose:

1. Make sure you have Docker Compose installed on your machine.
2. From the project directory, run the following command:

```bash
docker-compose up
```

This will build the Docker image and start the services defined in the docker-compose.yml file.

3. Once the containers are up and running, you can access the API at http://localhost:8000/docs and http://localhost:3000 to access the client.

4. To stop the application, press Ctrl + C in the terminal, and then run the following command to bring down the containers:

```bash
docker-compose down
```

### Final Considerations

Thank you for the opportunity to participate in the selection process for the Fullstack position. I look forward to discussing my experience in the course of developing this project.

Best regards,

Paulo Roberto

> This is a challenge by [Coodesh](https://coodesh.com/)
