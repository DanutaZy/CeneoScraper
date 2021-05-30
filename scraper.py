import requests
from bs4 import BeautifulSoup
import json
def get_feauture(dom_tree, selector, attribute= None):
    try:
        if isinstance(attribute,str):
            return dom_tree.select_one(selector)[attribute].strip()
        if isinstance(attribute,list):
            return [element.text.strip() for element in dom_tree.select(selector)]
        return dom_tree.select_one(selector).text.strip()
    except (AttributeError,TypeError):
        return None

respons= requests.get('https://www.ceneo.pl/52404834#tab=reviews')

page_dom = BeautifulSoup(respons.text,"html.parser")

opinions= page_dom.select("div.js_product-review")

all_opinions= []

for opinion in opinions:
    single_opinion ={
    "opinion_id": opinion["data-entry-id"],
    "author": get_feauture(opinion,"span.user-post__author-name"),
    "recomm": get_feauture(opinion,"span.user-post__author-recomendation"),
    "stars":get_feauture(opinion,"span.user-post__score-count"),
    "content":get_feauture(opinion,"div.user-post__text"),
    "pros":get_feauture(opinion,"div.review-feature__title--positives ~ .review-feature__item",[]),
    "cons":get_feauture(opinion,"div.review-feature__title--negatives ~ .review-feature__item",[]),
    "useful":get_feauture(opinion,"button.vote-yes > span"),
    "useless":get_feauture(opinion,"button.vote-no > span"),
    "purchased":get_feauture(opinion,"div.review-pz"),
    "publish_date":get_feauture(opinion,"span.user-post__published > time:nth-child(1)","datetime"),
    "purchuse_date":get_feauture(opinion,"span.user-post__published > time:nth-child(2)","datetime"),
    }
    all_opinions.append(single_opinion)
with open("opinions/52404834.json","w",encoding="UTF-8") as jf:
    json.dump(all_opinions,jf, indent=4, ensure_ascii=False)
#print(json.dumps(all_opinions, indent=4, ensure_ascii=False))
#print(page_dom.prettify())
