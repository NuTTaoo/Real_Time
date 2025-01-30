import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser(interpolation=None)
config_path = r"c:\Users\Naphat\Desktop\Real Time\X_API\config.ini"
config.read(config_path)

client = tweepy.Client(
    bearer_token=config['twitter']['bearer_token'],
    consumer_key=config['twitter']['api_key'], 
    consumer_secret=config['twitter']['api_key_secret'],
    access_token=config['twitter']['access_token'], 
    access_token_secret=config['twitter']['access_token_secret']
)
user = 'Freedom48G'
#limit = 10 #ควรตั้ง Limit ไม่เกิน 100 แต่ตั้งน้อย ดีกว่าเพราะเกิน Limit

# หา user ID
user_id = client.get_user(username=user).data.id

# ดึง tweets
tweets = client.get_users_tweets(
    id=user_id,
    max_results= 10,  # API V2 จำกัดที่ 100 tweets ต่อการเรียก
    tweet_fields=['created_at', 'text']
)

# Create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets.data:
    data.append([user, tweet.text])

df = pd.DataFrame(data, columns=columns)
print(df)