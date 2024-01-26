import sqlite3

#функция сохранения очков
def save_record(score):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    # Получаем текущий лучший рекорд
    cursor.execute('SELECT MAX(score) FROM records')
    current_best_score = cursor.fetchone()[0]

    if current_best_score is None or score > current_best_score:
        # Добавление нового рекорда, если он лучше текущего
        cursor.execute('INSERT INTO records (score) VALUES (?)', (score,))

    conn.commit()
    conn.close()


