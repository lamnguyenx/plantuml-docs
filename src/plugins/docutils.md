---
title: Docutils — PlantUML Official Documentation
source: https://plantuml.com/docutils
description: Official documentation for PlantUML Docutils
---

# Docutils (Install)

PlantUML Plugins Docutils Â Â Â Â

1. Replace/patch your docutils distribution with the files in src/
2. See usage examples in usage/ including how to setup defaults PlantUML

## Usage
```
.. uml::

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoWork
activate A
```
```
.. uml:: uml2/myDiagram123

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoMoreWork
activate A
```
