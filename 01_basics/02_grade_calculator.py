"""
02_grade_calculator.py
Module 1 Practice: Interactive CLI Student Grade Analyzer
Demonstrates: Functions, loops, user input, lists, conditionals, and formatting.
"""

def calculate_letter_grade(score: float) -> str:
    """Converts a numerical score (0-100) into a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def analyze_scores(scores: list) -> dict:
    """Calculates statistics for a list of numerical scores."""
    if not scores:
        return {"count": 0, "average": 0.0, "max": 0, "min": 0, "pass_count": 0}

    total = sum(scores)
    count = len(scores)
    avg = total / count
    
    # Count how many scores are passing (>= 60)
    pass_count = 0
    for score in scores:
        if score >= 60:
            pass_count += 1

    return {
        "count": count,
        "average": round(avg, 2),
        "max": max(scores),
        "min": min(scores),
        "pass_count": pass_count
    }


def main():
    """Main execution loop for the CLI application."""
    print("========================================")
    print("  PYTHON GRADEMASTER CLI - MODULE 1")
    print("========================================\n")

    student_scores = []

    # Loop to continuously take student score inputs
    while True:
        user_input = input("Enter a score (0-100) or type 'done' to analyze: ").strip().lower()

        if user_input == "done":
            break

        # Input Validation: convert text to float safely
        try:
            score = float(user_input)
            if 0 <= score <= 100:
                student_scores.append(score)
                letter = calculate_letter_grade(score)
                print(f" -> Recorded: {score} (Grade: {letter})")
            else:
                print(" [!] Please enter a valid score between 0 and 100.")
        except ValueError:
            print(" [!] Invalid input. Enter a number or 'done'.")

    # Display results after exiting the loop
    print("\n----------------------------------------")
    print("         SUMMARY REPORT")
    print("----------------------------------------")

    if not student_scores:
        print("No scores were entered.")
    else:
        stats = analyze_scores(student_scores)
        overall_letter = calculate_letter_grade(stats["average"])

        print(f" Total Students Processed : {stats['count']}")
        print(f" Class Average            : {stats['average']} (Overall Grade: {overall_letter})")
        print(f" Highest Score            : {stats['max']}")
        print(f" Lowest Score             : {stats['min']}")
        print(f" Students Passing (>= 60) : {stats['pass_count']} / {stats['count']}")
        print("----------------------------------------\n")


# Entry point guard (ensures this script runs only when executed directly)
if __name__ == "__main__":
    main()