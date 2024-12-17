def get_student_info():
    name = input("Enter your name: ")
    nsub = int(input("Enter number of subjects: "))
    return name, nsub
def get_subject_score(sub):
    global lst
    lst = []
    scores = 0
    for i in range(sub):
        student_score = int(input("Enter you score for subject " + str(i) + ": " ))
        scores += student_score
        lst.append(student_score)
    print("Your scores are: ", lst)

    return scores, len(lst)
def calculate_average(a,b):
    return a / b
def display_result(name, grade):
    print("You\'re name is", name, "and you\'re average grade is ", grade)

def highest_to_lowest():
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                swapped = True
                lst[i], lst[i + 1] = lst[i +1], lst[i]
    print("You\'re grade is sorted: ", lst)
def max_score():
    print("You\'re highest grade: ", lst[0])
def min_score():
    print("You\'re lowest grade: ", lst[-1])

student_info = get_student_info()
subject_scores = get_subject_score(student_info[1])
highest_to_lowest()
max_score()
min_score()
average = calculate_average(subject_scores[0], subject_scores[1])
result = display_result(student_info[0], average)
