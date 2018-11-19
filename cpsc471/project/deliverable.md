# Deliverable 3: OO Diagram & Sequence Diagrams
## Group #15: Daniel Artuso, Artem Golovin, Victor Mendoza

## Notes and Assumptions

We only provided methods and diagrams for core functions. The rest of functionoality have been ommited, but will be implemented in the project.

## SQL Functions

### Create User

Function: `createUser(String firstName, String lastName, int age, double weight)`

```sql
INSERT INTO User (first_name, last_name, age, weight)
       VALUES    (firstName, lastName, age, weight)
```

### Create Workout

Function: `createWorkout(String name, String description)`

```sql
INSERT INTO Workout (name, routine_description)
       VALUES       (name, description)
```

### Add Nutrition Recording

Function: `addNutritionRecording(NutritionRecording recording)`

```sql
INSERT INTO Nutrition_Recording (day, month, 
                                 year, time, 
                                 calories, protein,
                                 carbohydrate, fat)
       VALUES (recording.date.day, recording.date.month,
               recording.date.year, recording.date.time,
                recording.calories, recording.protein, 
                recording.carbohydrate, recording.fat)
```

### Add Body Measurement Recording

Function: `addBodyMeasurementRecording(BodyMeasurementRecording recording)`

```sql
INSERT INTO BodyMeasurement_Recording (day, month, 
                                 year, time, 
                                 bodyfat, weight)
       VALUES (recording.date.day, recording.date.month,
               recording.date.year, recording.date.time,
                recording.bodyFat, recording.weight)
```

