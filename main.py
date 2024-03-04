# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline
# import json
# import flask
#
#
# #load json from data.json
# with open('data.json', encoding='utf-8') as f:
#     data = json.load(f)
#
# texts = []
# labels = []
# for dane in data:
#     texts.append(dane['text'])
#     labels.append(dane['nonsense'])
#
#
# # Podział danych na zbiór treningowy i testowy
# X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
#
#
# model = make_pipeline(CountVectorizer(), MultinomialNB())
#
#
# model.fit(X_train, y_train)
#
#
# accuracy = model.score(X_test, y_test)
# print("Dokładność modelu:", accuracy)
#
#
# new_texts = ["połanana ławka", "ughejrueiwh re rewrtojre r"]
# predicted_labels = model.predict(new_texts)
#
#
# for text, label in zip(new_texts, predicted_labels):
#     if label == 1:
#         print(f"SPAM: {text}")
#     else:
#         print(f"VALID: {text}")
from model import Model

model =  Model()
model.load_data()
model.train()
print(model.accuracy)
print(model.predict(["połanana ławka", "poiuytrewqLKJHGF DSAPOIUYTREWQ"]))
