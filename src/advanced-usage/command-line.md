---
title: Command Line — PlantUML Official Documentation
source: https://plantuml.com/command-line
description: Official documentation for PlantUML Command Line
---

# Command line

PlantUML Advanced usage Command line Â Â Â Â
```
java -jar plantuml.jar file1 file2 file3
```
```
java -jar plantuml.jar "c:/directory1" "c:/directory2"
```
```
docker run ghcr.io/plantuml/plantuml
```

## New command-line interface (beta)

- The new options follow consistent naming and structure.
- The legacy options will still be supported for a transition period, but they will no longer be documented.
```
plantuml - generate diagrams from plain text

Usage:
  java -jar plantuml.jar [options] [file|dir]...
  java -jar plantuml.jar [options] --gui

Description:
  Process PlantUML sources from files, directories (optionally recursive), or stdin (-pipe).

Wildcards (for files/dirs):
  *   any characters except '/' and '\'
  ?   exactly one character except '/' and '\'
  **  any characters across directories (recursive)
  Tip: quote patterns to avoid shell expansion (e.g., "**/*.puml").

General:
 -h, --help ....................... Show this help
     --help-more .................. Show extended help (advanced options)
     --version .................... Show PlantUML and Java version
     --author ..................... Show information about PlantUML authors
     --gui ........................ Launch the graphical user interface
     --dark-mode .................. Render diagrams in dark mode
 -v, --verbose .................... Enable verbose logging
     --duration ................... Print total processing time
     --progress-bar ............... Show a textual progress bar
     --splash-screen .............. Show splash screen with progress bar
     --check-graphviz ............. Check Graphviz installation
     --http-server[:<port>] ....... Start internal HTTP server for rendering (default port : 4242)

Input & preprocessing:
 -p, --pipe ....................... Read source from stdin, write result to stdout
 -D<var>=<value>,
     --define <VAR>=<value> ....... Define a preprocessing variable (equivalent to '!define <var> <value>')
 -I<file>,
     --include <file> ............. Include external file (as with '!include <file>')
 -P<key>=<value>,
     --pragma <key>=<value> ....... Set pragma (equivalent to '!pragma <key> <value>')
 -S<key>=<value>,
     --skinparam <key>=<value> .... Set skin parameter (equivalent to 'skinparam <key> <value>')
     --theme <name> ............... Apply a theme
     --config <file> .............. Specify configuration file
     --charset <name> ............. Use a specific input charset

Execution control:
     --check-syntax ............... Check diagram syntax without generating images
     --stop-on-error .............. Stop at the first syntax error
     --check-before-run ........... Pre-check syntax of all inputs and stop faster on error
     --no-error-image ............. Do not generate error images for diagrams with syntax errors
     --graphviz-timeout <seconds>   Set Graphviz processing timeout (in seconds)
     --threads <n|auto> ........... Use <n> threads for processing  (auto = available processors)

Metadata & assets:
     --extract-source ............. Extract embedded PlantUML source from PNG or SVG metadata
     --disable-metadata ........... Do not include metadata in generated files
     --skip-fresh ................. Skip PNG/SVG files that are already up-to-date (using metadata)
     --sprite <4|8|16[z]> <file> .. Encode a sprite definition from an image file
     --obfuscate .................. Obfuscate diagram texts for secure sharing
     --encode-url ................. Generate an encoded PlantUML URL from a source file
     --decode-url <string> ........ Decode a PlantUML encoded URL back to its source
     --list-keywords .............. Print the list of PlantUML language keywords
     --dot-path <path-to-dot-exe>   Specify the path to the Graphviz 'dot' executable
     --ftp-server ................. Start a local FTP server for diagram rendering (rarely used)

Output control:
     --output-dir <dir> ........... Generate output files in the specified directory
     --overwrite .................. Allow overwriting of read-only output files
     --exclude <pattern> .......... Exclude input files matching the given pattern

Output format (choose one):
     --format <name>, -f <name> ... Set the output format for generated diagrams
                                    (e.g. png, svg, pdf, eps, latex, txt, utxt)

Available formats:
     --eps ........................ Generate images in EPS format
     --html ....................... Generate HTML files for class diagrams
     --latex ...................... Generate LaTeX/TikZ output
     --latex-nopreamble ........... Generate LaTeX/TikZ output without preamble
     --pdf ........................ Generate PDF images
     --png ........................ Generate PNG images (default)
     --scxml ...................... Generate SCXML files for state diagrams
     --svg ........................ Generate SVG images
     --txt ........................ Generate ASCII art diagrams
     --utxt ....................... Generate ASCII art diagrams using Unicode characters
     --vdx ........................ Generate VDX files
     --xmi ........................ Generate XMI files for class diagrams
     -preproc ..................... Output preprocessor text of diagrams

Statistics:
     --disable-stats .............. Disable statistics collection (default behavior)
     --enable-stats ............... Enable statistics collection
     --export-stats-html .......... Export collected statistics to an HTML report and exit
     --export-stats ............... Export collected statistics to a text report and exit
     --html-stats ................. Output general statistics in HTML format
     --xml-stats .................. Output general statistics in XML format
     --realtime-stats ............. Generate statistics in real time during processing
     --loop-stats ................. Continuously print usage statistics during execution


Examples:
  # Process all .puml recursively
  java -jar plantuml.jar "**/*.puml"

  # Check syntax only (CI)
  java -jar plantuml.jar --check-syntax src/diagrams

  # Read from stdin and write to stdout (SVG)
  cat diagram.puml | java -jar plantuml.jar --svg -pipe > out.svg

  # Encode a sprite from an image
  java -jar plantuml.jar --sprite 16z myicon.png

  # Use a define
  java -jar plantuml.jar -DAUTHOR=John diagram.puml

  # Change output directory
  java -jar plantuml.jar --format svg --output-dir out diagrams/

Exit codes:
  0   Success
  >0  Error (syntax error or processing failure)

See also:
  java -jar plantuml.jar --help-more
  Documentation: https://plantuml.com
```

## Wildcards

- For a single character, use ?
- For zero or more characters, use *
- For zero or more characters, (including / or \ ), use a double **
```
java -jar plantuml.jar "dummy*/*.cpp"
```
```
java -jar plantuml.jar "dummy*/**.cpp"
```

## Excluded files
```
java -jar plantuml.jar -x "**/common/**" -x "**/test/Test*" "dummy*/**/*.cpp"
```

## Output Directory
```
java -jar plantuml.jar -o "c:/outputPng" "c:/directory2"
```

- An absolute path will ensure that all images are output to a single, specific, directory.

- If you provide a relative path then the images is placed in that directory relative to the location of the input file , not the current directory (note: this applies even if the path begins with a . ). When Plantuml processes files from multiple directores then the corresponding directory structure is created under the computed output directory.

## Types of Output File

| Param name | Short param name | Output format | Comment |
| --png | -f png | PNG | Default |
| --svg | -f svg | SVG | Vector graphics â use for web and documentation(further details:SVG) |
| --eps | -f eps | EPS | PostScript/EPS output(further details:EPS) |
| --eps+ post-process | -f eps | EPS | Keeps EPS text as text â tool/version-specific(seeEPS) |
| --format pdf | -f pdf | PDF | PDF output(further details:PDF) |
| --format vdx | -f vdx | VDX | Microsoft Visio Document (if supported by your PlantUML build) |
| --format xmi | -f xmi | XMI | UML interchange (if supported)(seeXMI) |
| --format scxml | -f scxml | SCXML | State Chart XML (if supported) |
| --format html | -f html | HTML | Experimental/alpha â do not use in production without verifying support |
| --txt | -f txt | ATXT | ASCII art.(Further details:ASCII Art) |
| --utxt | -f utxt | UTXT | ASCII art using Unicode characters(Further details:ASCII Art) |
| --latex | -f latex | LATEX | LaTeX/TikZ output(further details:LaTeX) |
| --format latex+ opts | -f latex | LATEX | nopreamblebehaviour is version-specific â consult--help-more |
| --format braille | -f braille | PNG (braille) | Braille image(may be available in some builds; Ref.QA-4752) |
```
java -jar plantuml.jar yourdiagram.txt --txt
```

## Configuration File
```
java -jar plantuml.jar -config "./config.cfg" dir1
```

## Metadata

- If you do not want plantuml to save the diagram's source code in the generated PNG Metadata, you can during generation use the option -nometadata to disable this functionality (To NOT export metadata in PNG/SVG generated files).
- It is possible to retrieve this source with the -metadata option. This means that the PNG is almost "editable": you can post it on a corporate wiki where you cannot install plugins, and someone in the future can update the diagram by getting the metadata, editing and re-uploading again. Also, the diagram is stand-alone.
- Conversely, the -checkmetadata option checks whether the target PNG has the same source and if there are no changes, doesn't regenerate the PNG, thus saving all processing time. This allows you to run PlantUML on a whole folder (or tree with the -recursive option) incrementally.
```
java -jar plantuml.jar -metadata diagram.png > diagram.puml
```

## Exit code

## Standard report [stdrpt]

- none: two lines
- -stdrpt : single line
- -stdrpt:1 : verbose
- -stdrpt:2 : single line
```
@startuml
participant "Famous Bob" aass Bob
@enduml
```

### Without any option
```
java -jar plantuml.jar file1.pu
```

The error output is:
```
Error line 2 in file: file1.pu
Some diagram description contains errors
```

### -stdrpt option
```
java -jar plantuml.jar -stdrpt file1.pu
```

The error output is:
```
file1.pu:2:error:Syntax Error?
```

### -stdrpt:1 option
```
java -jar plantuml.jar -stdrpt:1 file1.pu
```

The error output is:
```
protocolVersion=1
status=ERROR
lineNumber=2
label=Syntax Error?
Error line 2 in file: file1.pu
Some diagram description contains errors
```

### -stdrpt:2 option (like -stdrpt)
```
java -jar plantuml.jar -stdrpt:2 file1.pu
```

The error output is:
```
file1.pu:2:error:Syntax Error?
```

## Standard Input & Output
```
cat somefile.puml | java -jar plantuml.jar -pipe > somefile.png
```
```
cat somefile.puml | java -jar plantuml.jar -pipemap > somefile.map
```
```
<map id="plantuml_map" name="plantuml_map">
<area shape="rect" id="id1" href="http://plantuml.com" title="http://plantuml.com"
      alt="" coords="1,8,88,44"/>
</map>
```

## Help
```
java -jar plantuml.jar --help-more
```
```
plantuml - generate diagrams from plain text

Usage:
  java -jar plantuml.jar [options] [file|dir]...
  java -jar plantuml.jar [options] --gui

Description:
  Process PlantUML sources from files, directories (optionally recursive), or stdin (-pipe).

Wildcards (for files/dirs):
  *   any characters except '/' and '\'
  ?   exactly one character except '/' and '\'
  **  any characters across directories (recursive)
  Tip: quote patterns to avoid shell expansion (e.g., "**/*.puml").

General:

General:
     --author ..................... Show information about PlantUML authors
     --check-graphviz ............. Check Graphviz installation
     --dark-mode .................. Render diagrams in dark mode
     --duration ................... Print total processing time
     --gui ........................ Launch the graphical user interface
 -h, --help ....................... Show help and usage information
     --help-more .................. Show extended help (advanced options)
     --http-server[:<port>] ....... Start internal HTTP server for rendering (default port : 8080)
     --progress-bar ............... Show a textual progress bar
     --splash-screen .............. Show splash screen with progress bar
 -v, --verbose .................... Enable verbose logging
     --version .................... Show PlantUML and Java version

Input & preprocessing:
     --charset <name> ............. Use a specific input charset
     --config <file> .............. Specify configuration file
 -d, --define <VAR>=<value> ....... Define a preprocessing variable (equivalent to '!define <var> <value>')
     --exclude <pattern> .......... Exclude input files matching the given pattern
 -I, --include <file> ............. Include external file (as with '!include <file>')
 -p, --pipe ....................... Read source from stdin, write result to stdout
 -P, --pragma <key>=<value> ....... Set pragma (equivalent to '!pragma <key> <value>')
     --skinparam <key>=<value> .... Set skin parameter (equivalent to 'skinparam <key> <value>')
     --theme <name> ............... Apply a theme

Execution control:
     --check-before-run ........... Pre-check syntax of all inputs and stop faster on error
     --check-syntax ............... Check diagram syntax without generating images
     --graphviz-timeout <seconds>   Set Graphviz processing timeout (in seconds)
     --ignore-startuml-filename ... Ignore '@startuml <name>' and always derive output filenames from input files
     --no-error-image ............. Do not generate error images for diagrams with syntax errors
     --stop-on-error .............. Stop at the first syntax error
     --threads <n|auto> ........... Use <n> threads for processing  (auto = available processors)

Metadata & assets:
     --decode-url <string> ........ Decode a PlantUML encoded URL back to its source
     --disable-metadata ........... Do not include metadata in generated files
     --dot-path <path-to-dot-exe>   Specify the path to the Graphviz 'dot' executable
     --encode-url ................. Generate an encoded PlantUML URL from a source file
     --extract-source ............. Extract embedded PlantUML source from PNG or SVG metadata
     --ftp-server ................. Start a local FTP server for diagram rendering (rarely used)
     --list-keywords .............. Print the list of PlantUML language keywords
     --skip-fresh ................. Skip PNG/SVG files that are already up-to-date (using metadata)
     --sprite <4|8|16[z]> <file> .. Encode a sprite definition from an image file

Output control:
     --output-dir <dir> ........... Generate output files in the specified directory
     --overwrite .................. Allow overwriting of read-only output files

Output format (choose one):
 -f, --format <name> .............. Set the output format for generated diagrams
                                    (e.g. png, svg, pdf, eps, latex, txt, utxt, obfuscate, preproc...)

Available formats:
     --eps ........................ Generate images in EPS format
     --html ....................... Generate HTML files for class diagrams
     --latex ...................... Generate LaTeX/TikZ output
     --latex-nopreamble ........... Generate LaTeX/TikZ output without preamble
     --obfuscate .................. Replace text in diagrams with obfuscated strings to share diagrams safely
     --pdf ........................ Generate PDF images
     --png ........................ Generate PNG images (default)
     --preproc .................... Generate the preprocessed source after applying !include, !define... (no rendering)
     --scxml ...................... Generate SCXML files for state diagrams
     --svg ........................ Generate SVG images
     --txt ........................ Generate ASCII art diagrams
     --utxt ....................... Generate ASCII art diagrams using Unicode characters
     --vdx ........................ Generate VDX files
     --xmi ........................ Generate XMI files for class diagrams

Statistics:
     --disable-stats .............. Disable statistics collection (default behavior)
     --enable-stats ............... Enable statistics collection
     --export-stats ............... Export collected statistics to a text report and exit
     --export-stats-html .......... Export collected statistics to an HTML report and exit
     --html-stats ................. Output general statistics in HTML format
     --loop-stats ................. Continuously print usage statistics during execution
     --realtime-stats ............. Generate statistics in real time during processing
     --xml-stats .................. Output general statistics in XML format


Examples:
  # Process all .puml recursively
  java -jar plantuml.jar "**/*.puml"

  # Check syntax only (CI)
  java -jar plantuml.jar --check-syntax src/diagrams

  # Read from stdin and write to stdout (SVG)
  cat diagram.puml | java -jar plantuml.jar --svg -pipe > out.svg

  # Encode a sprite from an image
  java -jar plantuml.jar --sprite 16z myicon.png

  # Use a define
  java -jar plantuml.jar -DAUTHOR=John diagram.puml

  # Change output directory
  java -jar plantuml.jar --format svg --output-dir out diagrams/

Exit codes:
  0    Success
  50   No file found
  100  No diagram found in file(s)
  200  Some diagrams have syntax errors

See also:
  java -jar plantuml.jar --help-more
  Documentation: https://plantuml.com
```
