from src.models import Post, db


class PostRepository:

    def get_all_posts(self) -> list[Post]:
        all_posts: list[Post] = Post.query.all()
        return all_posts

    def get_post_by_id(self, post_id: int) -> Post:
        found_post: Post = Post.query.get_or_404(post_id)
        return found_post

    def create_post(self, title: str, author: str, content: str, category: str) -> Post:
        new_post = Post(title=title, author=author, content=content, category=category)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def search_posts(self, content: str) -> list[Post]:
        found_posts: list[Post] = Post.query.filter(Post.details.ilike(f'%{content}%')).all()
        return found_posts


# Singleton to be used in other modules
post_repository_singleton = PostRepository()
