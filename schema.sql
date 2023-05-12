CREATE TYPE post_category AS ENUM ('1212', '1213', '2214', '3155');

CREATE TABLE IF NOT EXISTS post (
    post_id SERIAL,
    title    VARCHAR(255) NOT NULL,
    author   VARCHAR(255) NOT NULL,
    content  TEXT NOT NULL,
    category post_category NOT NULL,
    PRIMARY KEY (post_id)
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "user" (
    user_id SERIAL,
    first_name  VARCHAR(255) NOT NULL,
    last_name   VARCHAR(255) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    date_added  DATE NOT NULL,
    username    VARCHAR(255) NOT NULL,
    password    VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

-- Create the comments table
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    post_id INTEGER NOT NULL,
    author VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);
