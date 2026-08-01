---
title: Ant Task — PlantUML Official Documentation
source: https://plantuml.com/ant-task
description: Official documentation for PlantUML Ant Task
---

# Writing an Ant Task

PlantUML Plugins ANT task Â Â Â Â
```
<project name="OwnTaskExample" default="main" basedir=".">
<!-- task definition -->
<taskdef name="plantuml" classname="net.sourceforge.plantuml.ant.PlantUmlTask" classpath="plantuml.jar" />

<!-- process ./src files -->
<target name="main">
<plantuml dir="./src" />
</target>
</project>
```

## Output Directory
```
<!-- Put images in c:/images directory -->
<target name="main">
<plantuml dir="./src" output="c:/images" />
</target>
```

## Recurse through directories
```
<target name="main">
<plantuml output="d:/images" >
<fileset dir="c:/src">
<include name="**/*.java" />
<exclude name="**/*Test.java" />
</fileset>
</plantuml>
</target>
```

## SVG or EPS Support
```
<target name="main">
<plantuml dir="./src" format="svg" />
</target>
```

## Configuration file
```
<target name="main">
<plantuml dir="./src" config="./config.cfg" />
</target>
```

## Other parameters

| Parameter | Default | Description |
| nbthread | 1 | Number of thread for processing |
| graphvizDot |  | Path of the dot executable |
| format | png | Format for image generation: xmi, xmi:argo, xmi:start, eps, svg, txt, utxt |
| verbose | false | truefor more logs |
| config |  | File config to include before all diagrams |
| charset |  | Charset to use when reading files |
| output |  | Output directory for generated images |
| dir |  | Input directory to process (You can use<fileset>/<filelist>instead) |
| failonerror | false | trueto fail the build if some syntax error occurs |
| checkonly | false | trueif you want to only check the syntax of files without generating images |
| overwrite | false | trueif you want overwrite read-only files |
| enablestats | false | trueto enable statistics |
| htmlstats | false | trueto output general statistics in file plantuml-stats.html |
| xmlstats | false | trueto output general statistics in file plantuml-stats.xml |
| realtimestats | false | trueto generate statistics on the fly rather than at the end |
