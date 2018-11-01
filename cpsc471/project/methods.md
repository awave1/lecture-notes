# Deliverable 3: Class Methods

## User

1. `createWorkout(String name, String description)`

```sql
INSERT INTO Workout (name, routine_description) VALUES (name, description)
```

2. `editWorkout(String name, String description, int workoutId)`

```sql
UPDATE Workout SET name = name, routine_description = description WHERE id = workoutId
```

3. `markWorkoutAsPerformed(workoutId)`

```sql
INSERT INTO History (user_id, workout_id) VALUES (this.userId, workoutId) 
```

## Trainer

### Trains

## Goal

## History

## Schedule

## Workout

1. `addSetExercise(int exerciseId)`

```sql
INSERT INTO SetExercise (workout_id) VALUES (this.workout_id) WHERE exercise_id = exerciseId
```

1. `addTimedExercise(int exerciseId)`

```sql
INSERT INTO TimedExercise (workout_id) VALUES (this.workout_id) WHERE exercise_id = exerciseId
```

2. `getAllExercises()`

```sql
SELECT * FROM SetExercise CROSS JOIN TimedExercise WHERE workout_id = this.workout_id
```

## SetExercise

1. `createExercise()`

```sql
```

### Set

## TimedExercise

## NutritionRecording

### MicronutrientRecording

### Macronutrient

### Micronutrient

## BodyMeasurementRecording

### BodyPartMeasurement
