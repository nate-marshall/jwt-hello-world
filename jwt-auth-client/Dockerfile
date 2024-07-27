# Use the official Node.js image for the LTS version
FROM node:18-slim

# Create and change to the app directory
WORKDIR /app

# Copy application dependency manifests to the container image
COPY package*.json ./

# Install production dependencies
RUN npm install

# Copy local code to the container image
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the web service on container startup
CMD [ "node", "server/server.js" ]
