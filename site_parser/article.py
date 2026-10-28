from .base import BaseParser
class ArticleParser(BaseParser):
    def get_category_articles(self, category_url):
        category_soup = self.get_soup(category_url)

        result = {}
        total_pages = self.__get_total_pages(category_soup)

        for page in range(1, int(total_pages)+1)[:3]:
            _category_url = category_url if page == 1 else f'{category_url}/page/{page}/'
            category_soup = self.get_soup(category_url)
            wrapper = category_soup.find('div', id='content-block')
            items = wrapper.find_all('div', {'class': 'sh-news'})

            result[page] = []
            print(f'Получаем данные со страницы номер: {page}')

        for i in items:
            title = i.find('h2', class_='sh-title').get_text()
            print(title)
            img_url = i.find('img').get('data-src')
            text = i.find('div', class_='sh-text').next.get_text(strip=True)
            side_date = i.find('div', class_='side-date').find_all('span')
            time = side_date[0].get_text()
            if len(side_date) > 1:
                comments = side_date[1].get_text()
            else:
                comments = '0'
            result[page].append({
                'title': title,
                'time': time,
                'comments': comments,
                'img_url': img_url,
                'text': text
            })
        return result
    def get_article_detail(self, article_url):
        pass
    def __get_total_pages(self, page_soup):
        nav = page_soup.find('div', class_='navigation')
        items = nav.find_all('a')
        return items[-1].get_text()
