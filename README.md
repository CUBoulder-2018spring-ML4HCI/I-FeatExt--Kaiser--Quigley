# I-FeatExt--Kaiser--Quigley

Matt Kaiser and Tanner Quigey
- Dependencies: pyOSC, numpy, pandas
- Our goal was to create a simple tool to extract features from JSON data on a users tweets.

- After converting the tweets to JSON for usability we trained our classifer to label tweets with the person who tweeted them. In our case we only used two artists: Waka Flocka Flame and Gucci Mane.
- We created a feature extractor to collect respective metadata from tweets for a specific musical artist. The feature we decided to use was the retweet count number but a classifier could be trained on anything provided by the Twitter API.
- The classifer will label unlabeled tweets as either "Gucci" or "Waka" depending on the number of retweets the unlabeled tweet has.

