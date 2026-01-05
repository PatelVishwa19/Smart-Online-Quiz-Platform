import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

# Create questions table
cursor.execute("""
INSERT INTO questions 
(question, option1, option2, option3, option4, correct_option, difficulty)
VALUES
('What does HTML stand for?', 'Hyper Text Markup Language', 'High Text Machine Language',
 'Hyperlinks and Text Markup Language', 'Home Tool Markup Language', 1, 'easy'),

('Which language is used for web apps?', 'Python', 'Java', 'JavaScript', 'All', 4, 'easy'),

('Which database is lightweight and file-based?', 'MySQL', 'PostgreSQL', 'SQLite', 'MongoDB', 3, 'easy'),

('What does CSS control?', 'Logic', 'Database', 'Styling', 'Server', 3, 'easy')
""")


# Create attempts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER,
    total INTEGER,
    timestamp TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")
