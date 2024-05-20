from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB接続設定
uri = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.7wocgja.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['sample_mflix']
movies_collection = db['movies']

movies_bp = Blueprint('movies', __name__, template_folder='../templates')

@movies_bp.route('/movies')
@login_required
def movies():
    page = int(request.args.get('page', 1))
    per_page = 100
    skip = (page - 1) * per_page
    movies = movies_collection.find({}, {"title": 1}).skip(skip).limit(per_page)
    total_movies = movies_collection.count_documents({})
    total_pages = (total_movies // per_page) + (1 if total_movies % per_page > 0 else 0)
    return render_template('movies.html', movies=movies, page=page, total_pages=total_pages)

@movies_bp.route('/movies/movie/<movie_id>')
@login_required
def movie_details(movie_id):
    movie = movies_collection.find_one({"_id": ObjectId(movie_id)})
    if movie:
        movie['_id'] = str(movie['_id'])  # ObjectIdを文字列に変換
        return jsonify(movie)
    else:
        return jsonify({"error": "Movie not found"}), 404
