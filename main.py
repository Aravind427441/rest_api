from flask import Flask
from flask_restful import Api, Resource


app= Flask(__name__)
api=Api(app)

class Helloworld(Resource):
    def get(self,name,test):
        return {"name": name,"test":test}

api.add_resource(Helloworld, "/helloworld/<string:name>/<int:test>")





if __name__=="__main__":
    app.run(debug=True)
