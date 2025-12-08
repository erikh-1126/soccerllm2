from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["soccerdb"]
players = db.players

player_docs = [
    {"name": "Lionel Messi", "position": "Forward", "clubs": ["Barcelona", "PSG", "Inter Miami"], "appearances": 1000, "goals": 800},
    {"name": "Cristiano Ronaldo", "position": "Forward", "clubs": ["Sporting CP", "Manchester United", "Real Madrid", "Juventus", "Al-Nassr"], "appearances": 1300, "goals": 950},
    {"name": "Neymar Jr", "position": "Forward", "clubs": ["Santos", "Barcelona", "PSG", "Al-Hilal"], "appearances": 650, "goals": 400},
    {"name": "Kylian Mbappé", "position": "Forward", "clubs": ["Monaco", "PSG", "Real Madrid"], "appearances": 350, "goals": 250},
    {"name": "Robert Lewandowski", "position": "Forward", "clubs": ["Lech Poznań", "Dortmund", "Bayern", "Barcelona"], "appearances": 700, "goals": 540},
    {"name": "Luis Suárez", "position": "Forward", "clubs": ["Ajax", "Liverpool", "Barcelona", "Atlético"], "appearances": 700, "goals": 450},
    {"name": "Karim Benzema", "position": "Forward", "clubs": ["Lyon", "Real Madrid", "Al-Ittihad"], "appearances": 750, "goals": 430},
    {"name": "Mohamed Salah", "position": "Forward", "clubs": ["Basel", "Chelsea", "Roma", "Liverpool"], "appearances": 550, "goals": 300},
    {"name": "Kevin De Bruyne", "position": "Midfielder", "clubs": ["Genk", "Chelsea", "Wolfsburg", "Man City"], "appearances": 550, "goals": 110},
    {"name": "Luka Modrić", "position": "Midfielder", "clubs": ["Dinamo Zagreb", "Tottenham", "Real Madrid"], "appearances": 700, "goals": 80},
    {"name": "Toni Kroos", "position": "Midfielder", "clubs": ["Bayern Munich", "Real Madrid"], "appearances": 650, "goals": 70},
    {"name": "Sergio Ramos", "position": "Defender", "clubs": ["Sevilla", "Real Madrid", "PSG"], "appearances": 750, "goals": 110},
    {"name": "Virgil van Dijk", "position": "Defender", "clubs": ["Groningen", "Celtic", "Southampton", "Liverpool"], "appearances": 450, "goals": 45},
    {"name": "Giorgio Chiellini", "position": "Defender", "clubs": ["Juventus", "LAFC"], "appearances": 700, "goals": 40},
    {"name": "Marc-André ter Stegen", "position": "Goalkeeper", "clubs": ["Gladbach", "Barcelona"], "appearances": 500, "goals": 0},
    {"name": "Manuel Neuer", "position": "Goalkeeper", "clubs": ["Schalke", "Bayern Munich"], "appearances": 700, "goals": 0},
    {"name": "Thibaut Courtois", "position": "Goalkeeper", "clubs": ["Genk", "Chelsea", "Real Madrid"], "appearances": 550, "goals": 0},
    {"name": "Harry Kane", "position": "Forward", "clubs": ["Tottenham", "Bayern Munich"], "appearances": 550, "goals": 350},
    {"name": "Erling Haaland", "position": "Forward", "clubs": ["Molde", "Salzburg", "Dortmund", "Man City"], "appearances": 250, "goals": 200},
    {"name": "Antoine Griezmann", "position": "Forward", "clubs": ["Real Sociedad", "Atlético", "Barcelona"], "appearances": 650, "goals": 300},
    {"name": "Vinícius Júnior", "position": "Forward", "clubs": ["Flamengo", "Real Madrid"], "appearances": 250, "goals": 70},
    {"name": "Pedri", "position": "Midfielder", "clubs": ["Las Palmas", "Barcelona"], "appearances": 150, "goals": 20},
    {"name": "Rodri", "position": "Midfielder", "clubs": ["Villarreal", "Atlético", "Man City"], "appearances": 300, "goals": 25},
    {"name": "Son Heung-min", "position": "Forward", "clubs": ["Hamburg", "Leverkusen", "Tottenham"], "appearances": 500, "goals": 200},
    {"name": "Jude Bellingham", "position": "Midfielder", "clubs": ["Birmingham", "Dortmund", "Real Madrid"], "appearances": 200, "goals": 50}
]

result = players.insert_many(player_docs)

print(f"Inserted {len(result.inserted_ids)} player records into soccerdb.players")
