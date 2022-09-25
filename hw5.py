from task_5_decorator import decor
path = ''


@decor(path)
def count_cycle(args):
    result = 0
    for i in args:
        result += i
    return result


@decor(path)
def count_method(any_list):
    return sum(any_list)


@decor(path)
def printing(a, b, c):
    return a + b + c
