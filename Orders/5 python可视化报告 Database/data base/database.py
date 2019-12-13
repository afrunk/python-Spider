"""
python project
对txt实现增删改查

"""
# 读取txt的信息以,分割符存入到列表中便于后续的操作


def show_menu():
    print("""\nA) Find eligible song information
B) Show all song`s information
C) Input a song
D) Delect a song
E) Modify a song
F)  Exit""")

# 将我们修改后的列表数据传入到函数中写入到我们的规定好的文件中去
def save_data_txt(txt_list):
    # for i in txt_list:
    #     print(i)
    filename = 'data.txt'
    for input_information in txt_list:
        # 第一次写入的时候需要情况之前的txt数据 所以使用 w 覆盖的写法
        if input_information[0]=='Song ID':
            print(input_information)
            data = input_information[0] + ',' + input_information[1] + ',' + input_information[
                2] + ',' + input_information[3]+ ',' + input_information[4]
            with open(filename, 'w') as f:
                # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                # a 追加
                f.write(data)
                # print("write Success!\n")
        else:
        # 除了第一次之外的所有的数据都是追加的方法写入txt
            print(input_information)
            data = input_information[0] + ',' + input_information[1] + ',' + input_information[
                2] + ',' + input_information[3] + ',' + input_information[4]
            with open(filename, 'a') as f:
                # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                # a 追加
                f.write(data)
                # print("write Success!\n")

# 1. input songname,author,year,or types 输出符合条件的书籍信息
def input_songname_author_year_types():
    filename = 'data.txt'
    with open(filename, encoding='utf-8')  as f:  # 遍历 存入列表
        txt_list = [content.rsplit(',') for content in f]
    # for i in txt_list:
    #     print(i)
    flag = 0
    inputtext= input("input songname,author,year,or types: ")
    for i in txt_list:
        for data in i:
            # 如果不加一个for循环的话 判断的必须与输入一致 但是我们存在列表中的元素 年份后还有一个\n 所以需要加一个for循环
            # 在进行比较前将两个字符串都转换称为小写 再进行比较
            # print(inputtext.lower())
            # print(data.lower())
            if inputtext.lower() in  data.lower():
                print(i)
                flag =1

    if flag ==0:
        print("输入错误，搜索不到结果！")

# 2. show all song`s information 输出所有的信息
def show_all_song_information():
    # 对齐格式
    tplt = "{0:^20}\t{1:^20}\t{2:^20}\t{3:^20}\t{4:^20}"
    filename = 'data.txt'
    with open(filename, encoding='utf-8')  as f:  # 遍历 存入列表
        txt_list = [content.rsplit(',') for content in f]
    # for i in txt_list:
    #     print(i)
    for list  in txt_list:
        print(tplt.format(list[0], list[1], list[2],list[3],list[4]))

# 3. input a song
# 添加书籍，手动输入书籍名字、类型、作者、年份、确认添加 数据id自动叠加
def input_song_information():
    filename = 'data.txt'
    with open(filename, encoding='utf-8')  as f:  # 遍历 存入列表
        txt_list = [content.rsplit(',') for content in f]
    # for i in txt_list:
    #     print(i)
    #当前书籍的插入序数是多少
    listname = len(txt_list)
    # print(listname)
    input_information = input("Please input this song`s information，Separated by commas:").rsplit(',')
    print(input_information)

    data = str(listname)+','+input_information[0]+','+input_information[1]+','+input_information[2]+','+input_information[3]+'\n'
    data =data.rsplit(',')
    txt_list.append(data)
    # 调用函数将数据保存到txt
    save_data_txt(txt_list)

# 4. delect a song
"""
这里有确认删除和返回上一级，
"""
def delect_a_song():
    filename = 'data.txt'
    with open(filename, encoding='utf-8')  as f:  # 遍历 存入列表
        txt_list = [content.rsplit(',') for content in f]
    # for i in txt_list:
    #     print(i)
    # 测试用语
    for j in txt_list:
        print(j)

    inputNum = input("please input song`s num:")
    # 计算好列表的长度进行遍历
    lenTxtList =len(txt_list)
    print(lenTxtList)
    # 遍历删除我们匹配到的列表信息
    for i in range(lenTxtList):
        if inputNum == txt_list[i][0]:
            # 如果遍历到了 则进行判断是否确认删除
            isornot = input("Whether to confirm the deletion：y/n ")
            # 如果是确认删除 则需要修改后续的书籍的编号
            if isornot=='y':
                del txt_list[i]
                # 修改被删除的列表的后续的信息编号信息
                for s in range(i, lenTxtList-1):
                    txt_list[s][0] = str(int(txt_list[s][0]) - 1)
                # 调用函数将数据保存到txt
                save_data_txt(txt_list)
            else:
                print("取消删除 返回上一级！")
                break

# 5. modify information
def modify_information():
    filename = 'data.txt'
    with open(filename, encoding='utf-8')  as f:  # 遍历 存入列表
        txt_list = [content.rsplit(',') for content in f]
    # for i in txt_list:
    #     print(i)
    # 测试用语
    for j in txt_list:
        print(j)

    # 输入书籍的编号 进行选择
    inputNum = input("please input song`s num:")
    lenTxtList = len(txt_list) # 这个地方不能-1 否则会导致列表遍历不到最后一个元素
    for i in range(lenTxtList):
        if inputNum == txt_list[i][0]: # 匹配到该编号的书籍
            # 输入修改后书籍的所有信息 以逗号为分割符号
            editData = input("Please enter modified song information,Separated by commas: ").rsplit(',')
            # 输出测试
            # print(editData)
            txt_list[i][1]=editData[0]
            txt_list[i][2] = editData[1]
            txt_list[i][3] = editData[2]
            txt_list[i][4] = editData[3]+'\n'
            # 输出测试
            # print(txt_list[i])
    # 修改完成之后调用函数写入到txt
    save_data_txt(txt_list)


if __name__ == '__main__':
    while True:
        show_menu()
        option = input("Please select an option: ").lower()
        if option == "a":
            input_songname_author_year_types()
        elif option == "b":
            show_all_song_information()
        elif option == "c":
            input_song_information()
        elif option == "d":
            delect_a_song()
        elif option == "e":
            modify_information()
        elif option == "f":
            break
        else:
            print(f"Sorry, unknown option: {option}")

