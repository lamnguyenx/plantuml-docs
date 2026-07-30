---
title: Regex — PlantUML Official Documentation
source: https://plantuml.com/regex
description: Official documentation for PlantUML Regex
---

# Visualizing Regex with PlantUML

## Introduction to Regex and Visualization Challenges

## Why PlantUML for Regex?

### Simplifying Complexity with Visualization

- Demystifying Regex Syntax: The visual representation breaks down the regex into comprehensible components, making it easier to understand each part of the expression.
- Enhancing Pattern Recognition: Visual diagrams allow users to identify repeating patterns and structures in regex, which might be missed in the textual form.
- Debugging and Optimization: By laying out the regex structure visually, PlantUML can aid in spotting redundancies and errors, facilitating more efficient pattern design.

### An Invaluable Tool for Learning and Collaboration

- For learners, visual diagrams serve as educational aids, simplifying the learning curve associated with regex syntax.
- In collaborative environments, visual representations can bridge the gap in understanding, ensuring that team members are on the same page regarding the logic and function of a regex pattern.

## Fundamentals of Regular Expressions

```plantuml
@startregex
title litteralText
abc
@endregex
```

## Character Classes and Sequences

### Shorthand Character Classes

```plantuml
@startregex
title shorthandCharacterClasses
\d\w\s
@endregex
```

### Literal Character Sequences

```plantuml
@startregex
title litteralCharacterSequence
\Qfoo\E
@endregex
```

### Character Ranges

```plantuml
@startregex
title range
[0-9]
@endregex
```

### Any Character

```plantuml
@startregex
title anyCharacter
.
@endregex
```

### Special Escapes

```plantuml
@startregex
title specialEscapes
\t\r\n\a\e\f
@endregex
```

## Descriptive Name and Language

### Without Descriptive Name (by default)

```plantuml
@startregex
!option useDescriptiveNames false

\d?\D+\w*\W{1,2}|\s.\S
@endregex
```

### With Descriptive Name

#### English (en)

```plantuml
@startregex
!option language en
!option useDescriptiveNames true

\d?\D+\w*\W{1,2}|\s.\S
@endregex
```

#### Deutsch (de)

```plantuml
@startregex
!option language de
!option useDescriptiveNames true

\d?\D+\w*\W{1,2}|\s.\S
@endregex
```

#### Japanese (ja)

```plantuml
@startregex
!option language ja
!option useDescriptiveNames true

\d?\D+\w*\W{1,2}|\s.\S
@endregex
```

### Octal and Unicode Escapes

```plantuml
@startregex
title octalEscapes
\0377\337
@endregex
```

```plantuml
@startregex
title unicodeEscapes
\uFFFF\x{FFFF}
@endregex
```

## Repetitions and Alternation

### Repetitions

#### Optional Repetition

```plantuml
@startregex
title optional
ab?
@endregex
```

#### Required Repetition

```plantuml
@startregex
title requiredRepetition
ab+
@endregex
```

#### Zero or More Repetitions

```plantuml
@startregex
title optionalRepetition
ab*
@endregex
```

#### Specified Range of Repetitions

```plantuml
@startregex
title rangeRepetition
ab{1,2}
@endregex
```

#### Minimum Number of Repetitions

```plantuml
@startregex
title minimumRepetition
ab{1}c{1,}
@endregex
```

#### Repetition Equivalence

```plantuml
@startregex
title repetitionEquivalance
a{0,1}b{1,} is the same as a?b+
@endregex
@enduml
```

### Alternation

```plantuml
@startregex
title alternation
a|b
@endregex
```

## Unicode

### Unicode Categories

- Letters ( \p{L} ) : Matches any letter from any language.
- Lowercase Letters ( \p{Ll} ) : Specifically matches lowercase letters.

```plantuml
@startregex
title unicodeCategories
letter \p{L}\p{Letter} lower \p{Ll}\p{Lowercase_letter}
@endregex
```

### Unicode Scripts

```plantuml
@startregex
title unicodeScripts
latin \p{Latin}
@endregex
```

### Unicode Blocks

```plantuml
@startregex
title unicodeBlocks
\p{InGeometric_Shapes}
@endregex
```
