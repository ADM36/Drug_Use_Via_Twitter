import re
import csv
import pandas as pd
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.dicts.emoticons import emoticons
from ekphrasis.classes.segmenter import Segmenter
from nltk.tokenize import TweetTokenizer

def clean_tweets(df):
    # define the text preprocessro
    text_processor = TextPreProcessor(
        # terms that will be normalized
        normalize=['url', 'email', 'money', 'phone', 'time', 'date'],
        # terms that will be annotated
        annotate={"hashtag", "allcaps", "elongated", "repeated",
            'emphasis', 'censored'},
        fix_html=True,  # fix HTML tokens

        # corpus from which the word statistics are going to be used
        # for word segmentation
        segmenter="twitter",

        # corpus from which the word statistics are going to be used
        # for spell correction
        corrector="twitter",

        unpack_hashtags=True,  # perform word segmentation on hashtags
        unpack_contractions=True,  # Unpack contractions (can't -> can not)
        spell_correct_elong=False,  # spell correction for elongated words

        # select a tokenizer. You can use SocialTokenizer, or pass your own
        # the tokenizer, should take as input a string and return a list of tokens
        #tokenizer=SocialTokenizer(lowercase=True).tokenize,
        tokenizer=TweetTokenizer().tokenize,

        # list of dictionaries, for replacing tokens extracted from the text,
        # with other expressions. You can pass more than one dictionaries.
        dicts=[emoticons]
    )
    seg = Segmenter(corpus="twitter")


    tweet_text = df.tweet_text.to_list()

    clean_tweets = []
    for tweet in tweet_text:

        # manually tag usernames
        # ex: @DoctorChristian -> <user> doctor christian </user>
        match = re.findall(r'@\w+', tweet)

        try:
           for at in match:
               user_seg = seg.segment(at[1:])
               tweet = tweet.replace(at, '<user> ' + user_seg + ' </user>')
        except:
            None

        # manually tag all caps so that the unpack_contractions functions works
        match = re.findall(r"(?<![#@$])\b([A-Z][A-Z ,.']*[A-Z])\b", tweet)

        try:
            for all_caps in match:
                tweet = tweet.replace(all_caps, '<allcaps> ' + all_caps.lower() + ' </allcaps>')
        except:
            None

        # manually tag percentages
        match = re.findall(r"(\d+.?\d?%)", tweet)

        try:
            for percent in match:
                tweet = tweet.replace(percent, '<percent> ' + percent[0:len(percent)-1] + ' </percent>')
        except:
            None

        # deal with contractions that the tool misses
        tweet = re.sub(r"(\b)([Ww]hat|[Ii]t|[Hh]e|[Ss]he|[Tt]hat|[Tt]here|[Hh]ow|[Ww]ho|[Hh]ere|[Ww]here|[Ww]hen)'s", r"\1\2 is", tweet)
        tweet = re.sub(r"(\b)([Aa]in)'t", r"is not", tweet)
        tweet = re.sub(r"(\b)([Ww]asn)'t", r"was not", tweet)
        tweet = re.sub(r"(\b)([Hh]e|[Ss]he|[Ii]|[Yy]ou|[Tt]hey|[Ww]e)'d", r"\1\2 would", tweet)
        tweet = re.sub(r"(\b)([Ii]t|[Tt]hat|[Tt]his)'ll", r"\1\2 will", tweet)
        tweet = re.sub(r"(\b)([Cc])'mon", r"come on", tweet)

        # process the rest of the tweet with the nltk tweet tokenizer
        tweet = " ".join(text_processor.pre_process_doc(tweet)).lower()

        clean_tweets.append(tweet)

    # below is code to create the tsv file of cleaned tweets
    df['tweet_text'] = clean_tweets

    return df
