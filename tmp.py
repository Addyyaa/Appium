# 定义文件名
file_name = "配网结果1.txt"

# 初始化计数器和最后一次配网次数
fail_count = 0
last_attempt = 0

# 尝试打开文件
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        # 逐行读取文件内容
        lines = file.readlines()

        # 遍历每一行
        for line_number, line in enumerate(lines, start=1):
            # 判断是否包含连接失败的关键词
            if "连接失败" in line:
                fail_count += 1

            # 获取最后一次配网次数
            if line.startswith("第") and "次配网" in line:
                last_attempt = int(line.split("次")[0][1:])
except FileNotFoundError:
    print(f"找不到文件：{file_name}")
except Exception as e:
    print(f"发生错误：{e}")


# 打印统计结果
print(f"连接失败的次数：{fail_count}")
print(f"最后一次配网次数：{last_attempt}")
