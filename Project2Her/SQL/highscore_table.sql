CREATE TABLE highscores (
    player_id INT PRIMARY KEY,
    player_name VARCHAR(255),
    player_score INT);

INSERT INTO highscores (player_id, player_name, player_score)
VALUES (1, 'test1', 999);
INSERT INTO highscores (player_id, player_name, player_score)
VALUES (2, 'test2', 998);
INSERT INTO highscores (player_id, player_name, player_score)
VALUES (3, 'test3', 997);