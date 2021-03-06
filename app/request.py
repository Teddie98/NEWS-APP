import urllib.request,json
from .models import Sources,Articles
from datetime import datetime

#getting the api key
api_key = None

#getting the news base url
base_url = None

#getting the articlces url
articles_url = None

def configure_request(app):
	global api_key,base_url,articles_url
	api_key = app.config['NEWS_API_KEY']
	import urllib.request,json
from .models import Source,Article
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

Source = Source

Article = Article

api_key = None

news_sources_url = None

articles_url = None

def configure_request(app):
    global api_key,news_sources_url,articles_url
    #Getting api key
    api_key = app.config['NEWS_API_KEY']

    news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]

    articles_url = app.config["SPECIFIC_SOURCE_API_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = news_sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)

    return source_results

def process_source_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Source(id,name,description,category,language)
        source_results.append(source_object)

    return source_results

def get_articles(source_id):
    '''
    Function that gets the json response to our url request for a specific source
    '''
    get_articles_url = articles_url.format(source_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list)

    return articles_results

def process_articles_results(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of source objects
    '''
    article_results = []

    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        article_object = Article(author,title,description,url,image,publishedAt)
        article_results.append(article_object)

    return article_results

def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?language=en&q={}&apiKey={}'.format(article_name,api_key)

    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_articles_results(search_article_list)

    return search_article_resultsbase_url = app.config['NEWS_SOURCES_BASE_URL']
	articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(category, '7a7977d6a91a424eb4b03048da201678')

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results

def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''
	sources_results = []

	for source_item in sources_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')


		sources_object = Sources(id,name,description,url,category,country,language)
		sources_results.append(sources_object)


	return sources_results

def get_articles(id):
    '''
    Function that gets the json Articles response to our url request
    '''
    get_articles_url = base_article_url.format(id,'7a7977d6a91a424eb4b03048da201678')

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results

def process_articles_results(articles_list):
    """
    Function  that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain sources details
    Returns :
        articles_results: A list of source objects
    """
    
    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Articles(id, author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object)

    return articles_results