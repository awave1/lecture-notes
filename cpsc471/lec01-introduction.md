# Introduction

> Required reading: Ch.1 & 2

## Objectives
* Describe basic DB terminology, functionality, and types of users
* Entretrain the main characteristics of the DB approach
* Entertain the advantages of the DB approach
* Describe what a data model is
* Differentiate between a DB schema and set (instance)
* Understand the three-schema architecture
* Discuss and differentiate between centralized and distributed DB architectures

## Types of Databases and Database Applications
Traditional Applications:
- Numeric and Textual Databases
- Focus of this course

**More recent applications**
- Multimedia DBs
- GIS (Geographic Information Systems)
- Biological
- Data warehouses
- Mobil
- Real-time and active DBs

### Recent Developments
* Social networks capture a lot of data
* Search Engines collect their own repository of web pages for searching purposes
* Big Dat astorage systems involving large clusters
* NOSQL (Not Only SQL) systems
* Cloud: hude gata centers using thousands of machines

## Basic Definitions
* **Database** - a collection of related data.
* **Data** - known facts that can be recorded and have an implicit meaning. Not any data has meaning. Need to store meaningful data
* **Mini-world** - some part of the real world about which data is stored in a database
* **Database Managment System (DBMS)** - a software package to facilitate the creation and maintenance of a computerized database.
* **Database System** - the DBMS software together with the **data itself**. Sometimes the applications are also included.

### Simplified database system environment
`@TODO: add image`
![Simplified database system environment]('./img/lec01/simplified_db_sys_env.png')

## Typical DBMS Functionality
The first thing is to **define** a database. **Define** a particular database in terms of its data types, structures, and constraints. The next step is to **populate** it. **Populate** the initial database contents on a secondary storage medium. Then, the database can be **manipulated**. To **manipulate** the database means; *Retrieval*: quering, generating reports, *Modification*: insertions, deletions, and updates to its content. **Processing** and **sharing** by a set of concurent users and application programs - yet, keeping all data valid and consistent (preventing racing conditions).

### Application activities againsts a database
Applications can interact with a database by generating:
- **Queries**: that access different parts of dta and formulate the result of a request.
- **Transactions**: that may read some data and "updata" certain values or generate new data and store that in the database. It's an atomic operation, transaction has to succeed completely or fail completely, not partially. (it appears as if it is atomic)

Applications must not allow unauthorized users to access data. They also must keep up with chainging user requirements against the database.

### Additional DBMS Functionality
**DBMS** may additionally provide:
- Protetction or Security measures to prevent unauthorized access
- "Active" processing to take internal actions on data
- Presentation and Visualization of data
- Maintenance of the database and associated programs over the lifetime

#### Example of a Database (with a conceptual data model)
* Mini-world for example: a part of a `UNIVERSITY` environment.
* Some mini-worlds entities
*   `STUDENTs`
*   `COURSEs`
*   `SECTIONs` of `COURSEs`
*   (academic) `DEPARTMENTs`
*   `INSTRUCTORs`

**Relationships**:
- `SECTIONs` **are of specific** `COURSEs`
- `STUDENTs` **take** `SECTIONs`
- `COURSEs` **have prerequisite** `COURSEs`
- `INSTRUCTORs` **teach** `SECTIONs`
- `COURSEs` **are offered by** `DEPARTMENTs`
- `STUDENTs` **major in** `DEPARTMENTs`

**Example of a simple databases**:
**`COURSE`**:

|`course_name`         |`course_number`|`credit_hours`|`department`|
|----------------------|:-------------:|:------------:|:----------:|
| Intro to CS          | CS1310        | 4            | CS         |
| Data Structures      | CS1310        | 4            | CS         |
| Discrete Mathematics | CS1310        | 3            | MATH       |
| Datbase              | CS1310        | 3            | CS         |

**`SECTION`**:

|`section_identifier`|`course_number`|`semester`|`year`|`instructor`|
|:------------------:|---------------|----------|------|------------|
| 85                 | MATH2410      | Fall     | '07  | King       |
| 92                 | CS1310        | Fall     | '07  | Anderson   |
| 102                | CS3320        | Spring   | '08  | Knuth      |
| 112                | MATH2410      | Fall     | '08  | Chang      |
| 119                | CS1310        | Fall     | '08  | Anderson   |
| 135                | CS3380        | Fall     | '08  | Stone      |

**`GRADE_REPORT`**: `@TODO: Finish`

|`section_identifier`|`course_number`|`semester`|
|:------------------:|---------------|----------|
| 85                 | MATH2410      | Fall     |
| 92                 | CS1310        | Fall     |
| 102                | CS3320        | Spring   |
| 112                | MATH2410      | Fall     |
| 119                | CS1310        | Fall     |
| 135                | CS3380        | Fall     |

## Main Characteristics of Database Approach
1. Self-describing nature of a database system:
  - DBMS **catalog**
  - Called **meta-data**
  - This allows the DBMS software to work with different database applications

**Example of a simplified database catalog** `@TODO: Finish`
**`RELATIONS`**: 

2. Insulation between programs and data:
  - Called program-data independence
  - Allows changing data structures and storage organization, without having to change the DBMS access programs.

3. Data Abstractions
  - A **data model** is used to hide storage details and present the users with a conceptual view of the database.
  - Programs refer to the data model constructs rather than data storage details.
4. Support of multiple views of the data `@TODO: Finish`
5. Sharing of data and multi-user transaction processing `@TODO: Finish`

## Database Users
* Actors on the Scene
*   DBAs
*   Designers
*   Devs
* Workers behind the Scene
*   End Users

## Advantages of Using the Database Approach
* Controlling redundancy
*   Sharing of data among multiple users
* Restricting unauthorized access to data
* Providing persistent storage for program Objects
* Providing storage structures (e.g. indexes) for efficient query processing
* Providing optimization of queries for efficient processing
* Providing backup and recovery services
* Providing multiple interfaces to different classes of users
* Representing complex relationships among data
* Enforcing integrity constraints on the datbase
*   E.g. entering date in certain format
*   Can be implemented in database level and application level
* Drawing inferences and actions from the stored data using deductive and active rules and triggers
* Potential for enforcing standards.
*   E.g naming standards
* Reduced application development time
* Flixibility to change data structures
*   Most databases use tree data structure
* Availability of current information
* Econimies of scale
*   Doing more for less

## Historical Development of Database Technology
**Hierarchical and Network Models**
- Mid 1960s and dominated during the 70s
- Still in use: IBM's IMS system

**Relational Model based Systems**
- 1970, IBM research and several universities
- Products emerged in the early 80s

**OO and emerging applications**
- Late 80s and early 90s
- Their use has not taken off much
- Extended relational systems and OO support and for other data types

## Data Models
**Data Model** - A set of concepts to describe the **structure** of a database, the **operations** for manipulating these structures, and certain **constraints** that the database should obey.

## Schemas vs Instances

`@TODO: Finish`

**Database Schema** (intention)
**Database Instance** (state or extension)

**Examples of a database schema**
**Example of a database instance (store)**

## DBMS Languages
**Data Definition Language** (DDL)
**Data Manipulation Language** (DML)

### Types of DML
**High level** or non-procedural language
**Low level** or procedural language

## Typical DBMS Component Modules
`@TODO: Insert picture`

## Centralized and Client-server DBMS architectures
### Centralized DBMS
### Client-server DBMS

