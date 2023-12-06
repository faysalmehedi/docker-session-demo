#
# Build STAGE
#

FROM maven:3.9.5-eclipse-temurin-8 AS build-stage
WORKDIR /app
COPY . .
RUN mvn -f pom.xml clean package

#
# PACKAGE STAGE
#

FROM eclipse-temurin:8
WORKDIR /app
COPY --from=build-stage /app/target/netflix-eureka-naming-server-0.0.1-SNAPSHOT.jar /app/netflix-eureka-naming-server-0.0.1-SNAPSHOT.jar
EXPOSE 8761
CMD ["java","-jar","/app/netflix-eureka-naming-server-0.0.1-SNAPSHOT.jar"]

