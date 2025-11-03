# ---- Build stage ----
FROM node:22-alpine AS build
WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install dependencies
RUN npm ci || npm install

# Copy source code
COPY . .

# Build the Vite project
RUN npm run build

# ---- Serve stage ----
FROM nginx:alpine

# Copy build output to nginx html directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for the container
EXPOSE 80

# Default Nginx command
CMD ["nginx", "-g", "daemon off;"]
