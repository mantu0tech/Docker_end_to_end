FROM  node:20-alpine

LABEL name="mantasha" 

ENV app-name="myquiz app"

WORKDIR /quiz

COPY *.json /quiz

RUN npm install \
    npm install react-scripts --save \
    npm audit fix --force 

COPY    . /quiz/

EXPOSE 3000

CMD [ "npm", "start" ]




