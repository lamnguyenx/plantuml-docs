---
title: Svg — PlantUML Official Documentation
source: https://plantuml.com/svg
description: Official documentation for PlantUML Svg
---

# Scalable Vector Graphics

PlantUML Advanced usage SVG Support Â Â Â Â

### Command Line

### Ant Task
```
<target name="main">
  <plantuml dir="./src" format="svg" />
</target>
```

### Java

## Specific Skin Parameters for SVG

### svgLinkTarget

- _blank : Opens the link in a new window or tab
- _parent : Opens the link in the parent frame
- _self : Opens the link in the same frame where it was clicked (default setting)
- _top : Opens the link in the full body of the window

### pathHoverColor
```
@startuml
skinparam pathHoverColor green
class Foo2 [[http://www.yahoo.com/Foo2]] {
  +double[] x
  +double y
}
Foo2 --> Foo3
@enduml
```

[Reference: QA-5453 ]

### svgDimensionStyle
```
@startuml
skinparam svgDimensionStyle false

component a {
}
component b {
}
a -(0- b
@enduml
```

[Reference QA-7334 ]

## svgSize Pragma

### Using the svgSize Pragma Directive

- !pragma svgSize <U+hhhhh> XX
- !pragma svgSize <U+hhhhh> I

#### Example Usage
```
@startuml
!pragma svgSize <U+1F610> XX

test: text <U+1F610>
test_size45: text <size:45><U+1F610>
@enduml
```

### Command-Line Options

- Enclose the argument in quotes, especially when it contains spaces.
- Use this option multiple times in a single command, if necessary.

#### Example
```
java -jar plantuml.jar "-PsvgSize=<U+1F610> XX" "-PsvgSize=<U+1F611> I" -Tsvg <file.puml>
```

### References

- Forum QA-12550
- GitHub Issue 582

## Interactive SVG

- When you click on a diagram element, all other elements that are not connected to it, are dimmed out.
- When you click the same element twice, all elements are restored to their original visibility.

- QA-13350

### On Class, Object, UseCase or Deployment diagram

```plantuml
@startuml
!pragma svgInteractive true

package P {
  A-->B
  A-->C
}
C-->D
D-->A
E-->F
F-->B
B-->G
@enduml
```

```plantuml
@startuml
!pragma svginteractive true
left to right direction
skinparam actorStyle awesome

actor Guest as g
package Professional {
  actor Chef as c
  actor "Food Critic" as fc
}
package Restaurant {
  usecase "Eat Food" as UC1
  usecase "Pay for Food" as UC2
  usecase "Drink" as UC3
  usecase "Review" as UC4
  usecase "Cook" as UC5
}

g --> UC1
g --> UC2
g --> UC3

fc -u-> UC4
c -u-> UC5
@enduml
```

### On Sequence diagram

```plantuml
@startuml
!pragma svginteractive true


Alice -> Bob: Authentication Request

alt successful case

    Bob -> Alice: Authentication Accepted

else some kind of failure

    Bob -> Alice: Authentication Failure
    group My own label
    Alice -> Log : Log attack start
        loop 1000 times
            Alice -> Bob: DNS Attack
        end
    Alice -> Log : Log attack end
    end

else Another type of failure

   Bob -> Alice: Please repeat

end
|||
Alice -> Bob : message 1
Alice -> Bob : message 2
Alice -> Bob : message 3
Alice -> Bob : message 4
Alice -> Bob : message 5
Alice -> Bob : message 6
Alice -> Bob : message 7
Alice -> Bob : message 8
Alice -> Bob : message 9
|||
Alice -> Bob : message 10
Alice -> Bob : message 11
Alice -> Bob : message 12
Alice -> Bob : message 13
Alice -> Bob : message 14
Alice -> Bob : message 15
Alice -> Bob : message 16
Alice -> Bob : message 17
Alice -> Bob : message 18
Alice -> Bob : message 19
|||
Alice -> Bob : message 20
Alice -> Bob : message 21
Alice -> Bob : message 22
Alice -> Bob : message 23
Alice -> Bob : message 24
Alice -> Bob : message 25
Alice -> Bob : message 26
Alice -> Bob : message 27
Alice -> Bob : message 28
Alice -> Bob : message 29
@enduml
```

## Option for SVG [ svgTitle , svgDesc ]

```plantuml
@startuml
!option svgTitle "This is the title"
!option svgDesc "This is the description"

alice -> bob: hello
@enduml
```
