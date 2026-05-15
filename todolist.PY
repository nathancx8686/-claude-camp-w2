import json
def main(): #有名字用字典，没名字用列表
    try:
        with open("todolist.json", "r") as f:
            todolist = json.load(f)
        
    except FileNotFoundError:
        todolist = []
    
    while True:
        print("\n--- 待办清单 ---")
        print("1. 添加 2. 完成 3. 查看 4. 退出")
        try:
            choice = int(input("请选择操作数字: "))
        except ValueError:
            print("❌ 请输入有效的数字！")
            continue
        if choice == 1:   #字典用 [key] =，列表用 append()
            task = input("请输入待办事项：")
            due = input("请输入截止日期（如 2026-05-20）:")
            todolist.append({"task": task, "done": False,"due": due})
            with open("todolist.json", "w") as f:
                json.dump(todolist, f)
            print(f"✅ {task} 添加成功！")

  
        elif choice == 2: # 先显示所有未完成任务
            for todo in todolist:
                if not todo["done"]:
                    print(f"⬜ {todo['task']} | 截止: {todo['due']}")
            task = input("请输入要完成的任务名：")     # 用户输入任务名
            for todo in todolist:
                if todo["task"] == task:
                    todo["done"] = True
                    print(f"✅ {task} 完成！")
                    with open("todolist.json", "w") as f:
                        json.dump(todolist, f)
                    break
        elif choice == 3:
            sorted_todos = sorted(todolist, key=lambda x: x["due"])
            for todo in sorted_todos:
                if todo["done"]:
                    status = "done"
                else:
                    status = "not done"
                print(f"{status} {todo['task']} | 截止: {todo['due']}")

        elif choice == 4:
            print("再见,欢迎再次使用！")
            break
    

        else:
            print("❌ 无效选项，请重洗尝试！")    

if __name__ == "__main__":
    main()