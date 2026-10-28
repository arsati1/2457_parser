from site_parser.category import CategoryParser
from site_parser.article import ArticleParser
import json
import time
def main():
     category_parser = CategoryParser()
     categories = category_parser.get_categories()

     article_parser = ArticleParser()
     result = {}
     start_time = time.time()
     for category in categories:
         c_name, c_url = category.values()
         category_articles = article_parser.get_category_articles(c_url)
         print(f'Получаем данные из категории: {c_name}')
         result[c_name] = category_articles
     print(f'Выполнено за:{time.time()-start_time}')
     with open('result.json', 'w', encoding='utf-8') as file:
         json.dump(result, file, ensure_ascii=False, indent=4)
main()