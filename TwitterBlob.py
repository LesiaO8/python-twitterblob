import tweepy
from textblob import TextBlob
import argparse
import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

parser = argparse.ArgumentParser()
parser.add_argument("keyword")
parser.add_argument("--file", default = 0)
parser.add_argument("--count", default = 1000)
args = parser.parse_args()
to_find = args.keyword
save_file = args.file

if save_file != 0:
    ofile  = open(args.file, "w")
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

def auth():
    consumer_key = 'YOUR_KEY_HERE'
    consumer_secret = 'YOUR_KEY_HERE'

    access_token = 'YOUR_KEY_HERE'
    access_token_secret = 'YOUR_KEY_HERE'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def print_graph(X, Y, line, total_polarity, total_subjectivity):
    plt.plot(X, Y, 'bo', X, line, 'r--', total_polarity, total_subjectivity, 'ys')
    plt.title('Analysis for \"' + to_find + '\"')
    plt.axes().get_xaxis().set_ticks([-1, -0.5, 0, 0.5, 1])
    plt.axes().get_yaxis().set_ticks([0, 0.25, 0.5, 0.75, 1])

    plt.axes().set_xlim([-1, 1])
    plt.axes().set_ylim([0, 1])

    plt.xlabel('polarity')
    plt.ylabel('subjectivity')
    plt.show()

def search_tweets(api, query, max_tweets = int(args.count)):
    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q = query, count = count, max_id = str(last_id - 1), lang = 'en')
            if not new_tweets:
                break
            searched_tweets.extend(tweet.text for tweet in new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            break
    return list(set(searched_tweets))

api = auth()
public_tweets = search_tweets(api, to_find)
i = 0
total_polarity = 0
total_subjectivity = 0
tweet_sentiments = []

for tweet in public_tweets:
    i += 1
    print("Tweet " + str(i) + "/" + str(len(public_tweets)) + ":")
    print(tweet[0:80] + "\n")
    analysis = TextBlob(tweet)
    tweet_sentiments.append([analysis.sentiment.polarity, analysis.sentiment.subjectivity])
    total_polarity += analysis.sentiment.polarity
    total_subjectivity += analysis.sentiment.subjectivity
    if save_file != 0:
        writer.writerow([analysis.sentiment.polarity, analysis.sentiment.subjectivity])

total_polarity /= len(public_tweets)
total_subjectivity /= len(public_tweets)

print('\nAverage sentiment polarity for \"' + to_find + '\" is '+ str(total_polarity / len(public_tweets)))
print('Average sentiment subjectivity for \"' + to_find + '\" is '+ str(total_subjectivity / len(public_tweets)))

X = np.zeros(0)
Y = np.zeros(0)

for tweet in tweet_sentiments:
    X = np.append(X, tweet[0])
    Y = np.append(Y, tweet[1])

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
line = slope * X + intercept

print_graph(X, Y, line, total_polarity, total_subjectivity)
