---
title: Emacs — PlantUML Official Documentation
source: https://plantuml.com/emacs
description: Official documentation for PlantUML Emacs
---

# Emacs

PlantUML Plugins Emacs Â Â Â Â

## Org-Babel

### Napkin

## Emacs Org-Mode
```
(setq org-plantuml-jar-path (expand-file-name "/home/you/path/to/plantuml.jar"))
(add-to-list 'org-src-lang-modes '("plantuml" . plantuml))
(org-babel-do-load-languages 'org-babel-load-languages '((plantuml . t)))
```

4.) put some uml in your org file e.g.
```
#+begin_src plantuml :file my-diagram.png
title Authentication Sequence

Alice->Bob: Authentication Request
note right of Bob: Bob thinks about it
Bob->Alice: Authentication Response
#+end_src
```

5.) export e.g. with C-c C-e h o

### ob-plantuml.el (obsolete)
```
#+BEGIN_UML
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
#+END_UML
```

While the org file is exported to HTML or other formats, PlantUML is called to generate image and replace the block in place.
