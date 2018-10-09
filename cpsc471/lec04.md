# Mapping ER and EER to Relational Model

## ER to Relational Mappint

Mapping looks like this:
![01.png](cpsc471/img/lec04/01.png)

### Goals during mapping

- Preserve all information
  - that includes all attributes
- Maintainthe constraints to the extent possible
  - RM cannot preserve all constraints, such as:
    - cardinality, for example 1:10
    - Exhaustive classification into subtypes
- Minimize university data redundancy
- Minimize null values

## Step 1: Strong entity types

## Step 2: Weak entity types

For each weak entity type, _W_ in the ER schema with owner entity types _E1, E2,..., En_:

- Create a relation _Rel(W)_ & include all simple attributes of _W_ as attributes of _Rel(W)_.
- Also include _Ei.PK_ as foreign key attributes of _Rel(W)_
- The _Rel(W).PK_ = is the **combination of** _Ei.PK_ and the partial key of the weak entity type _W_ is any.

## Step 3: 1:1 Binary Relationship Types
