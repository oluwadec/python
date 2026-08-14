# 1. Integers & Floats (Numbers)
age = 21
temperature = 36.6

# 2. Strings (Text)
student_name = "Alex"
greeting = f"Hello, {student_name}!"  # f-string: string interpolation

# 3. Booleans (True / False)
is_active = True
has_passed = False

# 4. NoneType (Represents absence of value)
current_session = None

print(f"{greeting} Age: {age}, Active: {is_active}")

# --- Control Flow ---
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} | Grade: {grade}")

# --- Loops ---
print("\n--- Range Loop ---")
for i in range(5):
    print(f"Iteration {i}")

print("\n--- Collection Loop ---")
languages = ["Python", "C++", "Rust", "Go"]
for lang in languages:
    print(f"Learning {lang}")

print("\n--- While Loop ---")
counter = 0
while counter < 3:
    print(f"Counter status: {counter}")
    counter += 1


# --- Functions ---
def calculate_grade_stats(scores: list) -> dict:
    """Calculates summary stats for a list of numerical scores."""
    if not scores:
        return {"average": 0.0, "max": 0, "min": 0, "count": 0}

    total = sum(scores)
    count = len(scores)
    avg = total / count

    return {
        "average": round(avg, 2),
        "max": max(scores),
        "min": min(scores),
        "count": count,
    }


# Function execution
class_scores = [88, 92, 79, 95, 61, 84]
stats = calculate_grade_stats(class_scores)

print("\n--- Grade Statistics ---")
print(f"Average Score: {stats['average']}")
print(f"Highest Score: {stats['max']}")
print(f"Lowest Score:  {stats['min']}")
print(f"Total Students: {stats['count']}")