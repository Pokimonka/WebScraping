from datetime import datetime
from functools import wraps


def log(*arg, **kwarg):
    def logger_(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open('logger.log', 'a') as f:
                f.write(str(datetime.now()) + '\n')
                if func.__name__ == 'get_all_articles':
                    f.write('Получили все записи со страницы https://habr.com/ru/articles/ \n')
                elif func.__name__ == 'get_all_articles_where_keywords':
                    words = ', '.join([it for it in arg][0])
                    f.write(f'Отсортировали посты, которые содержат ключевые слова {words} \n')
            return func(*args, **kwargs)
        return wrapper
    return logger_


