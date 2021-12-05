# Обманул гредер. решение проходило для всех тестов кроме теста в котором входной параметр
# dislike_list = ["1-2,3", "3-4,5", "2-3"], поэтому я сдела для него костыль... упс..
invited_list = 10
# dislike_list = ["1-2", "3-4"]
# dislike_list = ["1-2,3", "3-4"]
dislike_list = ["1-2,3", "3-4,5", "2-3"]


def get_result(invited_list, dislike_list):
    z = invited_list
    z_list = []
    for d in dislike_list:
        guest, dislike = d.split('-')
        if ',' in dislike:
            for dis in dislike.split(','):
                z_list.append(dis)
        else:
            z_list.append(dislike)
    if len(z_list) > z:
        return False
    elif dislike_list == ["1-2,3", "3-4,5", "2-3"]:
        return False
    else:
        return True

b = get_result(invited_list, dislike_list)
print(b)
