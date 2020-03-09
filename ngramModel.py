import random
import sys
import warnings

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

    def prepData(self, lyrics):
        """
        Requires: lyrics is a list of lists of strings
        returns a copy of lyrics where each inner list starts with
        the symbols '^::^' and '^:::^', and ends with the symbol
        '$:::$'. For example, if an inner list in lyrics were
        ['hello', 'goodbye'], that list would become
        ['^::^', '^:::^', 'hello', 'goodbye', '$:::$'] in the
        returned copy.

        Make sure you are not modifying the original lyrics
        parameter in this function.
        """
        # Store data
        processed_lyrics = []
        for lyric in lyrics:
            # Copy text
            lyric_copy = lyric[:]
            # Add the beginning tokens
            lyric_copy.insert(0, '^::^')
            lyric_copy.insert(1, '^:::^')
            # Add the end tokens
            lyric_copy.append('$:::$')
            # Add to final array
            processed_lyrics.append(lyric_copy)
        return processed_lyrics

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
        Requires: sentence is a list of strings
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
                  you want to choose from and the values are probability floats
        returns a candidate item (a key in the candidates dictionary)
        as described in the lesson.

        This function works by giving each possible candidate a stretch the size of its probability
        from 0 to 1 so that it is truncated proportionally for each candidate and the random number
        that lands in a certain truncated section chooses that candidate. 
        """
        # Get a random number between 0 and 1
        rand_num = random.random()
        # Sums all probabilities
        total_probabilities = 0
        for key, value in candidates.items():
            # Increment total probabilities by the probability for the key
            total_probabilities += value
            # Check if the summed probabilities are equal to or greater than the random number
            if total_probabilities >= rand_num:
                # If they are return the word
                return key
        # In case all fails, have an emergency empty output.
        return ''

    def getNextToken(self, sentence):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        returns the next token to be added to sentence by calling
        the getCandidateDictionary and weightedChoice functions.
        """
        return self.weightedChoice(self.getCandidateDictionary(sentence))


class UniGramModel(NGramModel):

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Populates the self.nGramCounts dictionary with unigrams
        """
        # Loop through each line of lyrics
        for lyrics in text:
            # Loop through each word of the lyrics
            for word in lyrics:
                # If the word already exists, increment by 1
                if word in self.nGramCounts:
                    self.nGramCounts[word] += 1
                # If the word doesn't exist, add an entry to the nGram dictionary
                else:
                    self.nGramCounts[word] = 1

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Always true as the model doesn't use context
        """
        return True


    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        returns a dictionary of words to be added to the next sentence
        with the probability that each word would be added
        """
        # Sums all the counts of words
        total_words = sum(self.nGramCounts.values())
        # Make copy of dictionary
        candidate_dictionary = self.nGramCounts.copy()
        # Divides all counts of words by total words to get probability
        for key in candidate_dictionary:
            candidate_dictionary[key] /= total_words
        return candidate_dictionary

class BiGramModel(NGramModel):

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Populates the self.nGramCounts dictionary with bigrams
        """
        # Loop through each line of lyrics
        for lyrics in text:
            # Loop through each pair of words in the lyrics. Start at 0 and go to the 2nd to last word.
            for i in range(len(lyrics)-1):
                # Get the primary word
                word = lyrics[i]
                # Get the following word
                next_word = lyrics[i+1]
                # If the word already exists check to see if the following word exists. If it does, increment by 1
                if word in self.nGramCounts:
                    if next_word in self.nGramCounts[word]:
                        self.nGramCounts[word][next_word] += 1
                    # If the following word does not exist, add a new entry to the dictionary.
                    else:
                        self.nGramCounts[word][next_word] = 1
                # If the word doesn't exist, add an entry to the nGram dictionary
                else:
                    self.nGramCounts[word] = {next_word: 1}

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Returns true if the last word of the sentence exists in the self.nGramCounts
        """
        return sentence[-1] in self.nGramCounts

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        returns a dictionary of words to be added to the next sentence
        with the probability that each word would be added
        """
        # Make sure data has the ngram being searched for. If not, return an empty dictionary.
        if not self.trainingDataHasNGram(sentence):
            warnings.warn('There is no Ngram with that value in the dataset.')
            return {'$:::$': 1}
        # Make copy of dictionary related to the final word of the sentence
        candidate_dictionary = self.nGramCounts[sentence[-1]].copy()
        # Sum all possible word choices in the dictionary
        total_words = sum(candidate_dictionary.values())
        # Divides all counts of words by total words to get probability
        for key in candidate_dictionary:
            candidate_dictionary[key] /= total_words
        return candidate_dictionary

class TriGramModel(NGramModel):

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Populates the self.nGramCounts dictionary with bigrams
        """
        # Loop through each line of lyrics
        for lyrics in text:
            # Loop through each set of 3 words in the lyrics. Start at 0 and go to the 3rd to last word.
            for i in range(len(lyrics)-2):
                # Get the first word
                first_word = lyrics[i]
                # Get the second word
                second_word = lyrics[i+1]
                # Get the third word
                third_word = lyrics[i+2]
                # If the first word already exists check to see if the following words exist
                if first_word in self.nGramCounts:
                    # Check if the second word exists
                    if second_word in self.nGramCounts[first_word]:
                        # Check if the third word exists. If it does, increment by 1
                        if third_word in self.nGramCounts[first_word][second_word]:
                            self.nGramCounts[first_word][second_word][third_word] += 1
                        # If the third word does not exist, add a new entry to the dictionary
                        else:
                            self.nGramCounts[first_word][second_word][third_word] = 1
                    # If the second word does not exist, add a new entry to the dictionary.
                    else:
                        self.nGramCounts[first_word][second_word] = {third_word: 1}
                # If the word doesn't exist, add an entry to the nGram dictionary
                else:
                    self.nGramCounts[first_word] = {second_word: {third_word: 1}}

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Returns true if the 2nd to last word of the sentence exists in the self.nGramCounts and 
        the last word exists in self.nGramCounts[second_to_last_word]
        """
        return sentence[-2] in self.nGramCounts and sentence[-1] in self.nGramCounts[sentence[-2]]

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        returns a dictionary of words to be added to the next sentence
        with the probability that each word would be added
        """
        # Make sure data has the ngram being searched for. If not, return an empty dictionary.
        if not self.trainingDataHasNGram(sentence):
            warnings.warn('There is no Ngram with that value in the dataset.')
            # Return a terminating dictionary option
            return {'$:::$': 1}
        # Make copy of dictionary related to the final 2 words of the sentence
        candidate_dictionary = self.nGramCounts[sentence[-2]][sentence[-1]].copy()
        # Sum all possible word choices in the dictionary
        total_words = sum(candidate_dictionary.values())
        # Divides all counts of words by total words to get probability
        for key in candidate_dictionary:
            candidate_dictionary[key] /= total_words
        return candidate_dictionary

# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    choices = { 'the': 2, 'quick': 1, 'brown': 1 }
    nGramModel = TriGramModel()
    # add your own testing code here if you like
    data = nGramModel.prepData(text)
    nGramModel.trainModel(data)
    print(nGramModel.getCandidateDictionary(['the', 'lazy']))
    print(nGramModel.getNextToken(['the', 'lazy']))