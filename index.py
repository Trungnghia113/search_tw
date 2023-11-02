
import requests
import json

bearer_token = 'AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'

def get_twitter_api_guest_token(bearer_token):

    guest_token_response = requests.post(
        "https://api.twitter.com/1.1/guest/activate.json",
        headers={'authorization': f'Bearer {bearer_token}'}
        )
    guest_token = json.loads(guest_token_response.content)['guest_token']
    if not guest_token:
        raise Exception(f"Failed to retrieve guest token")
    return guest_token
def get_info_tw(username):
    url = "https://api.twitter.com/graphql/G6Lk7nZ6eEKd7LBBZw9MYw/UserByScreenName"
    guest_token_response = requests.post(
        "https://api.twitter.com/1.1/guest/activate.json",
        headers={'authorization': f'Bearer {bearer_token}'}
    )
    guest_token = json.loads(guest_token_response.content)['guest_token']
    print('guest_token: ',guest_token)
    headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-guest-token': guest_token,
    }
    params = (
        ('variables', '{"screen_name":"%s","withHighlightedLabel":false}' % username),
    )
    response = requests.get(url, headers=headers, params=params)

    return response.json()
print(get_info_tw('nghiatt'))
