## Sales FrontEnd

### What is the project?

This project is a client application that sends a .txt file containing sales data to an API. The API analyzes the data and populates a database, enabling informed decision-making for future business strategies. The application is developed using ReactJS, providing a user-friendly interface, and comprehensive unit testing with Jest ensures its reliability.

### Minimum requirements for use

- NodeJs 16 or higher
- Docker and Docker Compose (for running the application using the provided docker-compose.yml file)

### Installation

Clone the repository:

```bash
git clone git@github.com:paulorobsant/sales-parser-app.git
```

Change to the project directory:

```bash
cd sales-parser-frontend
```

Install the required dependencies:

```bash
yarn install
```

OR

```bash
npm install
```

### How to run the application locally?

After installing the dependencies, follow the steps below.

Use the following command in the terminal to run the project:

```bash
yarn start
```

OR

```bash
npm start
```

### How to run the application via docker?

To run the application, we provide a docker-compose.yml file that sets up the required services and configurations. Follow the steps below to start the application using Docker Compose:

1. Make sure you have Docker Compose installed on your machine.
2. From the project directory, run the following command:

```bash
docker-compose up
```

This will build the Docker image and start the services defined in the docker-compose.yml file.

3. Once the containers are up and running, you can access the interface at http://localhost:3000.

- Use the form to upload .txt files and trigger the data processing and storage.

4. To stop the application, press Ctrl + C in the terminal, and then run the following command to bring down the containers:

```bash
docker-compose down
```

### Future improvements

**Change the use of default CSS to a preprocessor css (Sass, Less) or TailwindCSS:** Currently the project uses only CSS as page styling for the simplicity and size of the project. However, as the project evolves and grows, css preprocessors can help and facilitate the development of page styling in a faster and more robust way.

> This is a challenge by [Coodesh](https://coodesh.com/)
