from quote import quote


def index():
    resp = dict()
    resp["welcome"] = 'Welcome to web2py!'
    resp["message"] = 'Hello World!!!'
    return resp


def quotes():
    resp = dict()

    citations = []
    for q in quote('Pushkin', limit=5):
        row = dict()
        row["author"] = q["author"]
        row["quote"] = q["quote"]
        citations.append(row)

    resp["citations"] = citations
    return resp
