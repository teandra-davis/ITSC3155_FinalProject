from src.models import User, db

class UserRepository:
    
    def get_user_by_id(self, user_id: int) -> User:
        found_user: User = User.query.get_or_404(user_id)
        return found_user
    
    def get_user_by_username(self, username: str) -> User:
        found_user: User = User.query.get_or_404(username)
        return found_user


    def create_user(self, first_name: str, last_name: str, email: str, date_added: str, username: str, password: str) -> User:
        new_user = User(first_name=first_name, last_name=last_name, email=email, date_added=date_added, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def search_users(self, content: str) -> list[User]:
        found_users: list[User] = User.query.filter(User.details.ilike(f'%{content}%')).all()
        return found_users
    
    def update_user(self, user_id: int, email: str) -> User:
        user_to_update: User = User.query.get_or_404(user_id)

        user_to_update.email = email
        db.session.commit()
        return user_to_update
    
    def delete_user(self, user_id: int) -> None:
        user_to_delete: User = User.query.get_or_404(user_id)
        db.session.delete(user_to_delete)
        db.session.commit()
    
# Singleton to be used in other modules
user_repository_singleton = UserRepository()