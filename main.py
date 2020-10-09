def main():
	from tk import get_keys
	from tweets import geo_query, get_coordinates

	import tweepy as tw

	# ---------- get api keys from locally-stored file -----------#
	keys = get_keys()
	auth = tw.AppAuthHandler(keys['APIKey'], keys['APISecretKey'])
	api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	# ------------------------------------------------------------#

	# USER-SPECIFIED INPUTS
	# ------------------------------------------------------------#
	search_text = 'Trump'
	search_location = 'San Diego'
	# ------------------------------------------------------------#

	search_coordinates = get_coordinates(search_location)
	tweets = geo_query(api, search_text, search_coordinates, search_radius='30mi')
	print(tweets)
	from tweets import clean_text

	for tweet_data in tweets:
		for datum in tweet_data:
			if isinstance(datum, str):
				clean_text(datum)

	from tk import get_db_conn
	db_conn = get_db_conn()
	from db import insert_data_into_db
	insert_data_into_db(tweets, 'twitter', 'tweets', db_conn)


# to do
# cast date into date type
# screenname and numberretweets not being inputted, despite showing up at line 21 print...
# what's happening between those? something with the clean function? something with default values?
# nlp!
# work on cleaning function more


if __name__ == '__main__':
	main()
