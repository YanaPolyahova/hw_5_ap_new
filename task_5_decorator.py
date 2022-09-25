import datetime as dt

def decor(path=None):
    def decor_(any_function):
        def new_function(*args):
            start_time = dt.datetime.now()
            print(f'Function {any_function.__name__} has started')
            result = any_function(*args)
            with open(f'{path}logs.txt', 'a') as f:
                f.write(f'Function: {any_function.__name__}, '
                           f'start: {start_time}, '
                           f'result: {result}, '
                           f'args: {args}\n')

            return result

        return new_function

    return decor_
