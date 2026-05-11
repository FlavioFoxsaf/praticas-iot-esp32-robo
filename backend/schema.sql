CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    temperatura_c REAL,
    luminosidade REAL,
    presenca INTEGER,
    probabilidade_vida REAL
);
