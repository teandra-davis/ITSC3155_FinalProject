from src.models import User, db

class UserRepository:
    
    def get_user_by_id(self, user_id: int) -> User:
        found_user: User = User.query.get_or_404(user_id)
        return found_user

    def create_user(self, first_name: str, last_name: str, email: str, date_added: str, username: str, password: str, user_id: int) -> User:
        new_user = User(first_name=first_name, last_name=last_name, email=email, date_added=date_added)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def search_posts(self, content: str) -> list[Post]:
        found_posts: list[Post] = Post.query.filter(Post.details.ilike(f'%{content}%')).all()
        return found_posts