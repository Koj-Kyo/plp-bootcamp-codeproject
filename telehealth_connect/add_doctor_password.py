"""
Script pour ajouter la colonne password_hash à la table doctors
"""
from app import create_app
from extensions import db
from sqlalchemy import text

app = create_app()

with app.app_context():
    # Ajouter la colonne password_hash si elle n'existe pas
    try:
        with db.engine.connect() as connection:
            connection.execute(text("""
                ALTER TABLE doctors
                ADD COLUMN password_hash VARCHAR(255);
            """))
            connection.commit()
        print("✅ Colonne password_hash ajoutée avec succès à la table doctors!")
    except Exception as e:
        if "Duplicate column name" in str(e):
            print("ℹ️  La colonne password_hash existe déjà.")
        else:
            print(f"❌ Erreur: {e}")
