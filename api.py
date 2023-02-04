from flask import Flask, render_template, jsonify, request

app = Flask (__name__)
app.config ["DEBUG"] = True

#books catalog 

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)
@app.route ('/api/v1/resources/books/all', methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route ('/api/v1/resouces/books/byid', methods=['GET'])
def get_book_by_id():
    book_id = int (request.args.get ('id'))
    print (type (book_id))
    print (book_id)
    for book in books: 
        if book ['id']  == book_id:
            return jsonify (book)

app.run()