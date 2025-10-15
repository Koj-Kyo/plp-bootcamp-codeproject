"""
Script pour peupler la base de données avec des données togolaises
TeleHealth Connect - Données du Togo
"""
from app import create_app, db
from models.health_center import HealthCenter
from models.doctor import Doctor
from datetime import datetime

# Créer l'application
app = create_app()

# Données des centres de santé au Togo
health_centers_data = [
    {
        'name': 'CHU Campus de Lomé',
        'address': 'Boulevard du 13 Janvier',
        'city': 'Lomé',
        'state': 'Maritime',
        'postal_code': 'BP 57',
        'phone': '+228 22 25 00 01',
        'latitude': 6.1725,
        'longitude': 1.2314
    },
    {
        'name': 'CHU Sylvanus Olympio',
        'address': 'Rue du Marché',
        'city': 'Lomé',
        'state': 'Maritime',
        'postal_code': 'BP 2000',
        'phone': '+228 22 21 25 01',
        'latitude': 6.1256,
        'longitude': 1.2116
    },
    {
        'name': 'Clinique Biasa',
        'address': 'Quartier Tokoin',
        'city': 'Lomé',
        'state': 'Maritime',
        'postal_code': 'BP 12345',
        'phone': '+228 22 21 84 00',
        'latitude': 6.1628,
        'longitude': 1.2255
    },
    {
        'name': 'Hôpital de Bè',
        'address': 'Quartier Bè-Kpota',
        'city': 'Lomé',
        'state': 'Maritime',
        'postal_code': 'BP 3003',
        'phone': '+228 22 21 28 30',
        'latitude': 6.1461,
        'longitude': 1.2058
    },
    {
        'name': 'CHR de Sokodé',
        'address': 'Avenue de la Paix',
        'city': 'Sokodé',
        'state': 'Centrale',
        'postal_code': 'BP 88',
        'phone': '+228 25 50 00 24',
        'latitude': 8.9833,
        'longitude': 1.1333
    },
    {
        'name': 'CHR de Kara',
        'address': 'Route Nationale N°1',
        'city': 'Kara',
        'state': 'Kara',
        'postal_code': 'BP 18',
        'phone': '+228 26 60 00 34',
        'latitude': 9.5511,
        'longitude': 1.1864
    },
    {
        'name': 'Hôpital de Tsévié',
        'address': 'Centre-ville',
        'city': 'Tsévié',
        'state': 'Maritime',
        'postal_code': 'BP 33',
        'phone': '+228 23 31 00 15',
        'latitude': 6.4262,
        'longitude': 1.2136
    },
    {
        'name': 'CHR d\'Atakpamé',
        'address': 'Quartier Administratif',
        'city': 'Atakpamé',
        'state': 'Plateaux',
        'postal_code': 'BP 14',
        'phone': '+228 24 40 00 22',
        'latitude': 7.5333,
        'longitude': 1.1167
    },
    {
        'name': 'Hôpital de Dapaong',
        'address': 'Centre-ville',
        'city': 'Dapaong',
        'state': 'Savanes',
        'postal_code': 'BP 10',
        'phone': '+228 27 70 00 18',
        'latitude': 10.8631,
        'longitude': 0.2072
    },
    {
        'name': 'Clinique Internationale du Golfe',
        'address': 'Boulevard du Mono',
        'city': 'Lomé',
        'state': 'Maritime',
        'postal_code': 'BP 8394',
        'phone': '+228 22 27 13 13',
        'latitude': 6.1319,
        'longitude': 1.2223
    }
]

# Données des médecins togolais
doctors_data = [
    {
        'first_name': 'Kofi',
        'last_name': 'Agbéko',
        'specialization': 'Médecine Générale',
        'email': 'k.agbeko@chu-lome.tg',
        'phone': '+228 90 12 34 56',
        'qualification': 'Docteur en Médecine',
        'experience_years': 12,
        'consultation_fee': 15000,  # En FCFA
        'health_center_name': 'CHU Campus de Lomé'
    },
    {
        'first_name': 'Ama',
        'last_name': 'Koffi',
        'specialization': 'Pédiatrie',
        'email': 'a.koffi@chu-lome.tg',
        'phone': '+228 90 23 45 67',
        'qualification': 'Pédiatre, Diplômée de Dakar',
        'experience_years': 8,
        'consultation_fee': 18000,
        'health_center_name': 'CHU Campus de Lomé'
    },
    {
        'first_name': 'Edem',
        'last_name': 'Attiogbé',
        'specialization': 'Cardiologie',
        'email': 'e.attiogbe@sylvanus.tg',
        'phone': '+228 90 34 56 78',
        'qualification': 'Cardiologue, Spécialiste',
        'experience_years': 15,
        'consultation_fee': 25000,
        'health_center_name': 'CHU Sylvanus Olympio'
    },
    {
        'first_name': 'Dzifa',
        'last_name': 'Amegavi',
        'specialization': 'Gynécologie-Obstétrique',
        'email': 'd.amegavi@sylvanus.tg',
        'phone': '+228 90 45 67 89',
        'qualification': 'Gynécologue-Obstétricienne',
        'experience_years': 10,
        'consultation_fee': 20000,
        'health_center_name': 'CHU Sylvanus Olympio'
    },
    {
        'first_name': 'Komi',
        'last_name': 'Gbadamassi',
        'specialization': 'Chirurgie Générale',
        'email': 'k.gbadamassi@biasa.tg',
        'phone': '+228 90 56 78 90',
        'qualification': 'Chirurgien, Spécialiste',
        'experience_years': 18,
        'consultation_fee': 30000,
        'health_center_name': 'Clinique Biasa'
    },
    {
        'first_name': 'Akossiwa',
        'last_name': 'Dogbey',
        'specialization': 'Dermatologie',
        'email': 'a.dogbey@biasa.tg',
        'phone': '+228 90 67 89 01',
        'qualification': 'Dermatologue',
        'experience_years': 7,
        'consultation_fee': 17000,
        'health_center_name': 'Clinique Biasa'
    },
    {
        'first_name': 'Yao',
        'last_name': 'Kouassi',
        'specialization': 'Médecine Générale',
        'email': 'y.kouassi@be.tg',
        'phone': '+228 90 78 90 12',
        'qualification': 'Médecin Généraliste',
        'experience_years': 9,
        'consultation_fee': 12000,
        'health_center_name': 'Hôpital de Bè'
    },
    {
        'first_name': 'Afi',
        'last_name': 'Tete',
        'specialization': 'Ophtalmologie',
        'email': 'a.tete@be.tg',
        'phone': '+228 90 89 01 23',
        'qualification': 'Ophtalmologue',
        'experience_years': 11,
        'consultation_fee': 22000,
        'health_center_name': 'Hôpital de Bè'
    },
    {
        'first_name': 'Kossi',
        'last_name': 'Atcholi',
        'specialization': 'Médecine Interne',
        'email': 'k.atcholi@sokode.tg',
        'phone': '+228 91 12 34 56',
        'qualification': 'Interniste',
        'experience_years': 13,
        'consultation_fee': 16000,
        'health_center_name': 'CHR de Sokodé'
    },
    {
        'first_name': 'Efua',
        'last_name': 'Lamisi',
        'specialization': 'Pédiatrie',
        'email': 'e.lamisi@sokode.tg',
        'phone': '+228 91 23 45 67',
        'qualification': 'Pédiatre',
        'experience_years': 6,
        'consultation_fee': 14000,
        'health_center_name': 'CHR de Sokodé'
    },
    {
        'first_name': 'Yaovi',
        'last_name': 'Komlan',
        'specialization': 'Traumatologie',
        'email': 'y.komlan@kara.tg',
        'phone': '+228 92 34 56 78',
        'qualification': 'Traumatologue',
        'experience_years': 14,
        'consultation_fee': 19000,
        'health_center_name': 'CHR de Kara'
    },
    {
        'first_name': 'Abla',
        'last_name': 'Akakpo',
        'specialization': 'Médecine Générale',
        'email': 'a.akakpo@tsevie.tg',
        'phone': '+228 93 45 67 89',
        'qualification': 'Médecin Généraliste',
        'experience_years': 5,
        'consultation_fee': 10000,
        'health_center_name': 'Hôpital de Tsévié'
    },
    {
        'first_name': 'Kwame',
        'last_name': 'Adjoyi',
        'specialization': 'Neurologie',
        'email': 'k.adjoyi@atakpame.tg',
        'phone': '+228 94 56 78 90',
        'qualification': 'Neurologue',
        'experience_years': 10,
        'consultation_fee': 23000,
        'health_center_name': 'CHR d\'Atakpamé'
    },
    {
        'first_name': 'Sena',
        'last_name': 'Aziagbe',
        'specialization': 'Médecine Générale',
        'email': 's.aziagbe@dapaong.tg',
        'phone': '+228 95 67 89 01',
        'qualification': 'Médecin Généraliste',
        'experience_years': 8,
        'consultation_fee': 11000,
        'health_center_name': 'Hôpital de Dapaong'
    },
    {
        'first_name': 'Ekoué',
        'last_name': 'Mensah',
        'specialization': 'Gastro-entérologie',
        'email': 'e.mensah@golfe.tg',
        'phone': '+228 96 78 90 12',
        'qualification': 'Gastro-entérologue',
        'experience_years': 16,
        'consultation_fee': 27000,
        'health_center_name': 'Clinique Internationale du Golfe'
    },
    {
        'first_name': 'Ayélé',
        'last_name': 'Kpelafia',
        'specialization': 'Radiologie',
        'email': 'a.kpelafia@golfe.tg',
        'phone': '+228 97 89 01 23',
        'qualification': 'Radiologue',
        'experience_years': 9,
        'consultation_fee': 20000,
        'health_center_name': 'Clinique Internationale du Golfe'
    }
]


def populate_database():
    """Peupler la base de données avec des données togolaises"""
    with app.app_context():
        print("🇹🇬 Démarrage du peuplement de la base de données...")
        print("=" * 60)

        # Vider les tables existantes
        print("\n🗑️  Suppression des données existantes...")
        Doctor.query.delete()
        HealthCenter.query.delete()
        db.session.commit()
        print("✓ Données existantes supprimées")

        # Ajouter les centres de santé
        print("\n🏥 Ajout des centres de santé du Togo...")
        health_centers = {}
        for hc_data in health_centers_data:
            health_center = HealthCenter(**hc_data)
            db.session.add(health_center)
            db.session.flush()  # Pour obtenir l'ID
            health_centers[hc_data['name']] = health_center
            print(f"  ✓ {hc_data['name']} - {hc_data['city']}")

        db.session.commit()
        print(f"\n✓ {len(health_centers)} centres de santé ajoutés avec succès!")

        # Ajouter les médecins avec mot de passe par défaut
        print("\n👨‍⚕️ Ajout des médecins togolais...")
        doctors_count = 0
        default_password = 'doctor123'

        for doc_data in doctors_data:
            health_center_name = doc_data.pop('health_center_name')
            health_center = health_centers.get(health_center_name)

            if health_center:
                doctor = Doctor(
                    health_center_id=health_center.id,
                    **doc_data
                )
                # Définir le mot de passe par défaut
                doctor.set_password(default_password)
                db.session.add(doctor)
                doctors_count += 1
                print(f"  ✓ Dr. {doc_data['first_name']} {doc_data['last_name']} - {doc_data['specialization']}")

        db.session.commit()
        print(f"\n✓ {doctors_count} médecins ajoutés avec succès!")
        print(f"🔑 Mot de passe par défaut pour tous les médecins : {default_password}")

        # Afficher le résumé
        print("\n" + "=" * 60)
        print("📊 RÉSUMÉ DU PEUPLEMENT")
        print("=" * 60)
        print(f"🏥 Centres de santé : {len(health_centers)}")
        print(f"👨‍⚕️ Médecins : {doctors_count}")
        print("\n🎯 Villes couvertes :")
        cities = set([hc['city'] for hc in health_centers_data])
        for city in sorted(cities):
            city_centers = [hc['name'] for hc in health_centers_data if hc['city'] == city]
            print(f"  • {city} : {len(city_centers)} centre(s)")

        print("\n🏥 Spécialités disponibles :")
        specializations = set([doc['specialization'] for doc in doctors_data])
        for spec in sorted(specializations):
            spec_count = len([d for d in doctors_data if d['specialization'] == spec])
            print(f"  • {spec} : {spec_count} médecin(s)")

        print("\n" + "=" * 60)
        print("✅ Base de données peuplée avec succès!")
        print("🇹🇬 Données togolaises prêtes pour TeleHealth Connect!")
        print("=" * 60)


if __name__ == '__main__':
    try:
        populate_database()
    except Exception as e:
        print(f"\n❌ Erreur lors du peuplement: {e}")
        import traceback
        traceback.print_exc()
