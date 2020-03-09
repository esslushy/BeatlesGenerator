#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import pickle
from ngramModel import UniGramModel, BiGramModel, TriGramModel

# -----------------------------------------------------------------------------
# Core ------------------------------------------------------------------------
# Functions to implement: trainLyricsModels, selectNGramModel,
# generateSentence, and runLyricsGenerator

def trainLyricsModels(lyricsDirectory):
    """
    loads lyrics data from the dataset/<lyricsDirectory> folder
    using the pre-written DataLoader class, then creates an
    instance of each of the NGramModel child classes and trains
    them using the text loaded from the data loader. The list
    should be in tri-, then bi-, then unigramModel order.

    Returns the list of trained models.
    """
    # Load your data here
    raw_data = pickle.load(open('dataset/' + lyricsDirectory, 'rb'))
    # Construct models
    models = [TriGramModel(), BiGramModel(), UniGramModel()]
    # Process data
    data = models[0].prepData(raw_data)
    # Train each model
    for model in models:
        model.trainModel(data)
    return models

def selectNGramModel(models, sentence):
    """
    Requires: models is a list of NGramModel objects sorted by descending
              priority: tri-, then bi-, then unigrams.
    starting from the beginning of the models list, returns the
    first possible model that can be used for the current sentence
    based on the n-grams that the models know. (Remember that you
    wrote a function that checks if a model can be used to pick a
    word for a sentence!)
    """
    # Find model that works
    for model in models:
        if model.trainingDataHasNGram(sentence):
            return model

def sentenceTooLong(desiredLength, currentLength):
    """
    returns a bool indicating whether or not this sentence should
    be ended based on its length. This function has been done for
    you.
    """
    STDEV = 1
    val = random.gauss(currentLength, STDEV)
    return val > desiredLength

def generateSentence(models, desiredLength):
    """
    Requires: models is a list of trained NGramModel objects sorted by
              descending priority: tri-, then bi-, then unigrams.
              desiredLength is the desired length of the sentence.
    returns a list of strings where each string is a word in the
    generated sentence. The returned list should NOT include
    any of the special starting or ending symbols.
    """
    sentence = ['^::^', '^:::^']
    # Repeat until sentence is long enough
    while(not sentenceTooLong(desiredLength, len(sentence))):
        # Choose model to use
        model = selectNGramModel(models, sentence)
        # Generate next token
        next_token = model.getNextToken(sentence)
        # If token is the end token break out and finish
        if next_token == '$:::$':
            break
        # If it is not the end token, add it to the sentence and continue the loop
        else:
            sentence.append(next_token)
    # Clear off starting tokens
    sentence = sentence[2:]
    return sentence

def printSongLyrics(verseOne, verseTwo, chorus):
    """
    Requires: verseOne, verseTwo, and chorus are lists of lists of strings
    prints the song. This function is done for you.
    """

    verses = [verseOne, chorus, verseTwo, chorus]
    print('\n'),
    for verse in verses:
        for line in verse:
            print (' '.join(line).capitalize())
        print('\n'),

def runLyricsGenerator(models):
    """
    Requires: models is a list of a trained nGramModel child class objects
    generates a verse one, a verse two, and a chorus, then
    calls printSongLyrics to print the song out.
    """
    # Desired length
    DESIRED_LENGTH = 50
    # Generate lyrics
    verseOne = [generateSentence(models, DESIRED_LENGTH) for i in range(4)]
    verseTwo = [generateSentence(models, DESIRED_LENGTH) for i in range(4)]
    chorus = [generateSentence(models, DESIRED_LENGTH) for i in range(4)]
    # Print lyrics
    printSongLyrics(verseOne, verseTwo, chorus)
    return verseOne, verseTwo, chorus

# -----------------------------------------------------------------------------
# Main ------------------------------------------------------------------------

def main():
    lyricsDirectory = 'beatles_songs.pickle'

    print('Starting program and loading data...')
    lyricsModels = trainLyricsModels(lyricsDirectory)
    print('Data successfully loaded\n')

    runLyricsGenerator(lyricsModels)


if __name__ == '__main__':
    main()
    # note that if you want to individually test functions from this file,
    # you can comment out main() and call those functions here. Just make
    # sure to call main() in your final submission of the project!


