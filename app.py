from flask import Flask, render_template, request

app = Flask(__name__)

# Simuler un ensemble de livres et de recommandations
recommendations = {
    1: [
        {"article_id": 101, "title": "The Great Gatsby", "category": "Fiction"},
        {"article_id": 102, "title": "1984", "category": "Dystopian"},
        {"article_id": 103, "title": "To Kill a Mockingbird", "category": "Classic"},
        {"article_id": 104, "title": "Moby Dick", "category": "Adventure"},
        {"article_id": 105, "title": "Pride and Prejudice", "category": "Romance"}
    ],
    2: [
        {"article_id": 106, "title": "The Catcher in the Rye", "category": "Fiction"},
        {"article_id": 107, "title": "The Lord of the Rings", "category": "Fantasy"},
        {"article_id": 108, "title": "Brave New World", "category": "Dystopian"},
        {"article_id": 109, "title": "Jane Eyre", "category": "Classic"},
        {"article_id": 110, "title": "War and Peace", "category": "Historical"}
    ],
    3: [
        {"article_id": 101, "title": "MAZA", "category": "Fiction"},
        {"article_id": 107, "title": "The Lord of the Rings", "category": "Fantasy"},
        {"article_id": 108, "title": "Brave New World", "category": "Dystopian"},
        {"article_id": 109, "title": "Jane Eyre", "category": "Classic"},
        {"article_id": 110, "title": "War and Peace", "category": "Historical"}
    ],
    4: [
        {"article_id": 106, "title": "IYAD RAYAN", "category": "Fiction"},
        {"article_id": 107, "title": "The Lord of the Rings", "category": "Fantasy"},
        {"article_id": 108, "title": "Brave New World", "category": "Dystopian"},
        {"article_id": 109, "title": "Jane Eyre", "category": "Classic"},
        {"article_id": 110, "title": "War and Peace", "category": "Historical"}
    ]    
}

# Page principale avec le formulaire d'entrée pour saisir l'ID utilisateur
@app.route('/', methods=['GET', 'POST'])  # Accepter les méthodes GET et POST
def home():
    user_id = None
    user_recommendations = []
    
    if request.method == 'POST':  # Vérifier si la requête est un POST
        user_id = int(request.form['userid'])  # Récupère l'ID utilisateur depuis le formulaire
        user_recommendations = recommendations.get(user_id, [])  # Récupère les recommandations
        
    return render_template('index.html', user_id=user_id, recommendations=user_recommendations)

if __name__ == "__main__":
    app.run(debug=True)

