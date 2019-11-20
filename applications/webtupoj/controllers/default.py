import random

from quote import quote
from os import getenv


def index():
    resp = dict()
    resp["message"] = 'BACKEND_URL=' + getenv("BACKEND_URL", "ya.ru")
    return resp


def quotes():
    resp = dict()

    citations = []
    authors = ["pushkin", "chekhov", "lermontov", "azimov", "pasternak", "bulgakov", "lenin", "strugatsky", "gumilyov", "akhmatova", "fet"]
    for q in quote(random.choice(authors), limit=5):
        row = dict()
        row["author"] = q["author"]
        row["quote"] = q["quote"]
        citations.append(row)

    resp["citations"] = citations
    return resp
