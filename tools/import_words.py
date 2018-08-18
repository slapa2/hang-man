import json
import requests


class Words:

    def __init__(self):
        self.api_url = 'https://pl.wiktionary.org/w/api.php?action=query&list=categorymembers&cmtype=page&' \
                  'cmtitle=Category:J%C4%99zyk+polski+-+rzeczowniki&format=json&cmprop=title&cmlimit=500{}'
        self.cont = ' '
        self.counter = 0
        self.words = list()
        while self.cont:
            self.words.extend(self.get_data())
        else:
            print()


    def get_data(self):
        ret = []
        response = requests.get(self.api_url.format(self.cont))
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            for site in data["query"]["categorymembers"]:
                ret.append(site["title"])

        if "continue" in data:
            self.cont = '&cmcontinue={}'.format(data["continue"]["cmcontinue"])
        else:
            self.cont = None
        self.counter += 1

        print('\r' + str(self.counter) + '...', end='')
        return ret


if __name__ == "__main__":
    words = Words()
    filtered_words = filter(lambda x: x.isalpha() and (' ' not in x) and (True not in map(lambda l: l.isupper(), x)), words.words)

    with open('wiki_nouns.txt', 'w') as f:
        f.write('\n'.join(filtered_words))

