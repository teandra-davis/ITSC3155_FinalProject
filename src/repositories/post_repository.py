from src.models import HomeworkPost, HomeworkCategory, db


class PostRepository:

    def get_all_posts(self) -> list[HomeworkPost]:
        all_posts: list[HomeworkPost] = HomeworkPost.query.all()
        return all_posts

    def get_post_by_id(self, post_id: int) -> HomeworkPost:
        found_post: HomeworkPost = HomeworkPost.query.get_or_404(post_id)
        return found_post

    def create_post(self, author_name: str, title: str, content: str, subject: int) -> HomeworkPost:
        new_post = HomeworkPost(author_name=author_name, title=title, content=content, subject=subject)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def search_posts(self, details: str) -> list[HomeworkPost]:
        found_posts: list[HomeworkPost] = HomeworkPost.query.filter(HomeworkPost.details.ilike(f'%{details}%')).all()
        return found_posts


# Singleton to be used in other modules
post_repository_singleton = PostRepository()
