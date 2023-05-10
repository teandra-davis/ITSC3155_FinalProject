from src.models import HomeworkPost, HomeworkCategory, db


class PostRepository:

    def get_all_posts(self) -> list[HomeworkPost]:
        all_posts: list[HomeworkPost] = HomeworkPost.query.all()
        return all_posts

    def get_post_by_id(self, post_id: int) -> HomeworkPost:
        found_post: HomeworkPost = HomeworkPost.query.get_or_404(post_id)
        return found_post

    def create_post(self, author_name: str, title: str, details: str, category_id: int) -> HomeworkPost:
        new_post = HomeworkPost(author_name=author_name, title=title, details=details, category_id=category_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def search_posts(self, details: str) -> list[HomeworkPost]:
        found_posts: list[HomeworkPost] = HomeworkPost.query.filter(HomeworkPost.title.ilike(f'%{title}%')).all()
        return found_posts


# Singleton to be used in other modules
post_repository_singleton = PostRepository()
