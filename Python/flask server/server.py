from flask import Flask, Response, request
import json
import string
import numpy as np


word_counter = {"hello": 1, "hi": 2, "d": 4, "po": 8, "lk": 6, "sd": 5}

app = Flask(__name__)
port = 3100


def format_word(word):
    """(for the extension):
    get a word,
    :returns: the same word, case-ignoring, and without special characters"""
    return ''.join(e for e in word.casefold() if e not in string.punctuation)


@app.route('/sanity')
def index():
    return "Server up and running"


@app.route('/words/<word>')
def words1(word):
    word = format_word(word)
    if word_counter.__contains__(word):  # this word is already in word_counter
        return Response(json.dumps({"count": word_counter[word]}))
    else:
        return Response(json.dumps({'count': 0}))


@app.route('/words', methods=['POST'])  # e.g.: {"word": "hello"} or {"sentence": "hi everyone, my name is Efrat"}
def words():
    if not request.get_json().__contains__("word"):
        # means a sentence is given
        sent = request.get_json()["sentence"]
        words_existed = 0
        words_from_sentence = sent.split(" ")
        for w in words_from_sentence:
            w = format_word(w)
            if word_counter.__contains__(w):
                words_existed += 1
                word_counter[w] += 1
            else:
                word_counter[w] = 1
        return Response(json.dumps({"text": "Added " + str(len(words_from_sentence)) + " words, " +
                                            str(words_existed) + " already existed", "current count": -1}), 201)
    word = format_word(request.get_json()["word"])
    if word_counter.__contains__(word):
        word_counter[word] += 1
    else:
        word_counter[word] = 1
    return Response(json.dumps({"text": "Added " + word, "current count": word_counter[word]}), 201)


@app.route('/total')
def total():
    return Response(json.dumps({"text": "Total count", "count": sum(list(word_counter.values()))}), 201)


@app.route('/delete<word>', methods=['DELETE'])  # e.g.: http://127.0.0.1:3100/deletehello
def dlt(word):
    if word_counter.__contains__(word):
        word_counter.pop(word)
    return Response(json.dumps({"deleted": word}), 201)


@app.route('/update', methods=['PATCH'])  # e.g.: {"old": "hello", "new": "hi"}
def update():
    old, new = request.get_json()["old"], request.get_json()["new"]
    if new != old:
        word_counter[new] = word_counter[old]
        del word_counter[old]
    return Response(json.dumps({"deleted": old}), 201)


@app.route('/popular')
def popular():
    word = ""
    count = 0
    most_popular = max(list(word_counter.values()))
    for key, value in word_counter.items():
        if most_popular == value:
            word = key
            count = value
    return Response(json.dumps({"text": word, "count": count}), 201)


@app.route('/ranking')
def ranking():
    length = 5
    if len(word_counter) < 5:
        length = len(word_counter)
    arr = np.array(list(word_counter.values()))
    idx = (-arr).argsort()[:length]
    res_dict = [{k: v} for k, v in [list(word_counter.items())[i] for i in idx]]
    return Response(json.dumps({"ranking": res_dict}), 201)


if __name__ == '__main__':
    app.run(port=port)


