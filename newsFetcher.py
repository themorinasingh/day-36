from newsapi import NewsApiClient

def news_fetcher(stock):
    newsapi = NewsApiClient(api_key='8dd47e88aab14037bcff8d5eb61a15a9')
    top_headlines = newsapi.get_top_headlines(q=stock,
                                              category='business',
                                              language='en',
                                              country='us')

    headline = top_headlines["articles"][0]["title"]
    brief = top_headlines["articles"][0]["description"]
    url = top_headlines["articles"][0]["url"]

    return {"headline":headline, "brief":brief, "url":url}

