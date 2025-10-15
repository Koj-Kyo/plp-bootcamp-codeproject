-- TeleHealth Connect Database Schema
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

-- Sample data for testing
INSERT INTO health_centers (name, address, city, state, postal_code, phone, latitude, longitude) VALUES
('Central Medical Center', '123 Main Street', 'New York', 'NY', '10001', '212-555-0100', 40.7128, -74.0060),
('Riverside Health Clinic', '456 River Road', 'Los Angeles', 'CA', '90001', '213-555-0200', 34.0522, -118.2437),
('Sunrise Healthcare', '789 Oak Avenue', 'Chicago', 'IL', '60601', '312-555-0300', 41.8781, -87.6298);

INSERT INTO doctors (health_center_id, first_name, last_name, specialization, email, phone, qualification, experience_years, consultation_fee, available) VALUES
(1, 'John', 'Smith', 'General Physician', 'john.smith@centralmedical.com', '212-555-0101', 'MD', 10, 100.00, TRUE),
(1, 'Sarah', 'Johnson', 'Cardiologist', 'sarah.johnson@centralmedical.com', '212-555-0102', 'MD, FACC', 15, 150.00, TRUE),
(2, 'Michael', 'Brown', 'Pediatrician', 'michael.brown@riverside.com', '213-555-0201', 'MD, FAAP', 8, 120.00, TRUE),
(2, 'Emily', 'Davis', 'Dermatologist', 'emily.davis@riverside.com', '213-555-0202', 'MD, FAAD', 12, 130.00, TRUE),
(3, 'David', 'Wilson', 'Orthopedic Surgeon', 'david.wilson@sunrise.com', '312-555-0301', 'MD, FAAOS', 20, 180.00, TRUE),
(3, 'Lisa', 'Anderson', 'General Physician', 'lisa.anderson@sunrise.com', '312-555-0302', 'MD', 7, 100.00, TRUE);
