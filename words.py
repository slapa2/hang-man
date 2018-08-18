file_name = 'wiki_nouns.txt'


class Words:

    def __init__(self):
        self.words = self.create_words_list()
        words_len_list = [len(x) for x in self.words]
        self.min_len = min(words_len_list)
        self.max_len = max(words_len_list)

    def create_words_list(self):
        words = []
        with open('dicts/' + file_name, 'r') as f:
            for line in f:
                words.append(line.rstrip())
        return words

    def get_words(self, min_len, max_len):
        ret = list(filter(lambda x: min_len <= len(x) <= max_len, self.words))
        print(len(ret))
        return ret

