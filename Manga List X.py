import os

# Configuration du projet
PROJECT_NAME = "Manga List X"
OUTPUT_DIR = "dist" # Dossier pour Netlify

# Liste factice pour l'exemple (tu pourras la remplir avec tes données)
manga_catalog = [
    {"id": 1, "title": "Maîtresse & Élève", "subtitle": "Une leçon particulière", "image": "https://via.placeholder.com/300x450"},
    {"id": 2, "title": "Secret de Bureau", "subtitle": "Travail de nuit", "image": "https://via.placeholder.com/300x450"},
    {"id": 3, "title": "Vacances d'Été", "subtitle": "Souvenirs de plage", "image": "https://via.placeholder.com/300x450"},
    {"id": 4, "title": "La Voisine", "subtitle": "Rencontre inattendue", "image": "https://via.placeholder.com/300x450"},
]

def generate_index_html():
    # Création du design CSS (Dark & Pro)
    css = """
    body {
        background-color: #0f0f0f;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
    }
    header {
        height: 40vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://via.placeholder.com/1200x400');
        background-size: cover;
        border-bottom: 2px solid #e74c3c;
    }
    h1 {
        font-size: 4rem;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: #e74c3c;
        text-shadow: 2px 2px 10px rgba(231, 76, 60, 0.5);
    }
    .catalog-container {
        padding: 50px 10%;
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 30px;
    }
    .manga-card {
        background: #1a1a1a;
        border-radius: 10px;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        text-decoration: none;
        color: white;
        border: 1px solid #333;
    }
    .manga-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(231, 76, 60, 0.3);
        border-color: #e74c3c;
    }
    .manga-card img {
        width: 100%;
        height: 350px;
        object-fit: cover;
    }
    .manga-info {
        padding: 15px;
    }
    .manga-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin: 0;
    }
    .manga-subtitle {
        font-size: 0.9rem;
        color: #aaaaaa;
        margin-top: 5px;
    }
    footer {
        text-align: center;
        padding: 40px;
        color: #555;
        font-size: 0.8rem;
    }
    """

    # Construction du catalogue en HTML
    cards_html = ""
    for manga in manga_catalog:
        cards_html += f"""
        <a href="manga_{manga['id']}.html" class="manga-card">
            <img src="{manga['image']}" alt="{manga['title']}">
            <div class="manga-info">
                <div class="manga-title">{manga['title']}</div>
                <div class="manga-subtitle">{manga['subtitle']}</div>
            </div>
        </a>
        """

    # Structure complète de la page
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{PROJECT_NAME}</title>
        <style>{css}</style>
    </head>
    <body>
        <header>
            <h1>{PROJECT_NAME}</h1>
            <p>Le catalogue ultime des mangas X</p>
        </header>

        <main class="catalog-container">
            {cards_html}
        </main>

        <footer>
            &copy; 2026 {PROJECT_NAME} - Contenu pour adultes
        </footer>
    </body>
    </html>
    """

    # Créer le dossier et sauvegarder le fichier
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    with open(f"{OUTPUT_DIR}/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Site généré avec succès dans le dossier '{OUTPUT_DIR}'")

if __name__ == "__main__":
    generate_index_html()
