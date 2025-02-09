import requests
import json
from json_parser import extract_tweet_urls
from env_extract import get_env



def read_messages():
    env = get_env()
    head = {'Authorization': env.DS_AUTH}
    r = requests.get(env.DS_LINK, headers=head)
    tweets = extract_tweet_urls(r.json())
    tweets = dict(sorted(tweets.items()))
    return tweets

if __name__ == '__main__':
    for i in read_messages():
        print(i)

def return_unread(msgs: list[str], latest_msgs: list[str]):
    res = []
    counter = 0
    for i in msgs:
        if i in latest_msgs:
            continue
        if len(latest_msgs)<50:
            counter+=1
        res.append(i)
        latest_msgs.append(i)
    return latest_msgs[counter: ], res


from random import randint
import time


def flow_messages():
    latest_msgs = []
    
    while True:
        sleep_secs = randint(3,8)
        msgs = read_messages()
        latest_msgs, new_msgs = return_unread(latest_msgs=latest_msgs, msgs=msgs)
        if not new_msgs:
            time.sleep(60)
        
        time.sleep(sleep_secs)
        
        