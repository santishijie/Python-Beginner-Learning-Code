def show_messages(lists):
    for list in lists:
        print(list)


def change_list(lists):
    n = 0
    while n < len(lists):
        lists[n] = '学' + lists[n]
        n += 1
    for list in lists:
        print(list)


l = ['python', 'C++', 'go']
show_messages(l)
change_list(l)
