# ==========================================
# 1. Variables & Data Types
# ==========================================
study_hours = 5.5
student_name = "Sudha"
has_passed = True
total_students = 30

# ==========================================
# 2. Operators & Conditions
# ==========================================
# Predict initial score based on study time
score = (study_hours * 10) + 20

# Check if the student passed comfortably
is_high_score = score > 50
is_successful = has_passed and is_high_score

print(f"Is score higher than 50? {is_high_score}")
print(f"Passed with high score? {is_successful}")

# ==========================================
# 3. Loops
# ==========================================
print("\n--- Predicted Scores by Hour ---")
for hour in range(1, 6):
    predicted = (hour * 10) + 20
    print(f"Study hour {hour}: predicted score = {predicted}")

print("\n--- Study Session Tracker ---")
current_hour = 1
while current_hour <= 5:
    print(f"Studying... hour {current_hour}")
    current_hour += 1

# ==========================================
# 4. Functions
# ==========================================
def predict_score(hours: float) -> float:
    """Calculates a simple baseline predicted score given study hours."""
    return (hours * 10) + 20


print("\n--- Function Predictions ---")
study_times = [1, 2, 3, 4, 5]

for hours in study_times:
    predicted_score = predict_score(hours)
    print(f"Hours: {hours} -> Predicted Score: {predicted_score}")