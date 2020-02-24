import random
import sys


# -----------------------------------------------------------------------------
# NGramModel class ------------------------------------------------------------
# Core functions to implement: prepData, weightedChoice, and getNextToken

class NGramModel(object):

    def __init__(self):
        """
        This is the NGramModel constructor. It sets up an empty
        dictionary as a member variable. It is called from the
        constructors of the NGramModel child classes. This
        function is done for you.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        returns the string to print when you call print on an
        NGramModel object. This function is done for you.
        """
        return 'This is an NGramModel object'

    def prepData(self, text):
        """
        Requires: text is a list of lists of strings
        returns a copy of text where each inner list starts with
        the symbols '^::^' and '^:::^', and ends with the symbol
        '$:::$'. For example, if an inner list in text were
        ['hello', 'goodbye'], that list would become
        ['^::^', '^:::^', 'hello', 'goodbye', '$:::$'] in the
        returned copy.

        Make sure you are not modifying the original text
        parameter in this function.
        """
        textCopy = text[:]

        return textCopy

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        this function populates the self.nGramCounts dictionary.
        It does not need to be modified here because you will
        override it in the NGramModel child classes according
        to the spec.
        """
        return

    def trainingDataHasNGram(self, sentence):
        """
        sentence is a list of strings
        returns a bool indicating whether or not this n-gram model
        can be used to choose the next token for the current
        sentence. This function does not need to be modified because
        you will override it in NGramModel child classes according
        to the spec.
        """
        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        returns the dictionary of candidate next words to be added
        to the current sentence. This function does not need to be
        modified because you will override it in the NGramModel child
        classes according to the spec.
        """
        return {}

    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary; the keys of candidates are items
                  you want to choose from and the values are integers
        returns a candidate item (a key in the candidates dictionary)
        as described in the lesson.
        """
        return

    def getNextToken(self, sentence):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        returns the next token to be added to sentence by calling
        the getCandidateDictionary and weightedChoice functions.
        """
        return ''



# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    choices = { 'the': 2, 'quick': 1, 'brown': 1 }
    nGramModel = NGramModel()
    # add your own testing code here if you like


