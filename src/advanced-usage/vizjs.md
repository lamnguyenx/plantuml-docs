---
title: Vizjs — PlantUML Official Documentation
source: https://plantuml.com/vizjs
description: Official documentation for PlantUML Vizjs
---

# The context of VizJs

PlantUML Advanced usage VizJs Integration Â Â Â Â

- PlantUML has to create a new process for each diagram, (and communication with this new process could be source of bugs).
- Users have to install DOT on their system, in addition of Java.
- PlantUML is not fully portable.

## Using visjs

- vizjs : A Java library written by Andreas Studer that embed viz.js and call J2V8
- The corresponding J2V8 implementation for your OS:
- For Windows x86/64 bit: j2v8_win32_x86_64-3.1.6.jar
- For Linux x86: j2v8_linux_x86_64-3.1.6.jar
- For Mac OS: j2v8_macosx_x86_64-3.1.6.jar
```
@startuml
testdot
@enduml
```

## Limitations

## Alternative layout engines
