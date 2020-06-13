import uuid

from flask import Flask, jsonify, request,render_template, send_file, send_from_directory,json, make_response
from flask_cors import CORS
import os

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

ITEMS = [
    {
        "title":"this is title 1",
        "term" : "girl", 
        "docid" : 1, 
        "content":"hello world girls 1dddddddddddddddddddddddddddddddddddddddd",
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    },
    {
        "title":"this is title 2",
        "term" : "girl2", 
        "content":"hello world girls 2ffffffffffffffffffffffffffffffffffffffff",
        "docid" : 2, 
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    },
    {
        "title":"this is title 3",
        "term" : "girl3", 
        "docid" : 3, 
        "content":"hello world girls 3ggggggggggggggggggggggggggggggggggggggggg",
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    }
]

ITEMS2 = [
    {
        "title":"this is title 4",
        "term" : "boy", 
        "docid" : 4, 
        "content":"hello world boy 3ggggggggggggggggggggggggggggggggggggggggg",
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    },
    {
        "title":"this is title 5",
        "term" : "next", 
        "docid" : 5, 
        "content":"hello world boy next 3ggggggggggggggggggggggggggggggggggggggggg",
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    },
    {
        "title":"this is title 6",
        "term" : "door", 
        "docid" : 6, 
        "content":"hello world girls boy next door 3ggggggggggggggggggggggggggggggggggggggggg",
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    },
    {
        "title":"this is title 7",
        "term" : "boy", 
        "docid" : 7, 
        "content":"hello world boy 3gggggggggggggggggggg",
        "freq" : 27, 
        "tfidf" : 0.6397118528111452, 
        "pagerank" : 0.14018906625922473, 
        "auth" : 0.12787699548690015, 
        "hub" : 0.5154156978600204 
    },
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


#@app.route('/Results', methods=['GET'])
#def all_items():
#    response_object = {'status': 'success'}
#    response_object['items'] = ITEMS
#    return jsonify(response_object)


@app.route('/Results', methods=['GET'])
def all_items():
    response_object = {'status': 'success'}
    query = request.args.get("query")
    algo = request.args.get("algo")
    response_object['algo'] = algo
    if query == "girls" :
        response_object['items'] =ITEMS
        response_object['use_time'] = 123
        response_object['total_count'] =3
    elif query == 'boy':
        response_object['items'] = ITEMS2
        response_object['use_time'] = 233
        response_object['total_count'] = 4
    else :
        response_object['items'] = ITEMS +ITEMS2
        response_object['use_time'] = 77777777
        response_object['total_count'] = 7777777
    #else:
    #    response_object['items'] = []
    #    response_object['use_time'] = -1
    #    response_object['total_count'] = -1  
    return jsonify(response_object)





@app.route('/Wiki', methods=['GET'])
def get_file():
    docid = "0"
    pwd = os.getcwd()
#当前文件的父路径
    father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    directory = father_path + '/data'
    docid = request.args.get("docid")
    print(docid)
    try:
        if docid <="3" :
            response = make_response(send_from_directory(directory, "girls.html", as_attachment=True))
        elif docid <= "6" :
            response = make_response(send_from_directory(directory, "boy.html", as_attachment=True))
        else:
            response = make_response(send_from_directory(directory, "anarchism.html", as_attachment=True))
        return response
    except Exception as e:
        return jsonify({"code": "error", "message": "{}".format(e)})




@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()