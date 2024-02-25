import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
from wordcloud import WordCloud, STOPWORDS
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def Trading(request):
    company_name = request.data.get('stock_name')
    nltk.download('vader_lexicon') #required for Sentiment Analysis
    now = dt.date.today()
    now = now.strftime('%m-%d-%Y')
    yesterday = dt.date.today() - dt.timedelta(days = 1)
    yesterday = yesterday.strftime('%m-%d-%Y')

    nltk.download('punkt')
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 10

    # save the company name in a variable
  #  company_name = input("Please provide the name of the Company or a Ticker: ")
    #As long as the company name is valid, not empty...
    if company_name != '':
        print(f'Searching for and analyzing {company_name}, Please be patient, it might take a while...')

        #Extract News with Google News
        googlenews = GoogleNews(start=yesterday,end=now)
        googlenews.search(company_name)
        result = googlenews.result()
        #store the results
        df = pd.DataFrame(result)
        print(df)
    try:
        list =[] #creating an empty list 
        for i in df.index:
            dict = {} #creating an empty dictionary to append an article in every single iteration
            article = Article(df['link'][i],config=config) #providing the link
            try:
                article.download() #downloading the article 
                article.parse() #parsing the article
                article.nlp() #performing natural language processing (nlp)
            except:
                pass 
            #storing results in our empty dictionary
            dict['Date']=df['date'][i] 
            dict['Media']=df['media'][i]
            dict['Title']=article.title
            dict['Article']=article.text
            dict['Summary']=article.summary
            dict['Key_words']=article.keywords
            list.append(dict)
        check_empty = not any(list)
        # print (check_empty)
        if check_empty == False:
            news_df=pd.DataFrame(list) #creating dataframe
            print(news_df)

    except Exception as e:
        #exception handling
        print("exception occurred:" + str(e))
        print('Looks like, there is some error in retrieving the data, Please try again or try with a different ticker.' )


    #Sentiment Analysis
    def percentage(part,whole):
        return 100 * float(part)/float(whole)

         #Assigning Initial Values
    positive = 0
    negative = 0
    neutral = 0
    #Creating empty lists
    news_list = []
    neutral_list = []
    negative_list = []
    positive_list = []

     #Iterating over the tweets in the dataframe
    for news in news_df['Summary']:
        news_list.append(news)
        analyzer = SentimentIntensityAnalyzer().polarity_scores(news)
        neg = analyzer['neg']
        neu = analyzer['neu']
        pos = analyzer['pos']
        comp = analyzer['compound']

        if neg > pos:
            negative_list.append(news) #appending the news that satisfies this condition
            negative += 1 #increasing the count by 1
        elif pos > neg:
            positive_list.append(news) #appending the news that satisfies this condition
            positive += 1 #increasing the count by 1
        elif pos == neg:
            neutral_list.append(news) #appending the news that satisfies this condition
            neutral += 1 #increasing the count by 1 

    positive = percentage(positive, len(news_df)) #percentage is the function defined above
    negative = percentage(negative, len(news_df))
    neutral = percentage(neutral, len(news_df))
    #using len(length) function for counting
   # return Response("Positive Sentiment:", '%.2f' % len(positive_list))("Neutral Sentiment:", '%.2f' % len(neutral_list))("Negative Sentiment:", '%.2f' % len(negative_list))
    # print("Neutral Sentiment:", '%.2f' % len(neutral_list), end='\n')
    # print("Negative Sentiment:", '%.2f' % len(negative_list), end='\n')
    return Response({"The given stock today positive sentiment is":positive,"The given stock today negative sentiment is":negative,"The given stock today neutral sentiment is":neutral})
