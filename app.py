from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_movie_details(query):
    api_key = 'ac9ed8e6a5f770b5645378b73a404a5b'
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}"
    response = requests.get(url)
    return response.json()['results']

def search_movies(query):
    query = query.lower()
    results = fetch_movie_details(query)
    return results

@app.route('/')
def index():
    return render_template('index.html', results=[])

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    if query:
        results = search_movies(query)
    else:
        results = []

    # Pass the enumerate function to the template context
    return render_template('index.html', results=results, enumerate=enumerate)


# ... rest of the code remains unchanged


@app.route('/movie_details', methods=['GET'])
def movie_details():
    num = int(request.args.get('num'))
    if 0 <= num < len(movie_details):
        movie = movie_details[num]
        title = movie['title']
        original_language = movie['original_language']
        release_date = movie['release_date']
        popularity = movie['popularity']
        overview = movie['overview']
    else:
        title, original_language, release_date, popularity, overview = "", "", "", "", ""

    return render_template('movie_details.html', title=title, original_language=original_language,
                           release_date=release_date, popularity=popularity, overview=overview)


if __name__ == '__main__':
    app.run(debug=True)
