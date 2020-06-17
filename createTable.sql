CREATE TABLE IF NOT EXISTS promotion (
    id SERIAL,
    external_id VARCHAR (36) ,
    price NUMERIC (5,2) NOT NULL,
    expiration_date  VARCHAR(100) NOT NULL 
);
