import itertools

def calculate_average_grade():
  """Calculates the average grade based on user input."""

  while True:
    subject = input("Enter the subject name: ")
    student_name = input("Enter the student's name: ")
    student_gender = input("Enter the student's gender (male/female): ")

    num_assessments_total = int(input("Enter the total number of assessments: "))
    num_assessments_completed = int(input("Enter the number of assessments completed: "))

    grades = []
    for i in range(num_assessments_completed):
      grade = float(input(f"Enter the grade for assessment {i + 1}: "))
      grades.append(grade)

    desired_average = float(input("Enter your desired average grade: "))

    # Calculate the missing grade (x)
    total_current_grades = sum(grades)
    total_missing_grades = (desired_average * num_assessments_total) - total_current_grades
    remaining_assessments = num_assessments_total - num_assessments_completed

    # Generate all possible combinations of missing grades that are less than or equal to 7
    combinations = []
    for i in range(1, remaining_assessments + 1):
      for combination in itertools.combinations_with_replacement(range(1, 8), i):
        if sum(combination) >= total_missing_grades:
          combinations.append(combination)

    if not combinations:
      print(f"It's impossible for {student_name} ({student_gender}) to achieve a {desired_average:.2f} average in {subject} with the current grades.")
    else:
      pronoun = "his" if student_gender.lower() == "male" else "her"
      print(f"{student_name} ({student_gender}) needs to score a total of at least {total_missing_grades:.2f} on {pronoun} remaining {remaining_assessments} assessments in {subject} to achieve a {desired_average:.2f} average.")
      print("Here are some possible combinations of grades:")
      for combination in combinations:
        print(combination)

    # Ask if the user wants to repeat the calculation
    repeat = input("Do you want to calculate another average? (yes/no): ")
    if repeat.lower() != "yes":
      break

if __name__ == "__main__":
  calculate_average_grade()
