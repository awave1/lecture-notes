# Deliverable 3: Class Methods

## Create User

Function: `createUser(String firstName, String lastName, int age, double weight)`

```sql
INSERT INTO User (first_name, last_name, age, weight)
       VALUES (firstName, lastName, age, weight)
```

## Create Workout

Function: `createWorkout(String name, String description)`

```sql
INSERT INTO Workout (name, routine_description) VALUES (name, description)
```

## Add Nutrition Recording

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

## Add Body Measurement Recording

Function: `addBodyMeasurementRecording(BodyMeasurementRecording recording)`

<!--@TODO: Update diagrams to remove body_part_name-->

```sql
INSERT INTO BodyMeasurement_Recording (day, month, 
                                 year, time, 
                                 bodyfat, weight)
       VALUES (recording.date.day, recording.date.month,
               recording.date.year, recording.date.time,
                recording.bodyFat, recording.weight)
```

