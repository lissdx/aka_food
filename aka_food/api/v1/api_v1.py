import json
from aka_food.common import es_driver
from aka_food.common import http_driver
from flask import Blueprint, request, abort, Response
from flask import current_app as app
from aka_food.util.str_util import is_blank

bpv = Blueprint('bpv1', __name__)


@bpv.route('/akafood/health', methods=['GET'])
def index():
    return {'status': 'OK', 'msg': 'strong like a bull'}


@bpv.route('/akafood/find/byingredient/<ingredient>', methods=['GET'])
def find_by_ingredient(ingredient: str = None):
    # check input
    if is_blank(ingredient):
        app.logger.error('ingredient is missing')
        abort(Response(json.dumps({'status': 'ERROR', 'msg': 'missing ingredient'}),
                       status=500,
                       mimetype='application/json',
                       content_type='application/json'))

    # run ES request
    res = es_driver.find_by_ingredient(ingredient=ingredient)
    response_hits = res['hits']['total']['value']
    res_list = []

    # if result found let's format response
    if response_hits > 0:
        for rcp in res['hits']['hits']:
            res_list.append(rcp['_source'])

    return {'status': 'OK', 'msg': f"found: {response_hits}", 'ingredient': ingredient, 'result': res_list}


@bpv.route('/akafood/find/sentence_similarity', methods=['GET'])
def sentence_similarity():
    # check query
    sentence = request.args.get('q')

    # the query should have a value
    if is_blank(sentence):
        app.logger.error('sentence is missing')
        abort(Response(json.dumps({'status': 'ERROR', 'msg': 'missing sentence'}),
                       status=500,
                       mimetype='application/json',
                       content_type='application/json'))

    # run ES search in purpose to
    # find a couple of suitable titles
    es_result = es_driver.find_by_title(sentence)

    # ES result processing
    es_response_hits = es_result['hits']['total']['value']
    sentences = []

    # if ES result is empty nothing to do
    if es_response_hits <= 0:
        app.logger.debug(f"got an empty ES result for sentence: {sentence}")
        return {'status': 'OK', 'msg': f'title not found for sentence: {sentence}', 'sentence': sentence, 'result': []}

    for rcp in es_result['hits']['hits']:
        sentences.append(rcp['_source']['title'])

    # sentences = ["I'm filled with happiness", "I'm happy"]
    # run sentence similarity request
    res = http_driver.sentence_similarity(sentence, sentences)

    if res.status_code != 200:
        app.logger.error('sentence_similarity invalid response')
        abort(Response(
            json.dumps({'status': 'ERROR', 'msg': f"sentence_similarity returns with code: {res.status_code}"}),
            status=500,
            mimetype='application/json',
            content_type='application/json'))

    res_list = []
    for i, s in zip(res.json(), sentences):
        d = {'rank': i, 'sentence': s}
        res_list.append(d)

    return {'status': 'OK', 'msg': f'found {es_response_hits} sentences', 'sentence': sentence, 'result': res_list}
