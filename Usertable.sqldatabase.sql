DROP TABLE IF EXISTS users;

CREATE TABLE users(
    username VARCHAR(30) PRIMARY KEY,
    hashed_password TEXT NOT NULL,
    roles VARCHAR(20) NOT NULL
);

INSERT INTO users (username, hashed_password, roles) VALUES
('Pavithra', 'pavii123', 'client'),
('Kandha', 'kandha123', 'client'),
('Kamal', 'kamal123', 'client'),
('Suresh', 'suresh123', 'client'),
('Priya', 'priya123', 'client'),
('Anu', 'anu123', 'support'),
('Elayappan', 'elayappan123', 'support'),
('Vijay', 'vijay123', 'support'),
('Meena', 'meena123', 'support'),
('Rohit', 'rohit123', 'support');

-- Update hashed passwords
UPDATE users
SET hashed_password ='2a88d9fb634610b00a96ada1feb80dd2a35453d8a6e84f63eb1d5810f2ed866d'
WHERE username = 'Pavithra';

UPDATE users
SET hashed_password ='cbeaae6fed8e46837bb0b803510b2dc6182591c65ca299255403b73d01203310'
WHERE username = 'Kandha';

UPDATE users
SET hashed_password ='46ee02533775fbeff2e9f3cdc437fa8ff426d8f2d0cc9b0f96c70ddcfc317047'
WHERE username = 'Kamal';

UPDATE users
SET hashed_password ='5ce986381bec29b9b8233906a722ff943b3b6caa24d00d207a15ab1205831ff2'
WHERE username = 'Suresh';

UPDATE users
SET hashed_password ='0a8b8dfad3f637d7d30fed7b108c5c5986c4775d14cab26ec9279866eba99116'
WHERE username = 'Priya';

UPDATE users
SET hashed_password ='686f2160bc1b0928c46ec5f9b87d65490306e018bdfafbae4fbc03e1e0aa70b5'
WHERE username = 'Anu';

UPDATE users
SET hashed_password ='30520fbbdc44b6cbff88b22d63751cfe1b0451c817ce6834a02901a332905530'
WHERE username = 'Elayappan';

UPDATE users
SET hashed_password ='0dfee0daca587e1826e80dbd56e0c0215be463504cbe8ca9a9dd41adc2ed2df4'
WHERE username = 'Vijay';

UPDATE users
SET hashed_password ='e341ae002fdfadb5389e4188800e5bb9a5d137d977fffd3b37be412501e70260'
WHERE username = 'Meena';

UPDATE users
SET hashed_password ='6ac79a6bd1f24a4ef77226c20d2c4ce395ce3ded1ce9b24dbf3e17b877af50e1'
WHERE username = 'Rohit';

SELECT * FROM users;