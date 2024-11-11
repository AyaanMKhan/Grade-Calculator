# Define the weights for each category
weights = {
    "first_week_quiz": 0.02,
    "assignments": 0.20,
    "lab_attendance": 0.12,
    "online_quizzes": 0.16,
    "midterm_exam": 0.20,
    "final_exam": 0.30
}

# Define the scores for each category
scores = {
    "first_week_quiz": 90,
    "assignments": [91.5, 0],  # Assignment 2 is missing
    "lab_attendance": 87.5,
    "online_quizzes": [100, 100, 100, 100, 100, 100, 80, 100],  # Drop the lowest 2 scores
    "midterm_exam": 90,
    "final_exam": 90  # Assume final exam score is not available yet
}

def calculate_weighted_average(weights, scores):
    total_weighted_score = 0
    total_weight = 0

    # Calculate the weighted score for the first week quiz
    total_weighted_score += weights["first_week_quiz"] * scores["first_week_quiz"]
    total_weight += weights["first_week_quiz"]

    # Calculate the weighted score for assignments
    assignment_average = sum(scores["assignments"]) / len(scores["assignments"])
    total_weighted_score += weights["assignments"] * assignment_average
    total_weight += weights["assignments"]

    # Calculate the weighted score for lab attendance
    total_weighted_score += weights["lab_attendance"] * scores["lab_attendance"]
    total_weight += weights["lab_attendance"]

    # Calculate the weighted score for online quizzes
    sorted_quizzes = sorted(scores["online_quizzes"])
    quizzes_to_consider = sorted_quizzes[2:]  # Drop the lowest 2 scores
    quiz_average = sum(quizzes_to_consider) / len(quizzes_to_consider)
    total_weighted_score += weights["online_quizzes"] * quiz_average
    total_weight += weights["online_quizzes"]

    # Calculate the weighted score for the midterm exam
    total_weighted_score += weights["midterm_exam"] * scores["midterm_exam"]
    total_weight += weights["midterm_exam"]

    # Calculate the weighted score for the final exam (if available)
    if scores["final_exam"] > 0:
        total_weighted_score += weights["final_exam"] * scores["final_exam"]
        total_weight += weights["final_exam"]

    # Calculate the final weighted average
    final_weighted_average = total_weighted_score / total_weight
    return final_weighted_average

# Calculate the final grade
final_grade = calculate_weighted_average(weights, scores)
print(f"Final Grade: {final_grade:.2f}%")