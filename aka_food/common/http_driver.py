from flask import current_app as app
import requests


class SentenceSimilarityDriver:
    _client = None
    _url = None
    _headers = None
    _method = None

    def __init__(self, url, token):
        self._method = 'POST'
        self._token = token
        self._url = url
        self._headers = {"Authorization": f"Bearer {token}"}

    def sentence_similarity(self, source_sentence, sentences):
        payload = {"inputs": {
            "source_sentence": source_sentence,
            "sentences": sentences
        }
        }

        return requests.post(self._url, headers=self._headers, json=payload)


http_driver = SentenceSimilarityDriver(url=app.config['HF_URL'],
                                       token=app.config['HF_TOKEN'])
