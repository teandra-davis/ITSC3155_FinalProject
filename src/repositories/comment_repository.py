from src.models import Comment, db

class CommentRepository:
    def create_comment(self, post_id, author, content):
        comment = Comment(post_id=post_id, author=author, content=content)
        db.session.add(comment)
        db.session.commit()
        return comment

    def get_comments_for_post(self, post_id):
        return Comment.query.filter_by(post_id=post_id).order_by(Comment.timestamp.desc()).all()

    def delete_comment(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()