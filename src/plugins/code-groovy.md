---
title: Code Groovy — PlantUML Official Documentation
source: https://plantuml.com/code-groovy
description: Official documentation for PlantUML Code Groovy
---

# Groovy API Client Code

PlantUML Plugins Groovy Â Â Â Â
```
println net.sourceforge.plantuml.version.Version.version() println
net.sourceforge.plantuml.code.TranscoderUtil.getDefaultTranscoder().encode("Bob->Alice:hello")
```
```
s = new net.sourceforge.plantuml.SourceStringReader("@startuml\nBob->Alice:hello\n@enduml")
FileOutputStream file = new FileOutputStream("c:/testGroovy2.png")
s.generateImage(file);
file.close()
```
