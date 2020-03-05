import requests
import random

#Secret key needed to call the API
API_KEY="68941a5169052a35992dab2d8cae9249"
#Starting URL for the API
BASE_URL="https://api.themoviedb.org/3"

#Returns a list of n movie objects from the TMDB service's "top rated" list.
#For other available endpoints see https://developers.themoviedb.org/3/movies/get-movie-details
def getRandomMovies(n):
  popularMovies = getJson('movie/top_rated')['results']
  return random.choices(popularMovies, k=n)

def getResults(url, minResults=50):
  gotResults = 0
  results = []
  while (gotResults < minResults):
    response = getJson(uri)
    totalResults = response['total_results']
    if minResults > totalResults:
      minResults = totalResults
    results += response['results']
    




# Generic function for making an API call to the TMDB service
def getJson(url):
  response = requests.get(url)
  if response.status_code != 200: 
    raise ApiError('GET {} {}'.format(url, response.status_code))
  return response.json()
