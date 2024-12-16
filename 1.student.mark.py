    students = [] 
    courses = []   
    marks = {}    

    def input_students():
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")    
            name = input("Enter student name: ")
            dob = input("Enter birthday (dd/mm/yyyy): ")
            students.append({"id": student_id, "name": name, "dob": dob})

    def input_courses():
        num_courses = int(input(" Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            courses.append({"id": course_id, "name": name})
            marks[course_id] = {}  

    def input_marks():
        print("Enter courses list: ")
        list_courses()
        course_id = input("Enter course ID to input marks: ")
        if course_id not in marks:
            print("Course does not exist.")
            return
        print("Enter marks for student: ")
        for student in students:
            mark = float(input(f"Enter marks for each student['name']} (ID: {student['id']}): "))
            marks[course_id][student['id']] = mark

    def list_courses():
        print("Course list")
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

    def list_students():
        print("Student list:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Ngày sinh: {student['dob']}")

    def show_marks():
        print("Danh sách khóa học: ")
        list_courses()
        course_id = input("Choose id course for show marks: ")
        if course_id not in marks:
            print("Course not available.")
            return
        print(f"Mark for course {course_id}:")
        for student in students:
            mark = marks[course_id].get(student['id'], "No mark")
            print(f"Student: {student['name']} (ID: {student['id']}), Điểm: {mark}")

    def menu():
        while True:
            print("\n=== QUẢN LÝ Student ===")
            print("1. Nhập thông tin Student")
            print("2. Nhập thông tin khóa học")
            print("3. Nhập điểm cho khóa học")
            print("4. Liệt kê Student list")
            print("5. Liệt kê danh sách khóa học")
            print("6. Hiển thị điểm cho khóa học")
            print("7. Thoát")
            choice = input("Chọn chức năng (1-7): ")
            if choice == "1":
                input_students()
            elif choice == "2":
                input_courses()
            elif choice == "3":
                input_marks()
            elif choice == "4":
                list_students()
            elif choice == "5":
                list_courses()
            elif choice == "6":
                show_marks()
            elif choice == "7":
                print("Thoát chương trình.")
                break
            else:
                print("Chức năng không hợp lệ. Hãy chọn lại.")
    if __name__ == "__main__":
        menu()
