FROM alpine/java:21-jdk

LABEL maintainer="Me"
LABEL description="this is my new image"

WORKDIR /main

COPY ./src/Main.java /main/Main.java

RUN javac Main.java

CMD ["java","Main"]