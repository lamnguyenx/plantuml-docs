---
title: Smetana02 — PlantUML Official Documentation
source: https://plantuml.com/smetana02
description: Official documentation for PlantUML Smetana02
---

# Context of the Smetana project

PlantUML Advanced usage Smetana Version Â Â Â Â

- PlantUML has to create a new process for each diagram, (and communication with this new process could be source of bugs).
- Users have to install DOT on their system, in addition of Java.
- PlantUML is not fully portable.

## Using Smetana

```plantuml
@startuml
!pragma layout smetana
class Foo1

Foo1 --> Foo2
Foo1 --> Foo3
Foo1 ---> Foo4 : test 4
Foo1 ----> Foo5 : test 5

@enduml
```
```
java -jar plantuml.jar -Playout=smetana
```

[Ref. issue-582 ]

## Alternative layout engines
