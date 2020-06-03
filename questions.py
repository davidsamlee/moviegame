from moviedata import getRandomMovies
import random


# Simple example function to generate a random multiple choice movie question with three answers.
def questionAndAnswers():
    films = getRandomMovies(3)  # Pick three films at random
    rightAnswerIndex = random.randint(0,2)  # Decide which of the three is right

    return {
        "question": "Which of the following films was released in {}?".format(films[rightAnswerIndex]["release_date"][:4]),
        "answers": list(map(lambda film: film["title"], films)),
        "rightAnswerIndex": rightAnswerIndex
    }
