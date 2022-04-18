import pandas as pd
from twilio.rest import Client
import tweepy
import configparser

import main
import experiments.sms_app.keys



class Listener(tweepy.Stream):
    tweets = []
    limit = 1

    def on_status(self, status):
        self.tweets.append(status)

        if len(self.tweets) == self.limit:
            self.disconnect()

stream_tweet = Listener(main.api_key, main.api_key_secret, main.access_token, main.access_token_secret)


users = 'elonmusk'
user_ids = []

for user in users:
    user_ids.append(main.api.get_user(screen_name=users).id)
#
stream_tweet.filter(follow=user_ids)

print(user_ids)
columns = ['User', 'Tweet']
data = []

for tweet in stream_tweet.tweets:
    if not tweet.truncated:
        data.append([tweet.user.screen_name, tweet.text])

# formatting the tweet message in order to use it for twilio app
tweet_name = data[0][0]
tweet_text = data[0][1]
tweet_message = f'{tweet_name} just tweeted: {tweet_text}'


# setting the twilio condition
# for tweet in stream_tweet.tweets:
#     client = Client(experiments.sms_app.keys.account_sid, experiments.sms_app.keys.auth_token)
#     message = client.messages.create(
#         body=tweet_message,
#         from_=experiments.sms_app.keys.twilio_number,
#         to=experiments.sms_app.keys.target_number
#     )
#     print(message.body)
#

# it will print the tweet as table
df = pd.DataFrame(data, columns=columns)
print(df)


