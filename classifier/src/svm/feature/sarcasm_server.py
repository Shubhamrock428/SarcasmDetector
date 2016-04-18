# coding=utf-8

import web
from sarcasmApp import run_all_features
  
urls = (
    '/(.*)', 'run_all_features_api'
)
app = web.application(urls, globals())

class run_all_features_api:        
    def GET(self, name):
        print "::::",name
        
        name = name.encode("utf-8")
        
        if not name: 
            return "Please specify a \"query\" like - http://localhost:8080/query"
        
        if name.strip() == "favicon.ico":
            return "YO"
        
        result =  run_all_features(name) 
        print "\n".join(result)

        web.header("Content-Type", "text/html; charset=UTF-8")

        return " <br/>".join(result)

if __name__ == "__main__":
    app.run()
