# Use the official Node.js 20 image as the base
FROM node:20

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json to leverage caching
COPY package*.json ./

# Install only production dependencies
RUN npm install --production

# Copy the rest of the project files to the container
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to start the app
CMD ["node", "app.js"]
