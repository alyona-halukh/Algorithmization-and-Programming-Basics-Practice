def calculate_average(grades):
    return sum(grades) / len(grades)


def find_max_grade(grades):
    return max(grades)


def find_min_grade(grades):
    return min(grades)


def analyze_grades(grades):
    if len(grades) == 0:
        return "Список оцінок порожній"

    average = calculate_average(grades)
    max_grade = find_max_grade(grades)
    min_grade = find_min_grade(grades)

    print("Середній бал:", average)
    print("Найвища оцінка:", max_grade)
    print("Найнижча оцінка:", min_grade)


grades = [90, 75, 85, 100, 60]

analyze_grades(grades)