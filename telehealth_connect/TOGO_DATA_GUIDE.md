# 🇹🇬 Guide de Configuration avec Données Togolaises

## Options pour Peupler la Base de Données

Vous avez **2 options** pour ajouter les données togolaises à votre application :

---

## ✅ **OPTION 1 : Utiliser le Script Python (Recommandé)**

Cette méthode utilise un script Python pour peupler la base de données.

### Étapes :

1. **Assurez-vous que l'application fonctionne**
   ```bash
   cd d:\PLP\bootcampProject\telehealth_connect
   venv\Scripts\activate
   ```

2. **Exécutez le script de peuplement**
   ```bash
   python populate_togo_data.py
   ```

3. **Résultat attendu**
   ```
   🇹🇬 Démarrage du peuplement de la base de données...
   ============================================================

   🗑️  Suppression des données existantes...
   ✓ Données existantes supprimées

   🏥 Ajout des centres de santé du Togo...
     ✓ CHU Campus de Lomé - Lomé
     ✓ CHU Sylvanus Olympio - Lomé
     ... (10 centres au total)

   👨‍⚕️ Ajout des médecins togolais...
     ✓ Dr. Kofi Agbéko - Médecine Générale
     ✓ Dr. Ama Koffi - Pédiatrie
     ... (16 médecins au total)

   ✅ Base de données peuplée avec succès!
   ```

### Avantages :
- ✅ Rapide et facile
- ✅ Supprime automatiquement les anciennes données
- ✅ Affiche un résumé détaillé
- ✅ Gère les erreurs automatiquement

---

## 🔧 **OPTION 2 : Utiliser MySQL directement**

Cette méthode utilise le fichier SQL pour créer et peupler la base de données.

### Étapes :

1. **Ouvrez MySQL**
   ```bash
   mysql -u root -p
   ```

2. **Exécutez le fichier SQL**
   ```sql
   SOURCE d:/PLP/bootcampProject/telehealth_connect/schema_togo.sql;
   ```

   Ou depuis l'invite de commande :
   ```bash
   mysql -u root -p < schema_togo.sql
   ```

### Avantages :
- ✅ Crée la base de données complète en une seule fois
- ✅ Pas besoin de Python
- ✅ Peut être utilisé pour réinitialiser complètement

---

## 📊 Données Incluses

### 🏥 **10 Centres de Santé**

| Ville | Centres |
|-------|---------|
| **Lomé** | CHU Campus, CHU Sylvanus Olympio, Clinique Biasa, Hôpital de Bè, Clinique Internationale du Golfe |
| **Sokodé** | CHR de Sokodé |
| **Kara** | CHR de Kara |
| **Tsévié** | Hôpital de Tsévié |
| **Atakpamé** | CHR d'Atakpamé |
| **Dapaong** | Hôpital de Dapaong |

### 👨‍⚕️ **16 Médecins Togolais**

Spécialités disponibles :
- Médecine Générale (4 médecins)
- Pédiatrie (2 médecins)
- Cardiologie
- Gynécologie-Obstétrique
- Chirurgie Générale
- Dermatologie
- Ophtalmologie
- Médecine Interne
- Traumatologie
- Neurologie
- Gastro-entérologie
- Radiologie

### 💰 **Tarifs de Consultation**

Les frais de consultation sont en **Francs CFA (FCFA)** :
- Médecine Générale : 10 000 - 15 000 FCFA
- Spécialités : 14 000 - 30 000 FCFA

---

## 🚀 Démarrer l'Application

Après avoir peuplé la base de données :

```bash
python app.py
```

Puis visitez : **http://localhost:5000**

---

## 🔄 Réinitialiser les Données

Pour réinitialiser et repeupler :

```bash
# Option 1 : Réexécuter le script Python
python populate_togo_data.py

# Option 2 : Réexécuter le fichier SQL
mysql -u root -p < schema_togo.sql
```

---

## 🎯 Tester l'Application

1. **Créez un compte patient** (inscription)
2. **Connectez-vous**
3. **Recherchez des médecins** par ville ou spécialité
4. **Réservez un rendez-vous** avec un médecin togolais

---

## 📝 Notes Importantes

- Les numéros de téléphone utilisent le format togolais (+228)
- Les adresses sont réelles ou basées sur des emplacements réels au Togo
- Les coordonnées GPS sont approximatives pour les grandes villes
- Les tarifs sont en FCFA (Franc CFA)

---

## ❓ En Cas de Problème

Si vous rencontrez une erreur :

1. **Vérifiez que MySQL est démarré**
2. **Vérifiez les identifiants dans `.env`**
3. **Vérifiez que la base de données existe** :
   ```sql
   SHOW DATABASES;
   USE telehealth_db;
   SHOW TABLES;
   ```

---

**🇹🇬 Votre application TeleHealth Connect est maintenant prête avec des données togolaises !**
