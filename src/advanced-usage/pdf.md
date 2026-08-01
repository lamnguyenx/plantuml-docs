---
title: Pdf — PlantUML Official Documentation
source: https://plantuml.com/pdf
description: Official documentation for PlantUML Pdf
---

# PDF Support

PlantUML Advanced usage PDF Support Â Â Â Â

## Make it work

- avalon-framework-4.2.0.jar
- batik-all-1.7.jar
- commons-io-1.3.1.jar
- commons-logging-1.0.4.jar
- fop.jar
- xml-apis-ext-1.3.04.jar
- xmlgraphics-commons-1.4.jar
```
java -jar plantuml.jar -tpdf diagram.txt
```
```
<!-- task definition -->
<taskdef name="plantuml" classname="net.sourceforge.plantuml.ant.PlantUmlTask" classpath="plantuml.jar" />
<!-- process diagram.txt file -->
<target name="images">
<plantuml format="pdf">
<fileset file="diagram.txt" />
</plantuml>
</target>
```

## Installation of the new libraries on a Unix system
```
#!/usr/bin/env bash

# These libraries will have to go in the same location where plantuml.jar is
PLANT_UML_WITH_PATH=$(awk '{for (i=1; i<=NF; i++) if ($i=="-jar") print $(i+1)}' "$(which plantuml)")
PLANT_UML_DIR=$(dirname "$PLANT_UML_WITH_PATH")

mapfile -t FILES_TO_REMOVE < <(find "$PLANT_UML_DIR" -type f ! -name "plantuml.jar")

if (( ${#FILES_TO_REMOVE[@]} == 0 )); then
    echo "No files to remove."
    #exit 0
else
    echo "The following files will be removed:"
    printf '%s\n' "${FILES_TO_REMOVE[@]}"

    read -p "Do you want to continue? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        find "$PLANT_UML_DIR" -type f ! -name "plantuml.jar" -delete
        echo "Files removed."
    else
        echo "Operation cancelled."
        exit 0
    fi
fi

# plantuml.jar uses these exact filenames in its manifest Class-Path.
curl -fL -o "$PLANT_UML_DIR/batik-all-1.7.jar" https://repo1.maven.org/maven2/org/apache/xmlgraphics/batik-all/1.17/batik-all-1.17.jar
#curl -fL -o "$PLANT_UML_DIR/batik-rasterizer-1.17.jar" https://repo1.maven.org/maven2/org/apache/xmlgraphics/batik-rasterizer/1.17/batik-rasterizer-1.17.jar
curl -fL -o "$PLANT_UML_DIR/fop.jar" https://repo1.maven.org/maven2/org/apache/xmlgraphics/fop-transcoder-allinone/2.9/fop-transcoder-allinone-2.9.jar
curl -fL -o "$PLANT_UML_DIR/xmlgraphics-commons-1.4.jar" https://repo1.maven.org/maven2/org/apache/xmlgraphics/xmlgraphics-commons/2.9/xmlgraphics-commons-2.9.jar
curl -fL -o "$PLANT_UML_DIR/commons-io-1.3.1.jar" https://repo1.maven.org/maven2/commons-io/commons-io/2.15.1/commons-io-2.15.1.jar
curl -fL -o "$PLANT_UML_DIR/commons-logging-1.0.4.jar" https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
curl -fL -o "$PLANT_UML_DIR/xml-apis-ext-1.3.04.jar" https://repo1.maven.org/maven2/xml-apis/xml-apis-ext/1.3.04/xml-apis-ext-1.3.04.jar

ls -l "$PLANT_UML_DIR"/*.jar

echo "Script finished successfully."
```
```
chmod +x download_pdf_conversion_libs.sh
./download_pdf_conversion_libs.sh
plantuml -tpdf file_to_convert.wsd
```
