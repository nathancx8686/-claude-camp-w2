
import json
def main():
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = {
            "zhangwei": {"email": "zhangwei@gmail.com", "add_date": "2025-01-05"},
            "linan":    {"email": "lina@qq.com",         "add_date": "2025-01-08"},
            "wangfang": {"email": "wangfang@163.com",     "add_date": "2025-01-10"},
            "chenming": {"email": "chenming@outlook.com", "add_date": "2025-01-12"},
            "liuyang":  {"email": "liuyang@hotmail.com",  "add_date": "2025-01-15"},
        }
    while True:
        print("\n--- 学员管理系统 ---")
        print("1. 添加 2. 查询 3. 删除 4. 显示所有学员 5. 修改 6. 退出")
        try:
            choice = int(input("请选择操作 (1-6): "))
        except ValueError:
            print("❌ 错误：请输入数字！")
            continue

        if choice == 1:
            name = input("请输入姓名：")
            email = input("请输入邮箱：")
            date = input("请输入加入日期：")
            students[name] = {"email": email, "add_date": date}
            print(f"✅ {name} 添加成功！") 
            with open("students.json", "w") as f:
                json.dump(students, f)

        elif choice == 2:
            name = input("请输入要查询的姓名：")
            if name in students:
                print(f"姓名：{name}")
                print(f"邮箱：{students[name]['email']}")
                print(f"日期：{students[name]['add_date']}")
            else:
                print("❌ 找不到此学员！")
        elif choice == 3:
            name = input("请输入要删除的姓名：")
            if name in students:
                del students[name]
                print(f"✅ {name} 删除成功！")
                with open("students.json", "w") as f:
                    json.dump(students, f)
            else:
                print("❌ 找不到此学员！")
        elif choice == 4:
            print("\n--- 全部学员 ---")
            for name, info in students.items():
                print(f"姓名：{name} | 邮箱：{info['email']} | 日期：{info['add_date']}")
        
        elif choice == 6:
            print("感谢使用，再见！")
            break

        elif choice == 5:
            name = input("请输入要修改的姓名：")
            if name in students:
                print(f"当前邮箱：{students[name]['email']}")
                print(f"当前日期：{students[name]['add_date']}")
                new_email = input("新邮箱（不改直接回车）：")
                new_date = input("新日期（不改直接回车）：")
                if new_email:
                    students[name]['email'] = new_email
                if new_date:
                    students[name]['add_date'] = new_date
                print(f"✅ {name} 修改成功！")
            else:
                print("❌ 找不到此学员！")

        else:
            print("❌ 无效选项！")

if __name__ == "__main__":
    main()
