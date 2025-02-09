import json

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def extract_tweet_urls(data: json):
    status_dict = {
    'Followed': ["подписался на", 0],
    'Quoted': ["процитировал",1],
    'Tweeted': ['выложил пост',2],
    'Retweeted': ['зарепостил',3],
    'Replied to': ['прокомментировал',4],
    'Pinned': ['закрепил',5]
    }
    tweets = dict()
    for i in data:
        for k in i.get('embeds'):
            if k.get('type') == 'rich':
                id = i.get('id')
                tweets[id] = ['']
                
                title: str = k.get('title')
                if title:
                    for key_word in status_dict:
                        if key_word in title:
                            title = title.replace(key_word, status_dict[key_word][0])
                            tweets[id][0] = status_dict[key_word][1]
                    tweets[id].append(title)
                url = k.get('url')
                if url:
                    tweets[id][1] = f'**[{title}]({url})**\n'
                    # tweets[id].append(k.get('url'))
                desc:str = k.get('description')
                if desc:
                    tweets[id].append(desc_processing(desc))
    return tweets

def desc_processing(desc: str):
    desc = desc.replace('**', '').replace('__', '___').replace('\n', '').replace('>', '\n').replace('- ~~                    ~~', '\n-----------------------')
    return desc

def test_extract():
    a = load_json_file('data.json')
    b = extract_tweet_urls(a)
    tweets = dict(sorted(b.items()))
    return tweets

if __name__ == '__main__':
    a = load_json_file('data.json')[4:40]
    b = extract_tweet_urls(a)
    # print(str(b))
    for i, j in b.items():
        # print(i, '\n'.join(j))
        print(j)
        # for k in j[2].split('>'):
        #     if k:
        #         print(k)
        # print()