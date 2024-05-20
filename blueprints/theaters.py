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
theaters_collection = db['theaters']

theaters_bp = Blueprint('theaters', __name__, template_folder='../templates')

@theaters_bp.route('/theaters')
@login_required
def theaters():
    page = int(request.args.get('page', 1))
    per_page = 100
    skip = (page - 1) * per_page
    theaters = theaters_collection.find({}).skip(skip).limit(per_page)
    total_theaters = theaters_collection.count_documents({})
    total_pages = (total_theaters // per_page) + (1 if total_theaters % per_page > 0 else 0)
    return render_template('theaters.html', theaters=theaters, page=page, total_pages=total_pages)

@theaters_bp.route('/theaters/theater/<theater_id>')
@login_required
def theater_details(theater_id):
    theater = theaters_collection.find_one({"_id": ObjectId(theater_id)})
    if theater:
        theater['_id'] = str(theater['_id'])  # ObjectIdを文字列に変換
        return jsonify(theater)
    else:
        return jsonify({"error": "Theater not found"}), 404
