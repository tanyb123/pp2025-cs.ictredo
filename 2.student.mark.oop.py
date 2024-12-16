class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}")


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name
        self.__marks = {}  # Dictionary to store student marks

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input_marks(self, students):
        print(f"Nhập điểm cho khóa học: {self.__name}")
        for student in students:
            mark = float(input(f"Nhập điểm của sinh viên {student.get_name()} (ID: {student.get_id()}): "))
            self.__marks[student.get_id()] = mark

    def display_marks(self, students):
        print(f"\nĐiểm cho khóa học: {self.__name}")
        for student in students:
            mark = self.__marks.get(student.get_id(), "Chưa có điểm")
            print(f"Sinh viên: {student.get_name()} (ID: {student.get_id()}), Điểm: {mark}")


class School:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self):
        num_students = int(input("Nhập số lượng sinh viên: "))
        for _ in range(num_students):
            student_id = input("Nhập ID sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            dob = input("Nhập ngày sinh (dd/mm/yyyy): ")
            self.__students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Nhập số lượng khóa học: "))
        for _ in range(num_courses):
            course_id = input("Nhập ID khóa học: ")
            name = input("Nhập tên khóa học: ")
            self.__courses.append(Course(course_id, name))

    def list_students(self):
        print("\nDanh sách sinh viên:")
        for student in self.__students:
            student.display()

    def list_courses(self):
        print("\nDanh sách khóa học:")
        for course in self.__courses:
            print(f"ID: {course.get_id()}, Tên: {course.get_name()}")

    def input_marks(self):
        self.list_courses()
        course_id = input("Chọn ID khóa học để nhập điểm: ")
        for course in self.__courses:
            if course.get_id() == course_id:
                course.input_marks(self.__students)
                return
        print("Khóa học không tồn tại.")

    def display_marks(self):
        self.list_courses()
        course_id = input("Chọn ID khóa học để xem điểm: ")
        for course in self.__courses:
            if course.get_id() == course_id:
                course.display_marks(self.__students)
                return
        print("Khóa học không tồn tại.")

    def menu(self):
        while True:
            print("\n=== QUẢN LÝ SINH VIÊN ===")
            print("1. Nhập thông tin sinh viên")
            print("2. Nhập thông tin khóa học")
            print("3. Nhập điểm cho khóa học")
            print("4. Liệt kê danh sách sinh viên")
            print("5. Liệt kê danh sách khóa học")
            print("6. Hiển thị điểm cho khóa học")
            print("7. Thoát")
            choice = input("Chọn chức năng (1-7): ")
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.display_marks()
            elif choice == "7":
                print("Thoát chương trình.")
                break
            else:
                print("Chức năng không hợp lệ.")


# Chạy chương trình
if __name__ == "__main__":
    school = School()
    school.menu()
