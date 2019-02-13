from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from bson.json_util import dumps
import json

from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Roy"]


class GetLocations(Resource):
    def get(self):
        values = dumps(users.find())
        newValue = json.loads(values)

        print(values)
        retJson = {
            "status":200,
            "result": newValue
        }

        return jsonify(retJson)


class PostLocations(Resource):
    def post(self):
        users.insert({
            "locations" : [ {
            "name" : "Chennai",
            "state" : "Tamil Nadu",
            "stores" : [ {
              "categories" : [ {
                "category_name" : "Food",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Lays - Sour Cream and Onion",
                  "price" : 35
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Maggi",
                  "price" : 24
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Pringles",
                  "price" : 99
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Pasta",
                  "price" : 40
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "Tomato Soup",
                  "price" : 30
                } ]
              }, {
                "category_name" : "Apparel Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "White Jeans",
                  "price" : 3500
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Jeans",
                  "price" : 3000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Shoes",
                  "price" : 800
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "White Shoes",
                  "price" : 3000
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "White Socks",
                  "price" : 100
                } ]
              }, {
                "category_name" : "Electronic Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Samsung Galaxy S8",
                  "price" : 43000
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPhone SE",
                  "price" : 14000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPad Air 2",
                  "price" : 24000
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple MacBook Pro Retina 15",
                  "price" : 190000
                } ]
              } ],
              "store_id" : 1
            } ]
          }, {
            "name" : "Bengaluru",
            "state" : "Karnataka",
            "stores" : [ {
              "categories" : [ {
                "category_name" : "Food Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Lays - Sour Cream and Onion",
                  "price" : 35
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Maggi",
                  "price" : 24
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Pringles",
                  "price" : 99
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Pasta",
                  "price" : 40
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "Tomato Soup",
                  "price" : 30
                } ]
              }, {
                "category_name" : "Apparel Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "White Jeans",
                  "price" : 3500
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Jeans",
                  "price" : 3000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Shoes",
                  "price" : 800
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "White Shoes",
                  "price" : 3000
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "White Socks",
                  "price" : 100
                } ]
              }, {
                "category_name" : "Electronic Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Samsung Galaxy S8",
                  "price" : 43000
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPhone SE",
                  "price" : 14000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPad Air 2",
                  "price" : 24000
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple MacBook Pro Retina 15",
                  "price" : 190000
                } ]
              } ],
              "store_id" : 1
            } ]
          }, {
            "name" : "Mumbai",
            "state" : "Maharastra",
            "stores" : [ {
              "categories" : [ {
                "category_name" : "Food Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Lays - Sour Cream and Onion",
                  "price" : 35
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Maggi",
                  "price" : 24
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Pringles",
                  "price" : 99
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Pasta",
                  "price" : 40
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "Tomato Soup",
                  "price" : 30
                } ]
              }, {
                "category_name" : "Apparel Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "White Jeans",
                  "price" : 3500
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Jeans",
                  "price" : 3000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Shoes",
                  "price" : 800
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "White Shoes",
                  "price" : 3000
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "White Socks",
                  "price" : 100
                } ]
              }, {
                "category_name" : "Electronic Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Samsung Galaxy S8",
                  "price" : 43000
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPhone SE",
                  "price" : 14000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPad Air 2",
                  "price" : 24000
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple MacBook Pro Retina 15",
                  "price" : 190000
                } ]
              } ],
              "store_id" : 1
            } ]
          }, {
            "name" : "Delhi",
            "state" : "Delhi",
            "stores" : [ {
              "categories" : [ {
                "category_name" : "Food Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Lays - Sour Cream and Onion",
                  "price" : 35
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Maggi",
                  "price" : 24
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Pringles",
                  "price" : 99
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Pasta",
                  "price" : 40
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "Tomato Soup",
                  "price" : 30
                } ]
              }, {
                "category_name" : "Apparel Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "White Jeans",
                  "price" : 3500
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Jeans",
                  "price" : 3000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Black Shoes",
                  "price" : 800
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "White Shoes",
                  "price" : 3000
                }, {
                  "_id" : 5,
                  "image_url" : "xxx.yzz",
                  "name" : "White Socks",
                  "price" : 100
                } ]
              }, {
                "category_name" : "Electronic Items",
                "items" : [ {
                  "_id" : 1,
                  "image_url" : "xxx.yzz",
                  "name" : "Samsung Galaxy S8",
                  "price" : 43000
                }, {
                  "_id" : 2,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPhone SE",
                  "price" : 14000
                }, {
                  "_id" : 3,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple iPad Air 2",
                  "price" : 24000
                }, {
                  "_id" : 4,
                  "image_url" : "xxx.yzz",
                  "name" : "Apple MacBook Pro Retina 15",
                  "price" : 190000
                } ]
              } ],
              "store_id" : 1
            } ]
        }, {
        "name" : "Hyderabad",
        "state" : "Telangana",
        "stores" : [ {
          "categories" : [ {
            "category_name" : "Food Items",
            "items" : [ {
              "_id" : 1,
              "image_url" : "xxx.yzz",
              "name" : "Lays - Sour Cream and Onion",
              "price" : 35
            }, {
              "_id" : 2,
              "image_url" : "xxx.yzz",
              "name" : "Maggi",
              "price" : 24
            }, {
              "_id" : 3,
              "image_url" : "xxx.yzz",
              "name" : "Pringles",
              "price" : 99
            }, {
              "_id" : 4,
              "image_url" : "xxx.yzz",
              "name" : "Pasta",
              "price" : 40
            }, {
              "_id" : 5,
              "image_url" : "xxx.yzz",
              "name" : "Tomato Soup",
              "price" : 30
            } ]
          }, {
            "category_name" : "Apparel Items",
            "items" : [ {
              "_id" : 1,
              "image_url" : "xxx.yzz",
              "name" : "White Jeans",
              "price" : 3500
            }, {
              "_id" : 2,
              "image_url" : "xxx.yzz",
              "name" : "Black Jeans",
              "price" : 3000
            }, {
              "_id" : 3,
              "image_url" : "xxx.yzz",
              "name" : "Black Shoes",
              "price" : 800
            }, {
              "_id" : 4,
              "image_url" : "xxx.yzz",
              "name" : "White Shoes",
              "price" : 3000
            }, {
              "_id" : 5,
              "image_url" : "xxx.yzz",
              "name" : "White Socks",
              "price" : 100
            } ]
          }, {
            "category_name" : "Electronic Items",
            "items" : [ {
              "_id" : 1,
              "image_url" : "xxx.yzz",
              "name" : "Samsung Galaxy S8",
              "price" : 43000
            }, {
              "_id" : 2,
              "image_url" : "xxx.yzz",
              "name" : "Apple iPhone SE",
              "price" : 14000
            }, {
              "_id" : 3,
              "image_url" : "xxx.yzz",
              "name" : "Apple iPad Air 2",
              "price" : 24000
            }, {
              "_id" : 4,
              "image_url" : "xxx.yzz",
              "name" : "Apple MacBook Pro Retina 15",
              "price" : 190000
            } ]
          } ],
          "store_id" : 1
           } ]
       } ]
            })
        return "hello world"

api.add_resource(PostLocations,"/postlocations")
api.add_resource(GetLocations,"/getlocations")

if __name__=="__main__":
    app.run(host='0.0.0.0')
















'''

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'number_of_users':0
})


class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['number_of_users']
        new_num = 1 + prev_num
        UserNum.update({},{"$set":{"number_of_users":new_num}})
        return str("hello user " + str(new_num))


def checkPostedData(postedData, functionName):
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301 #Missing parameter
        else:
            return 200
    elif (functionName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #If I am here, then the resouce Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "add")
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Add the posted data
        ret = x+y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        #If I am here, then the resouce Subtract was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "subtract")


        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Subtract the posted data
        ret = x-y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        #If I am here, then the resouce Multiply was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "multiply")


        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Multiply the posted data
        ret = x*y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        #If I am here, then the resouce Divide was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "division")


        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Multiply the posted data
        ret = (x*1.0)/y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)



api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")
api.add_resource(Visit , "/hello")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(host = '0.0.0.0')
'''
