from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm'

def clean_str(r):
    r = r.lower()
    r = [c for c in r if c in alphabet]
    return ''.join(r)


with open("ai.txt", encoding="utf-8") as f:
    content = f.read()

class AI:
    def __init__(self, content):
        self.content = content
    
    def start(self):
        self.blocks = self.content.split('\n')
        self.dataset = []
        for block in self.blocks:
            replicas = block.split('\\')[:2]

            if len(replicas) == 2:
                pair = [clean_str(replicas[0]), clean_str(replicas[1])]
                if pair[0] and pair[1]:
                    self.dataset.append(pair)

        self.X_text = []
        self.y = []

        for question, answer in self.dataset:
            self.X_text.append(question)
            self.y += [answer]

        self.vectorizer = CountVectorizer()
        self.X = self.vectorizer.fit_transform(self.X_text)
        self.clf = LogisticRegression()
        self.clf.fit(self.X, self.y)

    def get_func(self, text):
        text_vector = self.vectorizer.transform([text]).toarray()[0]
        question = self.clf.predict([text_vector])[0]
        return question
