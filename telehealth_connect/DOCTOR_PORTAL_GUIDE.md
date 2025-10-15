# 👨‍⚕️ Guide du Portail Médecin - TeleHealth Connect

## 🆕 Nouveau : Espace Médecin Ajouté !

Le système TeleHealth Connect dispose maintenant d'un **portail complet pour les médecins** pour gérer leurs rendez-vous et patients.

---

## 🚀 Mise en Place

### Étape 1 : Ajouter la colonne password_hash

```bash
cd d:\PLP\bootcampProject\telehealth_connect
venv\Scripts\activate
python add_doctor_password.py
```

### Étape 2 : Peupler avec les données togolaises

```bash
python populate_togo_data.py
```

Cela va :
- ✅ Ajouter 10 centres de santé togolais
- ✅ Ajouter 16 médecins togolais
- ✅ **Créer un mot de passe par défaut : `doctor123`** pour tous les médecins

---

## 🔑 Connexion Médecin

### URL d'accès
```
http://localhost:5000/doctor/login
```

### Identifiants par défaut
- **Email** : Utilisez l'email du médecin (ex: `k.agbeko@chucampus.tg`)
- **Mot de passe** : `doctor123` (pour tous les médecins)

### Exemples d'identifiants

| Médecin | Email | Spécialité | Mot de passe |
|---------|-------|------------|--------------|
| Dr. Kofi Agbéko | k.agbeko@chucampus.tg | Médecine Générale | doctor123 |
| Dr. Ama Koffi | a.koffi@chucampus.tg | Pédiatrie | doctor123 |
| Dr. Edem Attiogbé | e.attiogbe@sylvanus.tg | Cardiologie | doctor123 |
| Dr. Dzifa Amegavi | d.amegavi@sylvanus.tg | Gynécologie | doctor123 |

---

## 📋 Fonctionnalités du Portail Médecin

### 1️⃣ **Tableau de Bord**
- 📊 **Statistiques** : Total rendez-vous, en attente, complétés, annulés
- 📅 **Rendez-vous du jour** : Liste complète avec détails patients
- 📆 **Rendez-vous à venir** : Prochains rendez-vous programmés

### 2️⃣ **Gestion des Rendez-vous**
- 📋 **Liste complète** : Tous les rendez-vous avec filtres
- 🔍 **Filtres disponibles** :
  - Par statut (Tous, Programmés, Complétés, Annulés, Non présentés)
  - Par période (Toutes dates, Aujourd'hui, À venir, Passés)
- 📝 **Actions disponibles** :
  - Voir détails complets
  - Changer le statut
  - Ajouter des notes médicales

### 3️⃣ **Détails du Rendez-vous**
- 👤 **Informations patient** : Nom, âge, contact, historique
- 📅 **Informations rendez-vous** : Date, heure, raison, statut
- 📝 **Gestion** :
  - Marquer comme complété
  - Annuler le rendez-vous
  - Marquer comme non présenté
  - Ajouter notes de consultation

### 4️⃣ **Dossier Patient**
- 📁 **Informations complètes** : Données personnelles, contact
- 📅 **Historique complet** : Tous les rendez-vous avec ce médecin
- 📝 **Notes médicales** : Consultation précédente visible

---

## 🎯 Statuts des Rendez-vous

| Statut | Description | Action |
|--------|-------------|--------|
| **scheduled** | Rendez-vous programmé | En attente de consultation |
| **completed** | Consultation terminée | Patient vu et traité |
| **cancelled** | Rendez-vous annulé | Par médecin ou patient |
| **no-show** | Patient absent | Patient non présenté |

---

## 🔄 Workflow Typique

1. **Connexion médecin** → `/doctor/login`
2. **Voir tableau de bord** → Statistiques + Rendez-vous du jour
3. **Consulter patient** → Cliquer sur "Voir détails"
4. **Voir dossier patient** → Historique complet
5. **Ajouter notes** → Diagnostic, traitement, recommandations
6. **Changer statut** → Marquer comme "Complété"

---

## 🛠️ Structure Technique

### Routes créées
```python
/doctor/login                    # Connexion médecin
/doctor/logout                   # Déconnexion
/doctor/dashboard                # Tableau de bord
/doctor/appointments             # Liste rendez-vous
/doctor/appointment/<id>         # Détails rendez-vous
/doctor/appointment/<id>/update-status  # Mise à jour statut
/doctor/patient/<id>             # Dossier patient
```

### Templates créés
```
templates/doctor_login.html              # Page connexion
templates/doctor_dashboard.html          # Tableau de bord
templates/doctor_appointments.html       # Liste rendez-vous
templates/doctor_appointment_detail.html # Détails rendez-vous
templates/doctor_patient_detail.html     # Dossier patient
```

### Modèle Doctor mis à jour
```python
# Nouvelles méthodes ajoutées
doctor.set_password(password)     # Définir mot de passe
doctor.check_password(password)   # Vérifier mot de passe
```

---

## 🔐 Sécurité

- ✅ Mots de passe **hashés avec bcrypt**
- ✅ Vérification que le médecin accède uniquement à **ses rendez-vous**
- ✅ Session médecin séparée des patients
- ⚠️ **À faire** : Implémenter Flask-Login pour les médecins aussi

---

## 📱 Accès

### Patient
```
http://localhost:5000/login
```

### Médecin
```
http://localhost:5000/doctor/login
```

---

## 🎨 Interface

- 🎨 **Design moderne** avec cartes et statistiques
- 📊 **Graphiques visuels** pour les statistiques
- 🌈 **Badges colorés** pour les statuts
- 📱 **Responsive** : Fonctionne sur mobile et desktop

---

## 🧪 Test du Système

### 1. Tester la connexion médecin
```
1. Aller sur http://localhost:5000/doctor/login
2. Email: k.agbeko@chucampus.tg
3. Mot de passe: doctor123
4. Cliquer sur "Se connecter"
```

### 2. Créer un rendez-vous (côté patient)
```
1. Créer compte patient
2. Rechercher médecin
3. Réserver rendez-vous
```

### 3. Gérer le rendez-vous (côté médecin)
```
1. Se connecter comme médecin
2. Voir rendez-vous dans tableau de bord
3. Cliquer sur "Voir détails"
4. Ajouter notes de consultation
5. Marquer comme "Complété"
```

---

## 📝 Notes Importantes

- 💡 **Mot de passe par défaut** : Tous les médecins utilisent `doctor123`
- 🔄 **Changement recommandé** : Les médecins devraient changer leur mot de passe
- 📧 **Emails uniques** : Chaque médecin a un email unique
- 🏥 **Centres de santé** : Médecins liés à leurs centres respectifs

---

## 🚀 Démarrer l'Application

```bash
cd d:\PLP\bootcampProject\telehealth_connect
venv\Scripts\activate
python app.py
```

Accès :
- **Accueil** : http://localhost:5000
- **Espace Patient** : http://localhost:5000/login
- **Espace Médecin** : http://localhost:5000/doctor/login

---

## ✅ Checklist de Déploiement

- [x] Modèle Doctor avec authentification
- [x] Routes pour portail médecin
- [x] Templates pour interface médecin
- [x] Script de migration password_hash
- [x] Script de peuplement avec mots de passe
- [x] Blueprint enregistré dans app.py
- [x] Guide de documentation

---

**🇹🇬 TeleHealth Connect - Système Complet Patient & Médecin**

**Prochaine étape** : Implémenter Flask-Login pour les médecins (session plus sécurisée)
