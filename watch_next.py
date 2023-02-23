# Loading the spacy model.
import spacy

nlp = spacy.load("en_core_web_md")

# Creating a spacy object.
init_movie = nlp(
    """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him in to space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"""
)

# Initializing the variables.
movies_list = []
highest_similarity = -1
similar_sentence = ""

# Reading the movies.txt file and appending the second part of the line to the movies_list.
with open("movies.txt") as movies:
    for i in movies:
        i_split = i.strip("\n").split(":")
        movies_list.append(i_split[1])

# Comparing the similarity of the sentence in the movies_list to the init_movie.
for sentence in movies_list:

    similarity = nlp(sentence).similarity(init_movie)
    if similarity > highest_similarity:
        highest_similarity = similarity
        similar_sentence = sentence
print(similar_sentence, highest_similarity)
