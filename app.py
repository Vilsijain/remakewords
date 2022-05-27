import os
from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/<string:word>')
def split(word):
    

    #replacewords = input("Input: ")
    final = []
    final =  [char for char in word]


    final = ['ee' if x=='e' else x for x in final]
    final = ['z' if x=='s' else x for x in final]


    #print(final)

    f1 = "".join(map(str,final))
    print(f1)
    return f1

if __name__ == '__main__':
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port,debug=True)