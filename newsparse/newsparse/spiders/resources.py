resources = [
        ('Новостной портал nur.kz', 'https://nur.kz/latest, scrolling 4 2',
         'block-infinite js-infinite, div, article-preview-category__content, a',
         'formatted-body__content--wrapper, div',
         'main-headline js-main-headline, h1', '%Y-%m-%dT%H:%M:%S%z, time::attr(datetime)'),
        ('Новостной портал scientificrussia.ru',
         'https://scientificrussia.ru/news, pagination 1134 1130 -1 f"https://scientificrussia.ru/news/{i}"',
         'image, div, , a',
         'article-text, div', ', h1', '%Y-%m-%d %H:%M, time::attr(datetime)'),
        ('Новостной портал tengrinews.kz',
         'https://tengrinews.kz/news, pagination 1 5 1 f"https://tengrinews.kz/news/page/{i}"',
         'tn-article-grid, div, tn-link, a',
         'tn-news-content, div', 'tn-content-title, h1', '(СегодняOrВчераOr%d%b%Y)comma%H:%M, time::text')
]


# Резервные переменные

# nur.kz
# resource_name = 'Новостной портал nur.kz'
# resource_url = 'https://nur.kz/latest, scrolling 4 2'
# top_tag = 'block-infinite js-infinite, div, article-preview-category__content, a'
# bottom_tag = 'formatted-body__content--wrapper, div'
# title_cut = 'main-headline js-main-headline, h1'
# date_cut = '%Y-%m-%dT%H:%M:%S%z, time::attr(datetime)'

# scientificrussia.ru
# resource_name = 'Новостной портал scientificrussia.ru'
# resource_url = 'https://scientificrussia.ru/news, pagination 1134 1130 -1 f"https://scientificrussia.ru/news/{i}"'
# top_tag = 'image, div, , a'
# bottom_tag = 'article-text, div'
# title_cut = ', h1'
# date_cut = '%Y-%m-%d %H:%M, time::attr(datetime)'

# tengrinews.kz
# resource_name = 'Новостной портал tengrinews.kz'
# resource_url = 'https://tengrinews.kz/news, pagination 1 5 1 f"https://tengrinews.kz/news/page/{i}"'
# top_tag = 'tn-article-grid, div, tn-link, a'
# bottom_tag = 'tn-news-content, div'
# title_cut = 'tn-content-title, h1'
# date_cut = '(СегодняOrВчераOr%d%b%Y)comma%H:%M, time::text'
