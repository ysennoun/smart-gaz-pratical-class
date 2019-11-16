import os
from elasticsearch import Elasticsearch

ES01 = os.environ["ES01"]
ES02 = os.environ["ES02"]
INDEX = os.environ["INDEX"]
DOC_TYPE = os.environ["DOC_TYPE"]

def insert_to_es(document: dict={}):
    try:
        print("Insert: " + str(document))
        es = Elasticsearch([ES01, ES02])
        res = es.index(index=INDEX, doc_type=DOC_TYPE, body=document)
        print(res['result'])
    except Exception as ex:
        print(str(ex))
