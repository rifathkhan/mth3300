#******************************************************************************
# airlines.py
#******************************************************************************
# Name: Rifat Khan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#NONE
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import pandas as pd

tweet_df = pd.read_csv("tweet.csv")

pos_coeffs = {"great":0.93,"thank":0.87,"thanks":0.71,"love":0.53,"appreciate":0.46}
neut_coeffs = {"do":0.74,"add":0.68,"rt":0.62,"dm":0.51,"can":0.39,"please":0.26}
neg_coeffs = {"worst":1.2,"hours":1.08,"delay":0.97,"no":0.43,"why":0.41}

def predict_sentiment(tweet):
    tweet_list = tweet.lower().split();pos = 0;neut = 0;neg = 0
    for word in tweet_list:
        if word in pos_coeffs:
            pos += pos_coeffs[word]
        elif word in neut_coeffs:
            neut += neut_coeffs[word]
        elif word in neg_coeffs:
            neg += neg_coeffs[word]
        else:
            pass

    sentiment = max(pos,neut,neg)
    
    if pos == sentiment:
        return "positive"
    elif neut == sentiment:
        return "neutral"
    else:
        return "negative"
    
def main():
    
    cols = ['airline_sentiment','text']
    sub_df = tweet_df[cols]
    success = 0
    
    for idx, r in sub_df.iterrows():
        act_sent = r["airline_sentiment"]
        tweet = r["text"]
        
        pred_sent = predict_sentiment(tweet)
        
        if act_sent == pred_sent:
            success += 1
    print("There were {0} out of 4000 tweets ({1}%), where the predicted sentiment matched the actual sentiment".format(success,(success/4000)*100))

main()    
    