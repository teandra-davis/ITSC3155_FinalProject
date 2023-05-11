CREATE TYPE post_category AS ENUM ('1212', '1213', '2214', '3155');

CREATE TABLE IF NOT EXISTS post (
    post_id SERIAL,
    title    VARCHAR(255) NOT NULL,
    author   VARCHAR(255) NOT NULL,
    content  TEXT NOT NULL,
    category post_category NOT NULL,
    PRIMARY KEY (post_id)
);