import sys

from elasticsearch_dsl import (Completion, Date, Document, Float, Integer,
                               Keyword, Text, analyzer, connections)

sys.path.append("F:\\vscode-workspace\\HelloSearch")
sys.path.append("F:\\vscode-workspace\\HelloSearch\\Engine")
sys.path.append("F:\\vscode-workspace\\HelloSearch\\config.py")
from config import ES_HOST

connections.create_connection(hosts=[ES_HOST])

my_analyzer = analyzer('ik_smart')


class BlogsIndex(Document):
    suggest=Completion(analyzer=my_analyzer)
    page_url=Keyword()
    title=Text(analyzer="ik_max_word")
    keywords=Text(analyzer="ik_max_word")
    description=Text(analyzer="ik_max_word")
    content=Text(analyzer="ik_max_word")
    PR=Float()
    publish_time=Date()

    class Index:
        name = 'blogs'

    # class Meta:
    #     index = "blogs"
        
if __name__ == "__main__":
    BlogsIndex.init()
