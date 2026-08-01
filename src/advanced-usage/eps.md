---
title: Eps — PlantUML Official Documentation
source: https://plantuml.com/eps
description: Official documentation for PlantUML Eps
---

# EPS

PlantUML Advanced usage EPS Support Â Â Â Â

## EPS Support

- You can enable it by using -teps flag at the command line .
- By default, EPS output generates text outlines (i.e., the shapes of letters). This may have some advantages if the EPS renderer does not have access to appropriate fonts.  However, this makes it impossible to select, search, or copy text from the generated diagrams.  If you want to keep the original text, use the -teps:text flag. [Ref. QA-3214 ]
- You can also specify format="eps" or format="eps:text" in the ant task definition .
```
<target name="main">
<plantuml dir="./src" format="eps" />
</target>
```
