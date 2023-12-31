from flask import current_app as app
from aka_food.exception import AkaFoodDbConnectionError
from elasticsearch import Elasticsearch


# # Create the client instance
# client = Elasticsearch("http://localhost:9200")
#
# # Successful response!
# client.info()


class ESDriver:
    _client = None

    def __init__(self, host, port):
        self._client = Elasticsearch(f"http://{host}:{port}")
        if not self._client.ping():
            raise AkaFoodDbConnectionError(f"client.ping() returns FALSE. info: {self._client.info()}")

    def find_by_ingredient(self, ingredient: str):
        q = {
            "query": {
                "fuzzy": {
                    "ingredients": {
                        "value": ingredient,
                        "fuzziness": 1
                    }
                }
            }
        }
        return self._client.search(**q, size=10)

    def find_by_title(self, title: str):
        q = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "bool": {
                                "should": [
                                    {
                                        "match": {
                                            "title": title
                                        }
                                    }
                                ],
                                "minimum_should_match": 1
                            }
                        }
                    ]
                }
            }
        }
        return self._client.search(**q, size=10)

    def get_client(self):
        return self._client


es_driver = ESDriver(host=app.config['ES_HOST'], port=app.config['ES_PORT'])
