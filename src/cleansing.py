import json

def clean(data):

    d = json.loads(data)

    keys = d.keys()
    r = {}

    if d['truncated'] == False:
        r['text'] = d['text']
    else:
        r['text'] = d['extended_tweet']['full_text']

    r['id_str'] = d['id_str']
    r['timestamp_ms'] = d['timestamp_ms']

    if 'user' in keys:
        r['user'] = {}
        r['user']['user_id'] = d['user']['id_str']
        r['user']['name'] = d['user']['name']
        r['user']['screen_name'] = d['user']['screen_name']
        r['user']['followers_count'] = d['user']['followers_count']
        r['user']['friends_count'] = d['user']['friends_count']
        r['user']['listed_count'] = d['user']['listed_count']
        r['user']['statuses_count'] = d['user']['statuses_count']

    if 'retweeted_status' in keys:
        r['retweeted_status'] = {}
        r['retweeted_status']['id_str'] = d['retweeted_status']['id_str']
        r['retweeted_status']['created_at'] = d['retweeted_status']['created_at']

        if d['retweeted_status']['truncated'] == False:
            r['retweeted_status']['text'] = d['retweeted_status']['text']
        else:
            r['retweeted_status']['text'] = d['retweeted_status']['extended_tweet']['full_text']

        r['retweeted_status']['user'] = {}
        r['retweeted_status']['user']['id_str'] = d['retweeted_status']['user']['id_str']
        r['retweeted_status']['user']['name'] = d['retweeted_status']['user']['name']
        r['retweeted_status']['user']['screen_name'] = d['retweeted_status']['user']['screen_name']
        r['retweeted_status']['user']['followers_count'] = d['retweeted_status']['user']['followers_count']
        r['retweeted_status']['user']['friends_count'] = d['retweeted_status']['user']['friends_count']
        r['retweeted_status']['user']['listed_count'] = d['retweeted_status']['user']['listed_count']
        r['retweeted_status']['user']['statuses_count'] = d['retweeted_status']['user']['statuses_count']

        r['retweeted_status']['quote_count'] = d['retweeted_status']['quote_count']
        r['retweeted_status']['reply_count'] = d['retweeted_status']['reply_count']
        r['retweeted_status']['retweet_count'] = d['retweeted_status']['retweet_count']
        r['retweeted_status']['favorite_count'] = d['retweeted_status']['favorite_count']

    return json.dumps(r)


