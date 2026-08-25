---
title: Svg — PlantUML Official Documentation
source: https://plantuml.com/svg
description: Official documentation for PlantUML Svg
---

# Scalable Vector Graphics

PlantUML Advanced usage SVG Support

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
```puml
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
```puml
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
```puml
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

Interactive SVG is enabled with `!pragma svgInteractive true` inside the `@startuml ... @enduml` block (the value is a convention — any non-empty string works). PlantUML embeds a JavaScript bundle and CSS stylesheet directly into the SVG output, chosen by diagram type. No post-processing or external files are needed.

- QA-13350

### On Class, Object, UseCase or Deployment diagram

On these diagram types, interactions operate on elements connected by arrows/associations (internal `g.entity` and `g.link` elements):

- **Hover** (mouseover): the hovered element and its direct neighbors stay at full opacity; everything else dims. Moving the mouse away restores the diagram.
- **Click**: same as hover but *locked* — the selection stays highlighted after the mouse moves away. Click the same element again to clear.
- **Double-click**: highlights the *transitive closure* — the clicked element **and every other element reachable from it through any number of links** (the entire connected graph). Double-click again to clear.
- Pressing **`Escape`** clears the click selection without affecting the current hover highlight (hover and click are independent states).

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

- **Participant filter**: click a participant name or lifeline to highlight its messages in green (everything else dims). Click additional participants to filter by multiple lifelines — only messages touching all of them are highlighted. Click a selected participant again to remove it from the filter; when the set is empty the diagram is fully restored. If no message matches the selection, participants turn red instead.
- **Floating header**: a pin button (📌) appears in the participant header row. Click it to pin the header to the top of the viewport while scrolling. The pinned state persists in `localStorage` across page loads (requires HTTP hosting — `file://` storage is unreliable).

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
|||
Alice -> Bob : message 3
Alice -> Bob : message 4
Alice -> Bob : message 5

@enduml
```

### All diagram types — links and tooltips (native SVG, no JS needed)

- **Links**: `[[url label]]` on a participant, class, use case, message, or any other element wraps it in `<a href="url">` — clickable in the browser. Use skinparam `svgLinkTarget` to control the target (`_blank`, `_parent`, `_self`, `_top`).
- **Tooltips**: `[[url{tooltip} label]]` emits a `<title>tooltip</title>` inside the link — native browser hover tooltip.

## Option for SVG [ svgTitle , svgDesc ]

```plantuml
@startuml
!option svgTitle "This is the title"
!option svgDesc "This is the description"

alice -> bob: hello
@enduml
```
