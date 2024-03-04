from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import json

class Data:
    class DataUnit:
        def __init__(self, text, nonsense):
            self.text = text
            self.nonsense = nonsense
    list = []
    texts = []
    labels = []

    def append(self, text, nonsense):
        self.list.append(self.DataUnit(text, nonsense))
        self.texts.append(text)
        self.labels.append(nonsense)


class Model:
    data: Data= Data()
    def __init__(self):
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())
        self.accuracy = 0

    def load_data(self):
        with open('data.json', encoding='utf-8') as f:
            _data = json.load(f)
        for dane in _data:
            self.data.append(dane['text'], dane['nonsense'])

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data.texts, self.data.labels, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self.accuracy = self.model.score(X_test, y_test)

    def predict(self, new_texts):
        return self.model.predict(new_texts)
