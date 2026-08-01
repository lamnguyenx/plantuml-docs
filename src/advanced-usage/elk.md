---
title: Elk — PlantUML Official Documentation
source: https://plantuml.com/elk
description: Official documentation for PlantUML Elk
---

# Eclipse Layout Kernel

PlantUML Advanced usage Eclipse Layout Kernel Â Â Â Â

## Requirement

### From V1.2021.5 to V1.2024.6

### Since V1.2024.6

## Usage

```plantuml
@startuml
!pragma layout elk

package image {
	package color {
		class red
		class green
		
		red->green : red to green
	}
	package size {
		class big
		class small
	}
	class image1
	class image2
	image1 <|-- image2 
	
	size -> color : link between packages
}

class foo
class bar

foo -> bar : foo to bar
image1 "1" -> "*" bar
@enduml
```
```
java -jar plantuml.jar -Playout=elk
```

[Ref. GH-582 ]

## Alternative layout engines
