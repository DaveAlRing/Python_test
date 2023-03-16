-- @block
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);

-- @block
INSERT INTO Users (email, bio, country)
VALUES (
    'hello@world.com',
    'i love strangers!',
    'US'
);

-- @block
INSERT INTO Users (email, bio, country)
VALUES 
    ('hello@worlds.com', 'foo', 'US'),
    ('hola@munda.com', 'bar', 'MX'),
    ('bonjour@monde.com', 'baz', 'FR');

-- @block
CREATE INDEX email_index ON Users(email);

-- @block
CREATE TABLE Rooms(
    id INT AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);

-- @block
INSERT INTO Rooms (owner_id, street)
VALUES
    (1, 'san diego sailbot'),
    (1, 'nantucket cottage'),
    (1, 'vail cabin'),
    (1, 'sf cardboard box');

-- @block
CREATE TABLE Bookings(
    id INT AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id),
    FOREIGN KEY (guest_id) REFERENCES Users(id)
);

-- @block
DROP TABLE Users;
DROP DATABASE airbnb;


