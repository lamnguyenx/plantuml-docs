---
title: Color — PlantUML Official Documentation
source: https://plantuml.com/color
description: Official documentation for PlantUML Color
---

# Colors

- with its standard name or CSS name
- using HEX value (6 digits) : #RRGGBB
- using HEX value (8 digits) with alpha compositing or RGBA color model : #RRGGBBaa
- using short HEX value (3 digits) : #RGB (so #ABC means #AABBCC )
- using very short HEX value (1 digits): #x which is a shortcut for #xxxxxx (so you get some gray)

```plantuml
@startgantt
[Activity1] lasts 5 days
[Activity2] lasts 5 days
[Activity1] is colored in White/Red
[Activity2] is colored in Silver/SeaGreen
[Activity1] -> [Activity2]
@endgantt
```

```plantuml
@startuml
actor Bob #Red/Yellow
actor Alice #FF0000/FFFF00
Alice -> Bob : hello
@enduml
```

## Color gradient

- | ,
- / ,
- \ , or
- -

## Automatic Font Color

### How It Works:

- The #? prefix defines a conditional color choice.
- Two colors follow, separated by a colon.
- The engine selects one based on the background:

```plantuml
@startuml
<style>
document {
  BackGroundColor darkblue
}
root {
  FontColor #?black:white
  LineColor white
}
</style>
alice -> bob : hello
@enduml
```

## Color with preprocessing

| Name | Description | Example | Return |
| %darken | Return a darken color of a given color with some ratio | %darken("red", 20) | #CC0000 |
| %is_dark | Check if a color is a dark one | %is_dark("#000000") | true |
| %is_light | Check if a color is a light one | %is_light("#000000") | false |
| %lighten | Return a lighten color of a given color with some ratio | %lighten("red", 20) | #CC3333 |
| %reverse_color | Reverse a color using RGB | %reverse_color("#FF7700") | #0088FF |
| %reverse_hsluv_color | Reverse a colorusing HSLuv | %reverse_hsluv_color("#FF7700") | #602800 |

## View colors in PlantUML

```plantuml
@startuml
colors
@enduml
```

```plantuml
@startuml
colors chocolate
@enduml
```

## Archimate colors

- Application
- Business
- Implementation
- Motivation
- Physical
- Strategy
- Technology

```plantuml
@startuml
skinparam minClassWidth 125
skinparam nodesep 10
skinparam ranksep 10

rectangle Application    #Application
rectangle Business       #Business
rectangle Implementation #Implementation
rectangle Motivation     #Motivation
rectangle Physical       #Physical
rectangle Strategy       #Strategy
rectangle Technology     #Technology
@enduml
```

## PlantUML colors

```plantuml
@startuml
skinparam minClassWidth 200
skinparam nodesep 10
skinparam ranksep 10

rectangle "ClassColor" {
rectangle "Class_C_Background\n #ADD1B2" #ADD1B2
rectangle "Class_N_Background\n #E3664A" #E3664A
rectangle "Class_A_Background\n #A9DCDF" #A9DCDF
rectangle "Class_I_Background\n #B4A7E5" #B4A7E5
rectangle "Class_E_Background\n #EB937F" #EB937F
}
rectangle "DefaultColor" {
rectangle "BackGroundColor_Default\n #FEFECE" #FEFECE
rectangle "LineColor_Default\n #A80036"       #A80036
rectangle "Legend_BackGroundColor\n #DDDDDD"   #DDDDDD
rectangle "//TBC//\n..."
}
@enduml
```
