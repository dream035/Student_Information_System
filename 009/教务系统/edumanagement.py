__all__ = ["EduManagement"]
#教务系统类
from student import *
import json
import os

class EduManagement:
    sys_version = "0.1"
    sys_name = "教务管理系统"

    def __init__(self):
        self.Student_List = [] #列表，在校学生
        self.folder_name = "Student_data"#数据文件夹名
        self.filename = "students_data.json"  # 数据文件名称
        # 创建文件夹（如果不存在）
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            print(f"已创建数据文件夹：{self.folder_name}")

        self.load_data()  # 启动时自动加载数据
        print(f"教务系统{self.sys_version}初始化完毕")

        # 保存数据到文件
    def save_data(self):
        """将学生列表保存到JSON文件"""
        try:
            # 将Student对象转换为字典格式
            data = []
            for student in self.Student_List:
                student_dict = {
                    'name': student.name,
                    'chinese': student.chinese,
                    'math': student.math,
                    'english': student.english
                }
                data.append(student_dict)

            # 写入文件
            with open(f"{self.folder_name}/{self.filename}", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("数据保存成功")
            return True
        except Exception as e:
            print(f"数据保存失败：{e}")
            return False

    # 从文件加载数据
    def load_data(self):
        """从JSON文件加载学生数据"""
        if os.path.exists(f"{self.folder_name}/{self.filename}"):#判断是否存在文件
            try:
                with open(f"{self.folder_name}/{self.filename}", 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # 将字典数据转换回Student对象
                self.Student_List = []
                for student_dict in data:
                    student = Student(student_dict['name'],student_dict['chinese'],student_dict['math'],student_dict['english'])
                    self.Student_List.append(student)

                print(f"成功加载 {len(self.Student_List)} 条学生记录")
            except Exception as e:
                print(f"加载数据失败：{e}")
                self.Student_List = []
        else:
            print("未找到历史数据文件，将创建新文件")

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
            self.save_data()#保存
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
                    self.save_data()#保存
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
                self.save_data()#保存
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