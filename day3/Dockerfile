# ARG DEMO=node:lts-alpine3.23:latest

# FROM ${DEMO}
FROM node:lts-alpine3.23    

LABEL maintainer="Ansari mantahsa" \
      description="for thestin g the docker images " 

ENV APP_NAME='demo' \
    PORT=3000

WORKDIR /demo  


COPY package*.json /demo
RUN npm install \
    npm audit fix --force \
    npm install react-scripts --save

COPY . /demo

EXPOSE 3000

CMD ["npm","start"]






