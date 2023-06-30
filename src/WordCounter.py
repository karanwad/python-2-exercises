class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        self.count = len(self.sentence.split())
    
    def get_word_count(self):
        return len(self.sentence.split())
    
    def get_shortest_word(self):
        words = self.sentence.split()
        return (min(len(eachWord) for eachWord in words))
    
    def get_longest_word(self):
        words = self.sentence.split()
        return max(len(eachWord) for eachWord in words)