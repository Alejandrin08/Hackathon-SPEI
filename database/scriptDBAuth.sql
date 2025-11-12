IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'auth_db')
BEGIN
    CREATE DATABASE auth_db
    COLLATE Modern_Spanish_CS_AS;
END
GO

USE auth_db;
GO

-- -----------------------------------------------------
-- Tabla: users
-- Almacena la identidad principal y credenciales.
-- -----------------------------------------------------
CREATE TABLE users (
    id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    email VARCHAR(255) NULL,
    hashed_password VARCHAR(255) NOT NULL,
    [user_name] VARCHAR(100) NOT NULL,
    preferred_language VARCHAR(10) NOT NULL DEFAULT 'es-MX',
    created_at DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    updated_at DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    
    CONSTRAINT PK_users PRIMARY KEY (id),
    
    CONSTRAINT UQ_users_email UNIQUE (email)
);
GO

-- -----------------------------------------------------
-- Tabla: accessibility_profiles
-- Almacena las preferencias de accesibilidad del usuario
-- -----------------------------------------------------
CREATE TABLE accessibility_profiles (
    id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    user_id UNIQUEIDENTIFIER NOT NULL,
    
    alias VARCHAR(100) NULL, 
    age_range VARCHAR(50) NULL,   
    theme VARCHAR(50) NOT NULL DEFAULT 'claro', -- "claro", "oscuro", "alto_contraste"
    font_scale DECIMAL(2, 1) NOT NULL DEFAULT 1.0, -- Resultado de "¿Te cuesta leer texto pequeño?"
    voice_feedback BIT NOT NULL DEFAULT 0, -- "¿Necesita apoyo de voz? si/no"
    screen_reader_mode BIT NOT NULL DEFAULT 0, -- "¿Usar lector de pantalla? si/no"
    nudging_level VARCHAR(50) NOT NULL DEFAULT 'medium', -- "¿Cómo se siente? 'low' (muy comoda), 'medium' (mas o menos), 'high' (cuesta bastante)"
    literacy_level VARCHAR(50) NULL, -- "¿Dificultad leer/escribir? 'no_problemas', 'a_veces_cuesta', 'cuesta'"
    updated_at DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    
    CONSTRAINT PK_accessibility_profiles PRIMARY KEY (id),

    CONSTRAINT FK_accessibility_profiles_users 
        FOREIGN KEY (user_id) 
        REFERENCES users(id)
        ON DELETE CASCADE, 

    CONSTRAINT UQ_accessibility_profiles_user_id UNIQUE (user_id),
    
    CONSTRAINT CHK_accessibility_theme CHECK (theme IN ('claro', 'oscuro', 'alto_contraste')),
    CONSTRAINT CHK_accessibility_nudging_level CHECK (nudging_level IN ('low', 'medium', 'high')),
    CONSTRAINT CHK_accessibility_age_range CHECK (age_range IN ('18_30', '31_50', '51_60', 'mas_60', NULL)),
    CONSTRAINT CHK_accessibility_literacy_level CHECK (literacy_level IN ('no_problemas', 'a_veces_cuesta', 'cuesta', NULL))
);
GO

-- -----------------------------------------------------
-- Tabla: consent_records
-- Almacena los consentimientos del usuario
-- -----------------------------------------------------
CREATE TABLE consent_records (
    id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    user_id UNIQUEIDENTIFIER NOT NULL,
    granted BIT NOT NULL DEFAULT 0,
    timestamp DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    revoked_at DATETIME2 NULL, 

    CONSTRAINT PK_consent_records PRIMARY KEY (id),

    CONSTRAINT FK_consent_records_users 
        FOREIGN KEY (user_id) 
        REFERENCES users(id)
        ON DELETE CASCADE 
);
GO