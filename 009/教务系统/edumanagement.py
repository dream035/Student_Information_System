__all__ = ["EduManagement"]
#教务系统类
from student import *

class EduManagement:
    sys_version = "0.1"
    sys_name = "教务管理系统"

    def __init__(self):
        self.Student_List = [] #列表，在校学生
        print(f"教务系统{self.sys_version}初始化完毕")

    # 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    def add_student(self):
        name = input("请输入学生姓名：")

        for s in self.Student_List:#s为学生类
            if s.name == name:
                print("学生已存在，添加失败")
                return

        chinese = float(input("请输入学生语文成绩："))
        math = float(input("请输入学生数学成绩："))
        english = float(input("请输入学生英语成绩："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.Student_List.append(stu)
            print("添加成功")
        else:
            print("学生成绩必须在0-100之间")

    # 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for s in self.Student_List:
            if s.name == name:
                print("学生存在")
                print(f"原成绩：{s}")

                chinese = float(input("请输入要修改的学生语文成绩："))
                math = float(input("请输入要修改的学生数学成绩："))
                english = float(input("请输入要修改的学生英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("修改成功")
                    print(f"修改后成绩：{s}")
                    return
                else:
                    print("学生成绩必须在0-100之间")
                    return
        print("未找到该学生")

    # 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    def delete_student(self):
        name = input("请输入要删除学生姓名：")

        for s in self.Student_List:  # s为学生类
            if s.name == name:
                self.Student_List.remove(s)
                print("学生已删除")
                return
        print("未找到该学生")
    # 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
    def show_student(self):
        name = input("请输入要查询学生姓名：")
        for s in self.Student_List:
            if s.name == name:
                print(f"学生成绩为：{s}")
                return
        print("未找到该学生")
    # 展示全部学生成绩：展示出系统中所有学生的成绩
    def show_all_student(self):
        for s in self.Student_List:
            print(s)