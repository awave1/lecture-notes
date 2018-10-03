# Relational Model

**Objectives**

1. Formally define relations, tuples, domains, schema, and state
2. Specify integrity constraints on a database
3. Understand key constraints
4. Understand entity constraints
5. Understand referinrial constraints
6. How modifications can violate integrity constraints

## Relations

The relational Model of Data is based on the concept of **Relation**. Formal foundation provided by the theory of relations.

Informally, a **relation** looks like a **table** of values.

![lec03/01.png](cpsc471/img/lec03/01.png)

### Relations -- Mathematical Review

A set is unordored collection of unique elements. A multiset is an unordered collection of elements.

$`A \times B = \{<a, b> | a \in A, b \in B\}`$:

- Example $`A = \{1, 2\}`$ and $`B = \{a, b, c\}`$
- $`A \times B = \{<1, a>, <1, b>, <1, c>, <2, a>, <2, b>, <2, c>\}`$
- $`<a, b>`$ is ordered
- $`<1, a> \neq <a, 1>`$
- Hence, $`A \times B \neq B \times A`$, unless $`A = B`$

A relation $`R`$ from $`A`$ to $`B`$: $`R \subset A \times B`$:

- $`R`$ is a **set** of n-tuples

### Tables as Relations

![lec03/02.png](cpsc471/img/lec03/02.png)

## Schema

The **Scema** (or description) of a Relation:

- Denoted by $`R(A_1, A_2, ...A_n)`$

![03.png](cpsc471/img/lec03/03.png)
