def main():
    text = input("请输入一段ENGLISH文字：")
    # 后面继续写...
    text=text.lower()
    words=text.split()
    words = [word.strip(".,!?;:") for word in words]  # 去掉标点
    counts={}
    for word in words: # 遍历单词列表,# 遍历完自动结束,只有 while True 才需要 break
        if word in counts: 
            counts[word]+=1  # 直接添加新 key # counts = {"hello": 1}

        else:           
            counts[word]=1 
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)#reverse=True → 从高到低,key=lambda x: x[1] → 按第二个元素（次数）排序
#items() 是字典的内置方法，专门用来把字典转成可遍历的列表：
    for word, count in sorted_counts: #这个word count定义了吗 没有提前定义！for 循环自动帮你定义的。
    #Python 看到 in sorted_counts 就知道：这里面每个元素是 ("hello", 3) 两个值自动把第一个给 word，第二个给 count
        print(f"{word}: {count}")


    # 字母统计 ← 加在这里
    letter_counts = {}
    for letter in text:
        if letter==" ":
            continue
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

        sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    for letter, cnt in sorted_letters:
        print(f"{letter}: {cnt}")

if __name__ == "__main__":
    main()