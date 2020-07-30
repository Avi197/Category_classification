import ast
import json


def lowercase_and_tolist():
    with open('category.txt', encoding='utf-8') as infile:
        with open('__category__.txt', 'w', encoding='utf-8') as outfile:
            list_list = []
            for line in infile:

                newline = line.strip().lower()
                if newline:
                    list_list.append(f'{newline}')
                else:
                    outfile.write(str(list_list))

                    outfile.write('\n')
                    list_list = []


def to_list():
    # with open('__category__.txt', 'r', encoding='utf-8') as infile:
    with open('category_list.txt', 'w', encoding='utf-8') as outfile:
        list_list = []
        for line in '__category__.txt':
            line = ast.literal_eval(line)
            # line = json.loads(line.strip())
            list_list.append(line)
        outfile.write(str(list_list))

# x = '["thể thao", "bóng đá trong nước", "bóng đá quốc tế", "bóng đá việt nam", "tin chuyển nhượng", "các môn khác",
# "ngoại hạng anh"]' print(json.loads(x)) lowercase_and_tolist()
to_list()
# with open('__category__.txt', 'r', encoding='utf-8') as file:
#     listlist = []
#     for line in file:
#         data = ast.literal_eval(line)
#         print(data)
#         listlist.append(data)
#     print(listlist)
# data = open('__category__.txt', encoding='utf-8')
# data = data.read().strip()
# converted_data = ast.literal_eval(data)
# with open('category_list.txt', 'w', encoding='utf-8') as outfile:
#     outfile.write(converted_data)