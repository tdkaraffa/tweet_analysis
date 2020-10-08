def get_coordinates(location):

	from geopy.geocoders import Nominatim
	geolocator = Nominatim(user_agent='Twitter')
	try:
		coordinates = [geolocator.geocode(location).latitude, geolocator.geocode(location).longitude]
	except AttributeError:
		coordinates = None
	return coordinates

def geo_query(api, search_text, search_coordinates, search_radius='30mi'):
	import tweepy as tw
	if search_coordinates:
		full_search = f'{search_text} geocode:{search_coordinates[0]},{search_coordinates[1]},{search_radius}'
	else:
		full_search = f'{search_text}'

	tweets = [{'ID': tweet.id, 'Query': search_text, 'Date': tweet.created_at, 'Text': tweet.full_text,
			   'User': tweet.user.name,
			   'ScreenName': tweet.user.screen_name, 'Location': tweet.user.location,
			   'NumberRetweets': tweet.retweet_count} for tweet in
			  tw.Cursor(api.search, q=full_search, tweet_mode='extended', lang='en', count=2).items() if
			  (tweet.retweeted == False) & (tweet.full_text[:2] != 'RT')]
	return tweets

