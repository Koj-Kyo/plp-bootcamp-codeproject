-- TeleHealth Connect Database Schema - Version Togo
-- Database: telehealth_db

CREATE DATABASE IF NOT EXISTS telehealth_db;
USE telehealth_db;

-- Health Centers Table
CREATE TABLE health_centers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    address VARCHAR(300) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20),
    phone VARCHAR(20),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients Table
CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    address VARCHAR(300),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Doctors Table
CREATE TABLE doctors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    health_center_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(20),
    qualification VARCHAR(200),
    experience_years INT,
    consultation_fee DECIMAL(10, 2),
    available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (health_center_id) REFERENCES health_centers(id) ON DELETE CASCADE
);

-- Appointments Table
CREATE TABLE appointments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status ENUM('scheduled', 'completed', 'cancelled', 'no-show') DEFAULT 'scheduled',
    reason VARCHAR(500),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE,
    UNIQUE KEY unique_appointment (doctor_id, appointment_date, appointment_time)
);

-- Create indexes for better query performance
CREATE INDEX idx_patient_email ON patients(email);
CREATE INDEX idx_doctor_specialization ON doctors(specialization);
CREATE INDEX idx_doctor_health_center ON doctors(health_center_id);
CREATE INDEX idx_appointment_patient ON appointments(patient_id);
CREATE INDEX idx_appointment_doctor ON appointments(doctor_id);
CREATE INDEX idx_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_health_center_city ON health_centers(city);

-- ===============================================
-- DONNÉES TOGOLAISES 🇹🇬
-- ===============================================

-- Centres de santé au Togo
INSERT INTO health_centers (name, address, city, state, postal_code, phone, latitude, longitude) VALUES
('CHU Campus de Lomé', 'Boulevard du 13 Janvier', 'Lomé', 'Maritime', 'BP 57', '+228 22 25 00 01', 6.17250000, 1.23140000),
('CHU Sylvanus Olympio', 'Rue du Marché', 'Lomé', 'Maritime', 'BP 2000', '+228 22 21 25 01', 6.12560000, 1.21160000),
('Clinique Biasa', 'Quartier Tokoin', 'Lomé', 'Maritime', 'BP 12345', '+228 22 21 84 00', 6.16280000, 1.22550000),
('Hôpital de Bè', 'Quartier Bè-Kpota', 'Lomé', 'Maritime', 'BP 3003', '+228 22 21 28 30', 6.14610000, 1.20580000),
('CHR de Sokodé', 'Avenue de la Paix', 'Sokodé', 'Centrale', 'BP 88', '+228 25 50 00 24', 8.98330000, 1.13330000),
('CHR de Kara', 'Route Nationale N°1', 'Kara', 'Kara', 'BP 18', '+228 26 60 00 34', 9.55110000, 1.18640000),
('Hôpital de Tsévié', 'Centre-ville', 'Tsévié', 'Maritime', 'BP 33', '+228 23 31 00 15', 6.42620000, 1.21360000),
('CHR d\'Atakpamé', 'Quartier Administratif', 'Atakpamé', 'Plateaux', 'BP 14', '+228 24 40 00 22', 7.53330000, 1.11670000),
('Hôpital de Dapaong', 'Centre-ville', 'Dapaong', 'Savanes', 'BP 10', '+228 27 70 00 18', 10.86310000, 0.20720000),
('Clinique Internationale du Golfe', 'Boulevard du Mono', 'Lomé', 'Maritime', 'BP 8394', '+228 22 27 13 13', 6.13190000, 1.22230000);

-- Médecins togolais
INSERT INTO doctors (health_center_id, first_name, last_name, specialization, email, phone, qualification, experience_years, consultation_fee, available) VALUES
-- CHU Campus de Lomé (id: 1)
(1, 'Kofi', 'Agbéko', 'Médecine Générale', 'k.agbeko@chu-lome.tg', '+228 90 12 34 56', 'Docteur en Médecine', 12, 15000.00, TRUE),
(1, 'Ama', 'Koffi', 'Pédiatrie', 'a.koffi@chu-lome.tg', '+228 90 23 45 67', 'Pédiatre, Diplômée de Dakar', 8, 18000.00, TRUE),

-- CHU Sylvanus Olympio (id: 2)
(2, 'Edem', 'Attiogbé', 'Cardiologie', 'e.attiogbe@sylvanus.tg', '+228 90 34 56 78', 'Cardiologue, Spécialiste', 15, 25000.00, TRUE),
(2, 'Dzifa', 'Amegavi', 'Gynécologie-Obstétrique', 'd.amegavi@sylvanus.tg', '+228 90 45 67 89', 'Gynécologue-Obstétricienne', 10, 20000.00, TRUE),

-- Clinique Biasa (id: 3)
(3, 'Komi', 'Gbadamassi', 'Chirurgie Générale', 'k.gbadamassi@biasa.tg', '+228 90 56 78 90', 'Chirurgien, Spécialiste', 18, 30000.00, TRUE),
(3, 'Akossiwa', 'Dogbey', 'Dermatologie', 'a.dogbey@biasa.tg', '+228 90 67 89 01', 'Dermatologue', 7, 17000.00, TRUE),

-- Hôpital de Bè (id: 4)
(4, 'Yao', 'Kouassi', 'Médecine Générale', 'y.kouassi@be.tg', '+228 90 78 90 12', 'Médecin Généraliste', 9, 12000.00, TRUE),
(4, 'Afi', 'Tete', 'Ophtalmologie', 'a.tete@be.tg', '+228 90 89 01 23', 'Ophtalmologue', 11, 22000.00, TRUE),

-- CHR de Sokodé (id: 5)
(5, 'Kossi', 'Atcholi', 'Médecine Interne', 'k.atcholi@sokode.tg', '+228 91 12 34 56', 'Interniste', 13, 16000.00, TRUE),
(5, 'Efua', 'Lamisi', 'Pédiatrie', 'e.lamisi@sokode.tg', '+228 91 23 45 67', 'Pédiatre', 6, 14000.00, TRUE),

-- CHR de Kara (id: 6)
(6, 'Yaovi', 'Komlan', 'Traumatologie', 'y.komlan@kara.tg', '+228 92 34 56 78', 'Traumatologue', 14, 19000.00, TRUE),

-- Hôpital de Tsévié (id: 7)
(7, 'Abla', 'Akakpo', 'Médecine Générale', 'a.akakpo@tsevie.tg', '+228 93 45 67 89', 'Médecin Généraliste', 5, 10000.00, TRUE),

-- CHR d'Atakpamé (id: 8)
(8, 'Kwame', 'Adjoyi', 'Neurologie', 'k.adjoyi@atakpame.tg', '+228 94 56 78 90', 'Neurologue', 10, 23000.00, TRUE),

-- Hôpital de Dapaong (id: 9)
(9, 'Sena', 'Aziagbe', 'Médecine Générale', 's.aziagbe@dapaong.tg', '+228 95 67 89 01', 'Médecin Généraliste', 8, 11000.00, TRUE),

-- Clinique Internationale du Golfe (id: 10)
(10, 'Ekoué', 'Mensah', 'Gastro-entérologie', 'e.mensah@golfe.tg', '+228 96 78 90 12', 'Gastro-entérologue', 16, 27000.00, TRUE),
(10, 'Ayélé', 'Kpelafia', 'Radiologie', 'a.kpelafia@golfe.tg', '+228 97 89 01 23', 'Radiologue', 9, 20000.00, TRUE);
