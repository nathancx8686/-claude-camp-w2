def main():
    last_answer = None
    print("欢迎使用计算器，请输出数字和运算符号+-*/，输入c清零，输入quit退出:")
    while True:
        user_input = input("> ").strip()
        
        if user_input.lower() == "c":
            last_answer = None
            print("已清零！")
            continue

        if user_input.lower() == "quit":
            print("再见！谢谢使用！")
            break
        
        try:
            # 如果开头是运算符，自动加上上次结果
            if last_answer is not None and user_input[0] in "+-*/": #user_input[0] 是第一字符
                user_input = str(last_answer) + user_input #因为不能把数字和字符串直接相加：
            
            result = eval(user_input) #eval 里面是字符串，但内容必须是合法的 Python 数学表达式：
            last_answer = result
            print(f"= {result}")
            
        except ZeroDivisionError:
            print("❌ 不能除以0！")
        except:
            print("❌ 输入格式有误！")

if __name__ == "__main__":
    main()