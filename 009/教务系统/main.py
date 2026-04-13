#交互类
from edumanagement import *

print(f"欢迎使用教务系统! V{EduManagement.sys_version}")
e1 = EduManagement()
cai_dan = """
    *******************
    **   1.添加学生   **
    **   2.修改学生   **
    **   3.删除学生   **
    **   4.查看学生   **
    **   5.全部学生   **
    **   6.退出系统   **
    *******************
    """
while True:
    print(cai_dan)
    num = int(input("请输入选项:"))
    try:
        match num:
            case 1:
                e1.add_student()
            case 2:
                e1.update_student()
            case 3:
                e1.delete_student()
            case 4:
                e1.show_student()
            case 5:
                e1.show_all_student()
            case 6:
                e1.save_data()#退出保存
                print("已退出系统，欢迎下次使用！")
                break
            case _:
                print("输入错误")
    except ValueError:
        print("输入数据有问题")
    except Exception:
        print("程序出错了，请重选择")



