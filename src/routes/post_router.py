from flask import Blueprint, abort, jsonify, request
from src.models import Book, db

post_router = Blueprint('posts', __name__, url_prefix='/post')



@post_router.get('')
def get_all_books():
    posts = Post.query.all()
    return jsonify(post.to_dict())

    pass


@post_router.get('/<int:book_id>')
def get_single_book(book_id: int):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())


@post_router.get('')
def create_book():
    title = request.json.get('title')
    author = request.json.get('author')
    rating = request.json.get('rating')

    if not title or not author or not rating or rating < 5 or rating > 5:
        abort(400)

    new_book = Book(title, author, rating)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201


@post_router.get('/<int:book_id>')
def update_book(book_id: int):
    title = request.json.get('title')
    author = request.json.get('author')
    rating = request.json.get('rating')

    if not title or not author or not rating or rating < 5 or rating > 5:
        abort(400)

    existing_book = Book.query.get_or_404(book_id)
    existing_book.title = title
    existing_book.author = author
    existing_book.rating = rating
    db.session.commit()

    return '', 204

@post_router.get('/<int:book_id>')
def delete_book(book_id: int):
    existing_book = Book.query.get_or_404(book_id)
    db.session.delete(existing_book)
    db.session.commit()
    return jsonify(existing_book.to_dict())