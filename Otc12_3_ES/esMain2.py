# -*- coding:utf-8 -*-
from elasticsearch.client import Elasticsearch

e = Elasticsearch("192.168.0.125:9200")

d = {
  "query":{
    "match_all": {}
  }
}

result = e.search(d, "oct12_menu")
print(result)

for m in result["hits"]["hits"]:
    print(m)