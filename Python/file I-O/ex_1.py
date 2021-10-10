def create_students_files(exams):
    for i in range(len(exams)):

        with open("grades" + exams[i]["name"] + ".txt", 'w') as f:
            str_to_write = ""
            grades_sum = 0
            for j in range(1, 4):
                str_to_write += "Quiz {}: {}\n".format(j, exams[i]["quiz"+str(j)])
                grades_sum += exams[i]["quiz"+str(j)]
            f.write(str_to_write + "----\n" + str(round(grades_sum/3, 2)))


quizzes = [
    {"name": "Guillermo", "quiz1": 80, "quiz2": 85, "quiz3": 82},
    {"name": "Jamie", "quiz1": 78, "quiz2": 72, "quiz3": 80},
    {"name": "Otto", "quiz1": 92, "quiz2": 89, "quiz3": 96},
    {"name": "Christina", "quiz1": 91, "quiz2": 85, "quiz3": 94},
    {"name": "Ceasar", "quiz1": 62, "quiz2": 65, "quiz3": 73},
    {"name": "Barbara", "quiz1": 78, "quiz2": 68, "quiz3": 78},
    {"name": "Rosan", "quiz1": 84, "quiz2": 85, "quiz3": 81},
    {"name": "Marco", "quiz1": 79, "quiz2": 72, "quiz3": 87},
]
create_students_files(quizzes)