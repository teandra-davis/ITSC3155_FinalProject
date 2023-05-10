CREATE TABLE IF NOT EXISTS user (
    user_id SERIAL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    date_added DATETIME NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS post (
    post_author SERIAL,
    post_date   DATETIME NOT NULL,
    post_time  VARCHAR(255) NOT NULL,
    post_content  VARCHAR(255) NOT NULL,
    post_comments VARCHAR(255) NOT NULL,
    post_likes SERIAL,
    post_subject VARCHAR(255) NOT NULL,
    post_id SERIAL,
    PRIMARY KEY (post_id)
);

CREATE TABLE IF NOT EXISTS comment (
    comment_author VARCHAR(255) NOT NULL,,
    comment_date   DATETIME NOT NULL,
    comment_content  VARCHAR(255) NOT NULL,
    comment_likes  SERIAL,
    comment_postid SERIAL,
    PRIMARY KEY (comment_postid)
);


