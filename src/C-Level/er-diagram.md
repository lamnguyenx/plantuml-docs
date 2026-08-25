---
title: Er Diagram — PlantUML Official Documentation
source: https://plantuml.com/er-diagram
description: Official documentation for PlantUML Er Diagram
---

# Entity Relationship Diagrams (Chen's notation)

## Minimal Example

### Vertical (by default)

```plantuml
@startchen

entity Person {
}
entity Location {
}
relationship Birthplace {
}

Person -N- Birthplace
Birthplace -1- Location

@endchen
```

### Horizontal

```plantuml
@startchen
left to right direction

entity Person {
}
entity Location {
}
relationship Birthplace {
}

Person -N- Birthplace
Birthplace -1- Location

@endchen
```

## Entities and attributes

```plantuml
@startchen

entity DIRECTOR {
  Name {
    Fname
    Lname
  }
  Born
  Died
  Age
}

entity MOVIE {
  Title
  Released
  Code
}

@endchen
```

```plantuml
@startchen

entity DIRECTOR {
  Number : INTEGER <<key>>
  Name {
    Fname : STRING
    Lname : STRING
  }
  Born : DATE
  Died : DATE
  Age : INTEGER
}

entity CUSTOMER {
  Number : INTEGER <<key>>
  Bonus : REAL <<derived>>
  Name : STRING <<multi>>
}

@endchen
```

## Relationships

```plantuml
@startchen

entity CUSTOMER {
  Number <<key>>
  Name
}

entity MOVIE {
  Code <<key>>
}

relationship RENTED_TO {
  Date
}

RENTED_TO =1= CUSTOMER
RENTED_TO -N- MOVIE

@endchen
```

```plantuml
@startchen

entity CUSTOMER {
  Number <<key>>
  Name
}

entity MOVIE {
  Code <<key>>
}

entity INVOICE {
  Number <<key>>
  Amount
}

relationship RENTED_TO {
  Date
}

RENTED_TO =1= CUSTOMER
RENTED_TO -N- MOVIE
RENTED_TO =1= INVOICE

relationship REFERENCES {
}

REFERENCES -1- MOVIE
REFERENCES -1- MOVIE

@endchen
```

### Structural constraints

```plantuml
@startchen

entity CUSTOMER {
  Number <<key>>
  Name
}

entity MOVIE {
  Code <<key>>
}

relationship RENTED_TO {
  Date
}

RENTED_TO -(1,N)- CUSTOMER
RENTED_TO -(0,1)- MOVIE

@endchen
```

## Identifying relationships

```plantuml
@startchen

entity PARENT {
  Number <<key>>
  Name
}

entity CHILD <<weak>> {
  Name <<key>>
  Age
}

relationship PARENT_OF <<identifying>> {
}

PARENT_OF -1- PARENT
PARENT_OF =N= CHILD

@endchen
```

## Aliases

```plantuml
@startchen

entity "Customer" as CUSTOMER {
  "customer number" as Number <<key>>
  "member bonus" as Bonus <<derived>>
  "first and last names" as Name <<multi>>
}

entity "Movie" as MOVIE {
  "barcode" as Code
}

relationship "was-rented-to" as RENTED_TO {
  "date rented" as Date
}

RENTED_TO -1- CUSTOMER
RENTED_TO -N- MOVIE

@endchen
```

## Subclasses and categories

```plantuml
@startchen

entity CUSTOMER {
}

entity PARENT {
}

entity MEMBER {
}

CUSTOMER ->- PARENT
MEMBER -<- CUSTOMER

@endchen
```

```plantuml
@startchen

entity CUSTOMER {
}

entity PARENT {
}

entity MEMBER {
}

CUSTOMER ->- o { PARENT, MEMBER }

entity CHILD {
}

entity TODDLER {
}

entity PRIMARY_AGE {
}

entity TEENAGER {
}

CHILD =>= d { TODDLER, PRIMARY_AGE, TEENAGER }

@endchen
```

```plantuml
@startchen

entity CUSTOMER {
}

entity EMPLOYEE {
}

entity PERSON {
}

PERSON ->- U { CUSTOMER, EMPLOYEE }

@endchen
```

## Complex Example

```plantuml
@startchen movies
<style>
.red {
BackGroundColor Red
FontColor White
}
.blue {
BackGroundColor Blue
FontColor White
}
</style>

entity "Director" as DIRECTOR {
"No." as Number <<key>>
Name {
Fname
Lname
}
Born : DATE
Died<<red>>
Age<<blue>>
}

entity "Customer" as CUSTOMER {
Number <<key>>
Bonus <<derived>>
Name <<multi>>
}

entity "Movie" as MOVIE {
Code
}

relationship "was-rented-to" as RENTED_TO {
Date
}

RENTED_TO -1- CUSTOMER
RENTED_TO -N- MOVIE
RENTED_TO -(N,M)- DIRECTOR

entity "Parent" as PARENT {
}

entity "Member" as MEMBER {
}

CUSTOMER ->- PARENT
MEMBER -<- CUSTOMER

entity "Kid" as CHILD <<weak>> {
Name <<key>>
}

relationship "is-parent-of" as PARENT_OF <<identifying>> {
}

PARENT_OF -1- PARENT
PARENT_OF =N= CHILD

entity "Little Kid" as TODDLER {
FavoriteToy
}

entity "Primary-Aged Kid" as PRIMARY_AGE {
FavoriteColor
}

entity "Teenager" as TEEN {
Hobby
}

CHILD =>= d { TODDLER, PRIMARY_AGE, TEEN }

entity "Human" as PERSON {
}

PERSON ->- U { CUSTOMER, DIRECTOR }
@endchen
```
