from flask import Flask, request
from flask_restful import Resource, Api

def palindrome(x):
    if len(x) % 2 == 0:
        xref = x[int(len(x)/2):]
        if x[:int(len(x)/2)] == xref[::-1]:
            return "Palindrome hai ye bhai!"
        else:
            return "nhi hai palindrome ye!"
    else:
        xref = x[int(len(x) / 2) + 1:]
        if x[:int(len(x) / 2)] == xref[::-1]:
            return "Palindrome hai ye bhai!"
        else:
            return "nhi hai palindrome ye!"

app = Flask(__name__)
api = Api(app)

class palindrome_class(Resource):
    def get(self, pal_string):
        return {'verdict': palindrome(pal_string)}

api.add_resource(palindrome_class, '/palindrome/<pal_string>')

def sumOfTwo(a,b):
    return int(a)+int(b)

class sumClass(Resource):
    def get(self, int_1, int_2):
        return {'addition': sumOfTwo(int_1, int_2)}

api.add_resource(sumClass, '/sum/<int_1>/<int_2>')

if __name__ == '__main__':
     app.run()
