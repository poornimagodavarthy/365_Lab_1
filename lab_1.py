student_map, teacher_map, bus_route, grade_map = {}, {}, {}, {}

def user_input():
    query = input("Enter query: ").strip().split(' ')
    while query:
        if query[0].startswith("S"):
            student(query)
        elif query[0].startswith("T"):
            teacher(query)
        elif query[0].startswith("B"):
            bus(query)
        elif query[0].startswith("G"):
            grade(query)
        elif query[0].startswith("A"):
            average(query)
        elif query[0].startswith("I"):
            info()
        elif query[0].startswith("Q"):
            break
        else:
            print("Invalid Query, please try again")
        query = input("Enter query: ").strip().split(' ')


def parse_data():
    #read each instance to hashmap
    file_path = "./students.txt"
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] not in student_map:
                student_map[line[0]] = [line]
            else:
                student_map[line[0]].append(line)

            if line[6] not in teacher_map:
                teacher_map[line[6]] = [line]
            else:
                teacher_map[line[6]].append(line)

            if line[4] not in bus_route:
                bus_route[line[4]] = [line]
            else:
                bus_route[line[4]].append(line)

            if line[2] not in grade_map:
                grade_map[line[2]] = [line]
            else:
                grade_map[line[2]].append(line)
    file.close()
   

def student(query):
    if query[1] in student_map:
        if len(query) > 2:
            if query[2].startswith("B"):
                for lst in student_map[query[1]]:
                    print(lst[0], lst[1], lst[4])
            else:
                print("Invalid Query, please try again")
                return
        else:
            for lst in student_map[query[1]]:
                print(lst[0], lst[1], lst[2], lst[3], lst[6], lst[7])
    else:
        print("No student found")

    
def teacher(query):
    if query[1] in teacher_map:
        for lst in teacher_map[query[1]]:
            print(lst[0], lst[1])
    else:
        print("No teacher found")


def grade(query):
    if query[1] in grade_map:
        if len(query) > 2:
            if query[2].startswith("H"):
                cur_gpa = grade_map[query[1]][0][5]
                cur_student = []
                for lst in grade_map[query[1]]:
                    if lst[5] > cur_gpa:
                        cur_gpa = lst[5]
                        cur_student = [[lst[0], lst[1]]]
                    elif lst[5] == cur_gpa:
                        cur_student.append([lst[0], lst[1]])
                for student in cur_student:
                    print(student[0], student[1])

            elif query[2].startswith("L"):
                cur_gpa = grade_map[query[1]][0][5]
                cur_student = []
                for lst in grade_map[query[1]]:
                    if lst[5] < cur_gpa:
                        cur_gpa = lst[5]
                        cur_student = [[lst[0], lst[1]]]
                    elif lst[5] == cur_gpa:
                        cur_student.append([lst[0], lst[1]])
                for student in cur_student:
                    print(student[0], student[1])

            else:
                print("Invalid Query, please try again")
                return
            
        else:
            for lst in grade_map[query[1]]:
                print(lst[0], lst[1])
    else:
        print("No data for grade")


def bus(query):
    if query[1] in bus_route:
        for lst in bus_route[query[1]]:
            print(lst[0], lst[1], lst[4])
    else:
        print("No students found for bus route")


def average(query):
    sum_gpa = 0
    count_gpa = 0
    if query[1] in grade_map:
        for lst in grade_map[query[1]]:
            sum_gpa += float(lst[5])
            count_gpa += 1
        print(sum_gpa/count_gpa)
    else:
        print("No data for grade")


def info():
    for grade in range(7):
        if str(grade) in grade_map:
            print(str(grade) + ": " + str(len(grade_map[str(grade)])))
        else:
            print(str(grade) + ": 0")


def main():
    parse_data()
    user_input()


if __name__ == "__main__":
    main()
