import numpy as np

# 1. Create a 1D array of study hours for 5 students
study_hours = np.array([2.5, 5.1, 3.2, 8.5, 3.5])

# 2. Calculate statistics
mean_hours = np.mean(study_hours)
max_hours = np.max(study_hours)

# 3. Perform a mathematical operation
study_minutes = study_hours * 60

# Output results
print("Study Hours:", study_hours)
print("Mean Hours:", mean_hours)
print("Max Hours:", max_hours)
print("Study Minutes:", study_minutes)