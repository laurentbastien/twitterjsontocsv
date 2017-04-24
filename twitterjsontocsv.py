import json
import os
path_to_json = 'pathtofile'
import csv
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
with open("thursday.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["created_at", "hashtag", "url", "text", "user_mentions", "favorite_count", "id", "in_reply_to_screen_name", "retweet_count", "retweeted","usercreated", "userdescription", "userfavoritescount", "userfollowers", "userfriends", "userid", "userlang", "listedcount", "location", "name", "screen_name", "statuses_count", "time_zone", "verified"])
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            for line in json_file:
                text = " "
                myurl = " "
                d = json.loads(line)
                for a in d["entities"]["hashtags"]:
                    if "text" in a:
                        text = a["text"]
                if "entities" in d and "urls" in d["entities"]:
                    for o in d['entities']['urls']:
                        myurl = o["expanded_url"]
                writer.writerow([
                    d["created_at"],
                    text,
                    myurl,
                    d["text"],
                    d["entities"]["user_mentions"],
                    d["favorite_count"],
                    d["id"],
                    d["in_reply_to_screen_name"],
                    d["retweet_count"],
                    d["retweeted"],
                    d["user"]["created_at"],
                    d["user"]["description"],
                    d["user"]["favourites_count"],
                    d["user"]["followers_count"],
                    d["user"]["friends_count"],
                    d["user"]["id"],
                    d["user"]["lang"],
                    d["user"]["listed_count"],
                    d["user"]["location"],
                    d["user"]["name"],
                    d["user"]["screen_name"].encode("utf8"),
                    d["user"]["statuses_count"],
                    d["user"]["time_zone"],
                    d["user"]["verified"]])
                
    