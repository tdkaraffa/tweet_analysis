def main():
	from secret import get_keys
	from tweets import geo_query, get_coordinates

	import tweepy as tw

	#---------- get api keys from locally-stored file -----------#
	keys = get_keys()
	auth = tw.AppAuthHandler(keys['APIKey'], keys['APISecretKey'])
	api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	#------------------------------------------------------------#

	# USER-SPECIFIED INPUTS
	#------------------------------------------------------------#
	search_text = 'Trump'
	search_location = 'San Diego'
	#------------------------------------------------------------#

	search_coordinates = get_coordinates(search_location)
	tweets = geo_query(api, search_text, search_coordinates, search_radius='30mi')
	print(tweets)
if __name__=='__main__':
	main()