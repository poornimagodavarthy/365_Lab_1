student_map, teacher_map, bus_route, grade_map = {}, {}, {}, {}

def user_input():
    query = input("Enter query: ").strip().split()
    while query:
        if query[0].startswith("S"):
            student(query)
        elif query[0].startswith("T"):
            teacher(query)
        elif query[0].startswith("B"):
            break
        elif query[0].startswith("G"):
            break
        elif query[0].startswith("A"):
            break
        elif query[0].startswith("I"):
            break
        elif query[0].startswith("Q"):
            break
        else:
            print("Invalid Query, please try again")
        query = input("Enter query: ").strip()

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
    pass
    
def teacher(query):
    for lst in teacher_map[query[1]]:
        print(lst[1], lst[0])

def grade(query):
    pass

def bus(query):
    pass


def main():
    parse_data()
    user_input()

if __name__ == "__main__":
    main()



    