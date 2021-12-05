# Пятый бой я продул :(

names = ["Kevin", "Jack", "Mark"]
# statements = ["Kevin-is youngest", "Mark-is not oldest", "Mark-is not youngest", "Jack-is not youngest"]
# statements = ["Kevin-is not youngest", "Mark-is not oldest"]
# statements = ["Kevin-is youngest", "Mark-is oldest"]
statements = ["Kevin-is not youngest", "Jack-is oldest", "Mark-is not oldest"]

# def get_result1(names, statements):
#     dict_statements = {"is youngest": [],
#                        "is not youngest": [],
#                        "is not oldest": [],
#                        "is oldest": []}
#     result_list = []
#     for st in statements:
#         name, status = st.split('-')
#         dict_statements.update({status: name})
#     if dict_statements['is youngest']:
#         result_list.append(dict_statements["is youngest"])
#     if dict_statements["is not oldest"] and dict_statements["is not youngest"]:
#         result_list.append(dict_statements["is not oldest"])
#         result_list.append(dict_statements["is not youngest"])
#     if dict_statements["is not oldest"] and not dict_statements["is not youngest"]:
#         result_list.append(dict_statements["is not oldest"])
#     if not dict_statements["is not oldest"] and dict_statements["is not youngest"]:
#         result_list.append(dict_statements["is not youngest"])
#     for name in names:
#         if name not in list(dict_statements.values()):
#             result_list.append(name)
#
#     if dict_statements["is oldest"]:
#         result_list.append(dict_statements["is oldest"])
#     return result_list


# def get_result(names, statements):
#     dict_statements = {"is youngest": [],
#                        "is not youngest": [],
#                        "is not oldest": [],
#                        "is oldest": []}
#     result_list = []
#     for st in statements:
#         name, status = st.split('-')
#         dict_statements[status].append(name)
#     print(dict_statements)
#
#     for name in names:
#         index = names.index(name)
#         print(list(dict_statements['is youngest']))
#         print(list(dict_statements['is not youngest']))
#         print(list(dict_statements['is not oldest']))
#         print(list(dict_statements['is oldest']))
#         if not dict_statements['is youngest']:
#             if name in list(dict_statements['is not oldest']):
#                 result_list.append(name)
#                 names.pop(index)
#                 print('--------------', names)
#
#
#         elif not dict_statements['is oldest']:
#             if dict_statements['is youngest']:
#                 pass
#             else:
#                 pass
#         # result_list.insert(0, list(dict_statements['is youngest'])[0])
#
#         elif dict_statements['is youngest']:
#             result_list.insert(0, list(dict_statements['is youngest'])[0])
#         elif dict_statements['is oldest']:
#             result_list.insert(-1, list(dict_statements['is youngest'])[0])

def get_result(names, statements):
    list_1 = ["is youngest", "is not youngest", "is not oldest", "is oldest"]
    list_2 = ["is not oldest", "is not youngest", "is oldest"]
    list_3 = ["is youngest", "is not oldest", "is not youngest"]
    list_4 = ["is not oldest", "is not youngest"]
    list_5 = ["is youngest", "is oldest"]

    dict_statements = {"is youngest": [],
                       "is not youngest": [],
                       "is not oldest": [],
                       "is oldest": []}
    result_list = []
    for st in statements:
        name, status = st.split('-')
        dict_statements[status].append(name)
    print(dict_statements)

    for name in names:
        index = names.index(name)
        print(list(dict_statements['is youngest']))
        print(list(dict_statements['is not youngest']))
        print(list(dict_statements['is not oldest']))
        print(list(dict_statements['is oldest']))
        if not dict_statements['is youngest']:
            if name in list(dict_statements['is not oldest']):
                result_list.append(name)
                names.pop(index)
                print('--------------', names)


        elif not dict_statements['is oldest']:
            if dict_statements['is youngest']:
                pass
            else:
                pass
        # result_list.insert(0, list(dict_statements['is youngest'])[0])

        elif dict_statements['is youngest']:
            result_list.insert(0, list(dict_statements['is youngest'])[0])
        elif dict_statements['is oldest']:
            result_list.insert(-1, list(dict_statements['is youngest'])[0])

    return result_list


tt = get_result(names, statements)
print(tt)
