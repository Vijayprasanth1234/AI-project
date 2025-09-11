FROM node:18-alpine
WORKDIR /usr/src/app
COPY frontend/package.json ./package.json
RUN npm install --legacy-peer-deps
COPY frontend/ ./
EXPOSE 3000
CMD ["npm", "start"]
