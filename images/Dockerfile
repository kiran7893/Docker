# Use a lightweight image to reduce build size and time
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package files to leverage Docker's caching mechanism
COPY package*.json ./

# Install dependencies with offline and audit-disabled options
RUN npm install --prefer-offline --no-audit --no-fund

# Copy the rest of the application files
COPY . .

# Expose the port used by the app
EXPOSE 3000

# Run the application
CMD ["node", "server.js"]
