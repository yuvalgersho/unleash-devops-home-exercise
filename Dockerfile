# build stage
FROM node:18-alpine AS build-stage
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM node:18-alpine AS production-stage
WORKDIR /usr/src/app
ENV PORT "3000"
ENV BUCKET_NAME "unleashbucket7727432"
COPY package*.json ./
RUN npm ci --only=production-stage
COPY --from=build-stage /usr/src/app/dist ./dist
CMD [ "node", "dist/index.js" ]
