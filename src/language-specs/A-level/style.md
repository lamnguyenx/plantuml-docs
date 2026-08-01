---
title: Style — PlantUML Official Documentation
source: https://plantuml.com/style
description: Official documentation for PlantUML Style
---

# CSS Styles in PlantUML

## Getting Started

### Basic syntax and how to apply styles

```plantuml
@startuml
<style>
  /* Global style applied to all elements */
  element {
    BackGroundColor: #AAA;
  }

  /* Specific styles for a sequence diagram */
  sequenceDiagram {
    participant {
      FontColor: green;
      FontSize: 26;
      FontStyle: italic;
      LineColor: #E00;
    }
    arrow {
      FontColor: red;
      LineColor: blue;
    }
  }
</style>

participant Alice
participant Bob

Alice -> Bob : hello

@enduml
```

- The element selector applies a background color to all diagram elements.
- The sequenceDiagram block targets sequence diagrams specifically, allowing for more refined styling within that context.
- Within the sequenceDiagram block, the participant and arrow selectors define styles for participants and arrows respectively.

### Global vs. element-specific styles

- Definition : Rules applied to the element selector affect every part of your diagram.
- Usage : Use global styles to set defaults, such as background colors, that should be consistent throughout your entire diagram.

- Definition : These styles are applied only to specified parts of the diagram, such as sequenceDiagram , participant , or arrow .
- Usage : This approach is useful when you need to customize only certain components of your diagram. For instance, if you want to highlight participants in a sequence diagram differently from other elements, you can define rules under the participant selector.

## Detailed property reference

### Typography

| Property | Description |
| FontName | Sets the font family for text elements. |
| FontColor | Sets the color of the text. |
| FontSize | Specifies the size of the text. |
| FontStyle | Defines the text style (e.g., bold, italic, normal). |

### Color and background

| Property | Description |
| BackGroundColor | Sets the background color of an element. |
| HyperLinkColor | Sets the color used for hyperlinks. |

### Borders and corners

| Property | Description |
| RoundCorner | Sets the radius for rounding the corners of elements. |
| DiagonalCorner | Applies a diagonal cut effect to element corners. |
| LineColor | Specifies the color of lines or borders. |
| LineThickness | Sets the thickness of lines or borders. |
| LineStyle | Defines the line style (solid, dashed, dotted, etc.). |

### Spacing and sizing

| Property | Description |
| Padding | Sets the internal spacing within an element. |
| Margin | Defines the external spacing around an element. |
| MaximumWidth | Specifies the maximum width an element can occupy. |

### Additional visuals and effects

| Property | Description |
| Shadowing | Adds a shadow effect by specifying a numeric value for the shadow distance. |
| HyperlinkUnderlineStyle | Specifies the underline style for hyperlinks. |
| HyperlinkUnderlineThickness | Specifies the thickness of the hyperlink underline. |
| HorizontalAlignment | Aligns content horizontally (left, center, or right). |

## Advanced Examples

### Example 1: sequence â combining multiple styles

```plantuml
@startuml
<style>
  /* Global style for all elements */
  element {
    BackGroundColor: #f5f5f5;
  }

  /* Specific styles for sequence diagrams */
  sequenceDiagram {
    participant {
      FontColor: darkblue;
      FontSize: 24;
      FontStyle: bold;
    }
    arrow {
      LineColor: #008000;
      FontColor: #006400;
    }
  }
</style>

participant Alice
participant Bob

Alice -> Bob : Combined Styles Example

@enduml
```

### Example 2: sequence â using selectors for custom styles

```plantuml
@startuml
<style>
  sequenceDiagram {
    .primary {
      FontColor: darkred;
      FontSize: 16;
      FontStyle: bold;
      BackGroundColor: #ffe6e6;
    }
    .secondary {
      FontColor: gray;
      FontSize: 14;
      FontStyle: italic;
      BackGroundColor: #f0f0f0;
    }
    arrow {
      LineColor: #ff6600;
      FontColor: #0000ff;
    }
  }
</style>

participant "Alice (Primary)" as Alice <<primary>>
participant "Bob (Secondary)" as Bob <<secondary>>

Alice -> Bob : Message

@enduml
```

### Example 3: classes â custom class style

```plantuml
@startuml
<style>
classDiagram {
    RoundCorner 15
    .mystyle {
        RoundCorner 5
        BackgroundColor cyan
        FontStyle Bold
        FontColor red
    }
}
</style>
class Alice <<<mystyle>>>
@enduml
```

- All classes have a default round corner of 15.
- The custom class .mystyle further customizes the appearance of the class Alice .

### Example 4: classes â multiple custom class styles

```plantuml
@startuml
<style>
classDiagram {
    arrow {
        LineColor blue
    }
    class {
        BackgroundColor #00ff00  
    }
    .x {
        BackgroundColor #00ffff  
    }
    .y {
        BackgroundColor #ff0000  
    }
}
</style>
class Customer <<x>>
class Order <<y>>
class Product
Customer --> Order
@enduml
```

- The default background color for classes is bright green ( #00ff00 ).
- The custom selectors .x and .y override the background colors to cyan and red respectively.

### Example 5: classes â visibility icon styling

```plantuml
@startuml
<style>
visibilityIcon {
  protected {
    LineColor DarkGoldenRod
    BackgroundColor DarkGoldenRod
  }
}
</style>

class TaskRunner {
  --
  {method} + executeTask
  {method} # executeForAllSubtasks
}
class MetadataInspector {
  --
  {method} # inspectClassMetadata
  {method} # inspectFooterMetadata
}
TaskRunner <|-- MetadataInspector
@enduml
```

- The visibilityIcon style targets protected members, setting both their line and background colors to DarkGoldenRod.
- This helps visually distinguish protected elements in the diagram.

### Example 6: objects â global and specific styling

```plantuml
@startuml
<style>
root {
  FontColor Red
  BackgroundColor palegreen
}
objectDiagram {
  object {
      FontColor blue
      BackgroundColor yellow
  }
}
</style>

object PaymentService
object Customer {
  name = "John Doe"
  id = 456
}

PaymentService -> Customer
@enduml
```

- The root style applies a red font color and a pale green background to the diagramâs root elements.
- The style defined in objectDiagram targets only the objects.

### Example 7: mindmap â basic node styling

```plantuml
@startmindmap
<style>
node {
    Padding 10
    HorizontalAlignment center
    LineColor blue
    LineThickness 3.0
    BackgroundColor gold
    RoundCorner 40
}
</style>

* Renovation project
** Planning
*** Budget & deadlines
** Execution
*** Team coordination
*** Material selection
** Monitoring
*** Quality control
*** Managing unforeseen events

@endmindmap
```

- All nodes are styled with padding, centered text, blue borders (thickness 3.0), a gold background, and rounded corners (radius 40).

### Example 8: mindmap â detailed node styling with width constraints

```plantuml
@startmindmap
<style>
node {
    Padding 12
    Margin 3
    HorizontalAlignment center
    LineColor blue
    LineThickness 3.0
    BackgroundColor gold
    RoundCorner 40
    MaximumWidth 100
}

rootNode {
    LineStyle 8.0-3.0
    LineColor red
    BackgroundColor white
    LineThickness 1.0
    RoundCorner 0
    Shadowing 0.0
}

leafNode {
    LineColor gold
    RoundCorner 0
    Padding 3
}

arrow {
    LineStyle 4
    LineThickness 0.5
    LineColor green
}
</style>

* Hi =)
    * sometimes i have node in which i want to write a long text
        * this results in really huge diagram
            * of course, i can explicitly split with a\nnew line
            * but it could be cool if PlantUML was able to split long lines automatically, maybe with an option to specify the maximum width of a node
@endmindmap
```

- The detailed styling controls spacing and maximum width to prevent overly extended diagrams.

### Example 9: wbs â depth-based styling

```plantuml
@startwbs
<style>
wbsDiagram {
  :depth(1) {
    // Targets top-level nodes like America and Europe
    BackGroundColor white
  }
  
  .americaStyle * {
      FontColor red
      :depth(2) {
        BackGroundColor blue
      }
  }
}
</style>

* World
** America <<americaStyle>>
*** Canada
*** Mexico
*** USA
**** Texas
** Europe <<europeStyle>>
*** England
*** Germany
*** Spain
@endwbs
```

- The styling varies according to the node's depth and assigned class, allowing for clear hierarchical visualization.

### Example 10: json â styling a json diagram

```plantuml
@startjson
<style>
jsonDiagram {
  node {
    FontName Helvetica
    FontColor Coral
    FontSize 12
    FontStyle bold
    BackGroundColor Khaki
    LineColor lightblue
  }
  arrow {
    BackGroundColor lightblue
    LineColor green
  }
}
</style>
{
    "quiz": {
        "question": "2+2?",
        "options": ["3", "4", "5"],
        "answer": "4"
    }
}
@endjson
```

- The node style sets the font to Helvetica, Coral text with bold style at size 12, a Khaki background, and a light blue border.
- Arrows are styled with a light blue background and green line.

### Example 11: arrows â customizing with class selectors

```plantuml
@startuml
<style>
arrow {
  LineColor #Green
  FontColor #Green
  LineStyle 10-5
  
  .critical {
      LineColor #Red
      FontColor #Red
  }
  .supporting {
      LineColor #Blue
  }
}
</style>

[Order_Service]

Order_Service --> Payment_Processor <<critical>> : Handles payment validation
Order_Service --> Inventory_Service <<supporting>> : Checks stock levels
@enduml
```

- The default arrow style is set to green.
- The .critical class changes arrows to red, while the .supporting class changes them to blue.

### Example 12: timing â class-based color customization

```plantuml
@startuml
<style>
timingDiagram {
  .bluecolor {
    BackGroundColor LightSkyBlue
  }
}
</style>
concise "LR" as LR <<bluecolor>> #FFB6C1
concise "ST" as ST

LR is AtPlace
ST is AtLoad

@LR
0 is Lowering
100 is Lowered
350 is Releasing
 
@ST
200 is Moving
@enduml
```

- The .bluecolor class gives the element a blue background, combined here with a red font color.

### Example 13: timing â timeline customization

```plantuml
@startuml
<style>
timingDiagram {
  timeline {
    FontColor red
    FontSize 10
    FontStyle italic
    LineColor red
    LineThickness 2
    LineStyle 4-4
    BackgroundColor pink
  }
}
</style>

clock   "Clock_0"   as C0 with period 50
binary  "Binary"  as B
concise "Concise" as C
robust  "Robust"  as R
@0
C is Idle
R is Idle
@100
B is high
C is Waiting
R is Processing
@300
R is Waiting
@enduml
```

- The timeline is styled with red italic text (size 10) and a pink background, with red lines drawn in a specific style and thickness for improved clarity.

### Example 14: gantt â task status styling

```plantuml
@startgantt
<style>
ganttDiagram {
  task {
    BackGroundColor GreenYellow
    LineColor Green 
    unstarted {
      BackGroundColor Fuchsia 
    }
  }
  undone {
    BackGroundColor red
  }
}
</style>

[Prototype Design] lasts 7 days
[Functional Testing] lasts 4 days
[Performance Testing] lasts 4 days

[Functional Testing] starts at [Prototype Design]'s end
[Performance Testing] starts at [Prototype Design]'s end

[Functional Testing] is 0% complete
[Performance Testing] is 80% complete
@endgantt
```

- Different background colors help quickly identify the status of each task in the timeline.

## Conclusion
