import psycopg2

class Database:
    def interact_with_database(command):
        connection = psycopg2.connect(host = "localhost", dbname = "Jaar 1 Project 2 Her", user = "postgres", password = "password")
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        results = None
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:
            pass
        cursor.close()
        connection.close()
        return results
    def get_top_5():
        return Database.interact_with_database("SELECT player_name, player_score FROM highscores ORDER BY player_score ASC LIMIT 5;")
    def get_newest_id():
        return Database.interact_with_database("SELECT player_id FROM highscores ORDER BY player_id DESC LIMIT 1;")[0][0]
    def get_player(player_id):
        return Database.interact_with_database("SELECT player_name, player_score FROM highscores WHERE player_id = " + str(player_id) + ";")
    def upload_score(name, score):
        player_id = Database.get_newest_id()
        Database.interact_with_database("INSERT INTO highscores (player_id, player_name, player_score) VALUES (" + str(player_id + 1) + ", '" + str(name) + "', " + str(score) + ");")
