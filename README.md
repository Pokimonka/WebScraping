# WebScraping


Разработан парсер главной страницы сайта habr.com, который печатает названия и ссылки тех статей, в названии или содержании которых есть заданные ключевые слова.


## Описание основных функций


get_all_articles - парсит страницу для поиска блоков статей и возвращает список из них.

get_all_articles_where_keywords - анализирует список полученных статей, проверяет есть ли ключевые слова в названии или в содержании и возвращает строку: "время - "Название" - ссылка".
