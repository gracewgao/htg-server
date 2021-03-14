-- table for users
CREATE TABLE IF NOT EXISTS user (
    id SERIAL,
    username VARCHAR(100) NOT NULL UNIQUE,
    email_address VARCHAR(255) NOT NULL UNIQUE
);

-- images table
CREATE TABLE IF NOT EXISTS images ( 
    image_id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL UNIQUE,
    detail TEXT,
    created_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME'))
);

-- many-to-many associations for mojees and keywords
CREATE TABLE IF NOT EXISTS items (
    mojee_id INTEGER PRIMARY KEY,
    emoji VARCHAR(100) NOT NULL,
    keyword VARCHAR(100) NOT NULL
);
