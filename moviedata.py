import requests
import random

#Secret key needed to call the API
API_KEY="68941a5169052a35992dab2d8cae9249"
#Starting URL for the API
BASE_URL="https://api.themoviedb.org/3"

#Returns a list of n movie objects from the TMDB service's "top rated" list.
#For other available endpoints see https://developers.themoviedb.org/3/movies/get-movie-details
def getRandomMovies(n, poolSize=50):
  popularMovies = getResults('movie/top_rated',poolSize)
  print(len(popularMovies))
  return random.choices(popularMovies, k=n)

#Queries data from a TMDB endpoint. If the first page doesn't return enough results, it cycles through successive pages until it has the minimum specified.
def getResults(uri, minResults):
  gotResults = 0
  results = []
  page = 0

  while (gotResults < minResults):
    page += 1
    url = "{}/{}?api_key={}&page={}&language=en-US".format(BASE_URL,uri,API_KEY,page)
    response = getJson(url)
    totalResults = response['total_results']
    if minResults > totalResults:
      minResults = totalResults
    newResults = response['results']
    results += newResults
    gotResults += len(newResults)
  return results[:minResults]

# Generic function for making an API call to the TMDB service
def getJson(url):
  response = requests.get(url)
  if response.status_code != 200: 
    raise ApiError('GET {} {}'.format(url, response.status_code))
  return response.json()
