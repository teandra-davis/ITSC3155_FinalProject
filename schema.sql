CREATE TABLE IF NOT EXISTS user (
    user_id SERIAL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    date_added VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS post (
    book_id SERIAL,
    title   VARCHAR(255) NOT NULL,
    author  VARCHAR(255) NOT NULL,
    rating  INT          NOT NULL,
    PRIMARY KEY (book_id)
);

CREATE TABLE IF NOT EXISTS comment (
    book_id SERIAL,
    title   VARCHAR(255) NOT NULL,
    author  VARCHAR(255) NOT NULL,
    rating  INT          NOT NULL,
    PRIMARY KEY (book_id)
);

