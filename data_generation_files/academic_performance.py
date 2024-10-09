import csv
import random

# Teacher data
teachers = {
    "English Language": [201, 202, 203],
    "Mathematics": [204, 205, 206],
    "Basic Science": [207, 208, 209],
    "Basic Technology": [210, 211, 212],
    "Social Studies": [213, 214, 215],
    "Civic Education": [216, 217, 218],
    "Physics": [219, 220, 221],
    "Chemistry": [222, 223, 224],
    "Biology": [225, 226, 227],
    "Literature-in-English": [228, 229, 230],
    "Government": [231, 232, 233],
    "History": [234, 235, 236],
    "Financial Accounting": [237, 238, 239],
    "Commerce": [240, 241, 242],
    "Economics": [243, 244, 245],
}

# Class arms and subjects
junior_subjects = ["Mathematics", "English Language", "Civic Education", "Basic Science", "Basic Technology", "Social Studies"]
senior_subjects = {
    "A": ["Mathematics", "English Language", "Civic Education", "Literature-in-English", "Government", "History"],
    "B": ["Mathematics", "English Language", "Civic Education", "Physics", "Chemistry", "Biology"],
    "C": ["Mathematics", "English Language", "Civic Education", "Financial Accounting", "Commerce", "Economics"]
}

# Assign one teacher per subject per arm
arm_teachers = {}

def assign_teachers_to_arms():
    global arm_teachers
    arm_teachers = {
        "A": {subject: teachers[subject][0] for subject in junior_subjects + senior_subjects["A"]},  # First teacher for each subject
        "B": {subject: teachers[subject][1] for subject in junior_subjects + senior_subjects["B"]},  # Second teacher for each subject
        "C": {subject: teachers[subject][2] for subject in junior_subjects + senior_subjects["C"]},  # Third teacher for each subject
    }

# Generate a score with distribution including 80-100 range
def generate_score():
    # 50% chance for 40-60, 30% chance for 30-40, 10% for 60-80, 10% for 80-100
    score_distribution = random.choices(
        [(30, 40), (40, 60), (60, 80), (80, 100)], 
        weights=[0.3, 0.5, 0.1, 0.1], 
        k=1
    )[0]
    return random.randint(score_distribution[0], score_distribution[1])

# Create rows for each student's performance
def generate_performance_data():
    rows = []
    performance_id = 1

    for student_id in range(1001, 1301):
        if 1001 <= student_id <= 1100:
            arm = "A"
        elif 1101 <= student_id <= 1200:
            arm = "B"
        else:
            arm = "C"

        # Add Junior School records (2019-2021)
        for year_offset, class_level in enumerate(["1", "2", "3"], start=2019):
            class_name = f"JS{class_level}{arm}"  # JSS1, JSS2, JSS3
            for subject in junior_subjects:
                rows.append([
                    performance_id, student_id, year_offset, class_name, subject,
                    generate_score(), arm_teachers[arm][subject]
                ])
                performance_id += 1

        # Add Senior School records (2022-2023)
        for year_offset, class_level in enumerate(["1", "2"], start=2022):
            class_name = f"SS{class_level}{arm}"  # SS1, SS2
            for subject in senior_subjects[arm]:
                rows.append([
                    performance_id, student_id, year_offset, class_name, subject,
                    generate_score(), arm_teachers[arm][subject]
                ])
                performance_id += 1

    return rows

# Write to CSV
def write_to_csv():
    assign_teachers_to_arms()  # Ensure the arm-teacher assignments are set
    with open('FactAcademicPerformance8.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["performance_id", "student_id", "year", "class_name", "subject", "total_score", "teacher_id"])

        # Generate and write rows
        performance_data = generate_performance_data()
        writer.writerows(performance_data)

    print("CSV file 'FactAcademicPerformance7.csv' generated successfully.")

# Run the script
write_to_csv()
