---
title: Api — PlantUML Official Documentation
source: https://plantuml.com/api
description: Official documentation for PlantUML Api
---

# Calling PlantUML from Java

PlantUML Plugins Calling PlantUML from Java Â Â Â Â

## PNG generation from a String
```
import net.sourceforge.plantuml.SourceStringReader;
OutputStream png = ...;
String source = "@startuml\n";
source += "Bob -> Alice : hello\n";
source += "@enduml\n";

SourceStringReader reader = new SourceStringReader(source);
// Write the first image to "png"
String desc = reader.outputImage(png).getDescription();
// Return a null string if no generation
```

## PNG generation from a File
```
File source = ...;
SourceFileReader reader = new SourceFileReader(source);
List<GeneratedImage> list = reader.getGeneratedImages();
// Generated files
File png = list.get(0).getPngFile();
```

## SVG generation from a String
```
String source = "@startuml\n";
source += "Bob -> Alice : hello\n";
source += "@enduml\n";

SourceStringReader reader = new SourceStringReader(source);
final ByteArrayOutputStream os = new ByteArrayOutputStream();
// Write the first image to "os"
String desc = reader.generateImage(os, new FileFormatOption(FileFormat.SVG));
os.close();

// The XML is stored into svg
final String svg = new String(os.toByteArray(), Charset.forName("UTF-8"));
```
