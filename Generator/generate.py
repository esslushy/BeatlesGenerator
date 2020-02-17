#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from unigramModel import *
from bigramModel import *
from trigramModel import *

# -----------------------------------------------------------------------------
# Core ------------------------------------------------------------------------
# Functions to implement: trainLyricsModels, selectNGramModel,
# generateSentence, and runLyricsGenerator

def trainLyricsModels(lyricsDirectory):
    """
    loads lyrics data from the data/lyrics/<lyricsDirectory> folder
    using the pre-written DataLoader class, then creates an
    instance of each of the NGramModel child classes and trains
    them using the text loaded from the data loader. The list
    should be in tri-, then bi-, then unigramModel order.

    Returns the list of trained models.
    """
    #Load your data here
    
    models = [TrigramModel(), BigramModel(), UnigramModel()]

    # add rest of trainLyricsModels implementation here

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
    return

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

    # add rest of generateSentence implementation here

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
            print (' '.join(line)).capitalize()
        print('\n'),

def runLyricsGenerator(models):
    """
    Requires: models is a list of a trained nGramModel child class objects
    generates a verse one, a verse two, and a chorus, then
    calls printSongLyrics to print the song out.
    """
    verseOne = []
    verseTwo = []
    chorus = []

    # add rest of runLyricsGenerator implementation here

    return

# -----------------------------------------------------------------------------
# Main ------------------------------------------------------------------------

def main():
    lyricsDirectory = 'the_beatles'

    print('Starting program and loading data...')
    lyricsModels = trainLyricsModels(lyricsDirectory)
    print('Data successfully loaded\n')

    runLyricsGenerator(lyricsModels)


if __name__ == '__main__':
    main()
    # note that if you want to individually test functions from this file,
    # you can comment out main() and call those functions here. Just make
    # sure to call main() in your final submission of the project!


