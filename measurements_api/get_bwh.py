#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_bwh(name):
    from SPARQLWrapper import SPARQLWrapper, JSON
 
    sparql = SPARQLWrapper("http://ja.dbpedia.org/sparql")
    sparql.setQuery("""
    SELECT ?b ?w ?h
WHERE {
  <http://ja.dbpedia.org/resource/%s> <http://ja.dbpedia.org/property/バスト> ?b ;
        <http://ja.dbpedia.org/property/ウエスト> ?w ;
        <http://ja.dbpedia.org/property/ヒップ> ?h .
}
""" % name)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()


    for result in results["results"]["bindings"]:
        b = float(result['b']['value'])
        w = float(result['w']['value'])
        h = float(result['h']['value'])
        return b, w, h



if __name__ == '__main__':
    import sys
    name = sys.argv[1]

    b, w, h = get_bwh(name)

    print "%sのスリーサイズは上から%dcm、%dcm、%dcmです！" % (name, b, w, h)

    
