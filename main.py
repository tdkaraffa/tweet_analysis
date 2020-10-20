def main():
	from tk import get_keys
	from tweetSearch import geo_query, get_coordinates
	import tweepy as tw

	# ---------- get api keys from locally-stored file -----------#
	keys = get_keys()
	auth = tw.AppAuthHandler(keys['APIKey'], keys['APISecretKey'])
	api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=False)
	# ------------------------------------------------------------#

	# USER-SPECIFIED INPUTS
	# ------------------------------------------------------------#
	search_list = ['Trump', 'Biden']
	search_location = 'San Diego'
	# ------------------------------------------------------------#

	from tk import get_db_conn
	db_conn = get_db_conn()
	from db import insert_data_into_db
	search_coordinates = get_coordinates(search_location)
	for search_text in search_list:
		tweets = geo_query(api, search_text, search_coordinates, search_radius='30mi')
		from tweetSearch import clean_text
		for tweet_data in tweets:
			for datum in tweet_data:
				if isinstance(datum, str):
					clean_text(datum)
		insert_data_into_db(tweets, 'twitter', 'tweets', db_conn)

# to do
# cast date into date type
# nlp!
# work on cleaning function more

if __name__ == '__main__':
	main()
