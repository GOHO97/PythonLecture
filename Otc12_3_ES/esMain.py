# -*- coding:utf-8 -*-
from elasticsearch.client import Elasticsearch

e = Elasticsearch("192.168.0.125:9200")

d = {
  "name":"소고기김밥",
  "price":5000
}

result = e.index("oct12_menu", d)
print(result)