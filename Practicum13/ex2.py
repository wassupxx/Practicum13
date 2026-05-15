N = int(input())
all_students = []
for student in range(N):
    courses = set(input().split())
    all_students.append(courses)

common_courses = all_students[0].intersection(*all_students[1:])
print(len(common_courses))
