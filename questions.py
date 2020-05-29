from moviedata import getRandomMovies

# Simple example function to generate a random multiple choice movie question with three answers.
def questionAndAnswers():
    film = getRandomMovies(1)[0] # Pick a single movie at random
    yearReleased = int(film["release_date"][:4]) # Get the release date, take the first 4 characters (the year), and convert from string to a number
    return {
        "question":
        "Which year was the movie {} released?".format(film["title"]),
        "answers": [yearReleased - 2, yearReleased, yearReleased + 2],
        "rightAnswerIndex": 1
    }
