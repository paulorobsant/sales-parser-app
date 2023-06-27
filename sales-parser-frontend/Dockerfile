# Base Image
FROM node:18

# Working directory
WORKDIR /src

# Copy the project files
COPY package.json .
COPY yarn.lock .
COPY . .

# Install the dependencies
RUN yarn install

# Build the React project
RUN yarn build

# Expose port 3000 (or desired port)
EXPOSE 3000

# Command to start the web server
CMD ["yarn", "start"]