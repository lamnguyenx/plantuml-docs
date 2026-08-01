---
title: Starting — PlantUML Official Documentation
source: https://plantuml.com/starting
description: Official documentation for PlantUML Starting
---

# Quick Start Guide to PlantUML

PlantUML News and information PlantUML for the impatient Â Â Â Â

## Local Installation Procedure

- Check if Java is already installed: java -version .

- The minimum recommended version is Java 11 ; however, we provide a special build compatible with Java 8 if you cannot migrate yet. Please upgrade to Java 11 or later to benefit from security and performance improvements.

- If not installed, download and install it from the official Java website or through package managers like apt for Ubuntu, brew for macOS, etc.

- Linux : You'll find mode information here about GraphViz installation
- Windows : A compiled version of GraphViz is embedded within PlantUML, eliminating the need for a separate installation. However, if needed, you can acquire a standalone version here

## Command Line Operations
```
@startuml
Alice -> Bob: test
@enduml
```
```
java -jar plantuml.jar sequenceDiagram.txt
```
```
java -jar plantuml.jar -gui
```

## Using Docker

### Instructions

1. Pull the PlantUML Docker Image
```
docker pull plantuml/plantuml-server:jetty
```
```
docker run -d -p 8080:8080 plantuml/plantuml-server:jetty
```

- -d : Runs the container in detached mode.
- -p 8080:8080 : Maps port 8080 of the container to port 8080 on your host machine.

- Type or paste your PlantUML code into the provided text area.
- As you type or modify the code, the diagram on the right should update automatically.
```
docker ps
```
```
docker stop [CONTAINER_ID]
```
```
docker rm [CONTAINER_ID]
```

## PlantUML Integration Capabilities

- IDE Integration :

- Version Control System Integration :

- Documentation and Wiki Tools :

- Continuous Integration/Continuous Deployment (CI/CD) :

- Browser Extensions :

- Other Tools :

- Cloud Platforms :

- Docker :

## PlantUML Language Reference Guide
