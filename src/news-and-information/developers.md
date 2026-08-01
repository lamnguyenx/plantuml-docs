---
title: Developers — PlantUML Official Documentation
source: https://plantuml.com/developers
description: Official documentation for PlantUML Developers
---

# Language

PlantUML News and information Information for developers Â Â Â Â
```
java -jar plantuml.jar -language
```
```
;type
;10
abstract
actor
class
component
enum
interface
object
participant
state
usecase

;keyword
;43
@enduml
@startuml
activate
alt
[..]
up

;preprocessor
;6
!define
!endif
!ifdef
!ifndef
!include
!undef

;skinparameter
;145
ActivityArrowFontColor
ActivityArrowFontName
[..]
UsecaseStereotypeFontSize
UsecaseStereotypeFontStyle

;color
;140
AliceBlue
AntiqueWhite
Aqua
[..]
WhiteSmoke
Yellow
YellowGreen

;EOF
```

## Syntax check
```
type mytext.txt | java -jar plantuml.jar -syntax
```
```
Bob -> Alice : hello
```
```
SEQUENCE
(2 participants)
```
```
actor Bob
actor Bob
Bob -> Alice : hello
```
```
ERROR
2
Duplicate participant : Bob
```
