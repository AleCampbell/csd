/*
    
    Campbell, Alexander
    11 JUL2021
    Outland Adventure
*/


/*
-- drop contstraints if they exist
ALTER TABLE location DROP FOREIGN KEY fk_trip;
ALTER TABLE trip DROP FOREIGN KEY fk_customer;
ALTER TABLE trip DROP FOREIGN KEY fk_equiptment;
ALTER TABLE equiptment DROP FOREIGN KEY fk_acquisition_Date;
ALTER TABLE trip DROP FOREIGN KEY fk_bookings;
*/

-- drop tables if they exist
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS equiptment;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS acquisition_Date;


/*
    Create table(s)
*/

CREATE TABLE location (
    country_id    INT             NOT NULL    AUTO_INCREMENT,
    trips_available  VARCHAR(30)     NOT NULL,
    PRIMARY KEY(location_id)
);

CREATE TABLE trip (
    date_depart         DATE             NOT NULL    AUTO_INCREMENT,
    date_return       DATE     NOT NULL,
    equiptment_req           VARCHAR(30)             NOT NULL,
    PRIMARY KEY(trip)_id) 
);

CREATE TABLE customer (
    product_order_id   INT             NOT NULL    AUTO_INCREMENT,
    date_depart      DATE            NOT NULL,
    date_return         DATE             NOT NULL,
    equiptment           VARCHAR(30)             NOT NULL,
    equiptment_sales      VARCHAR(30)           NOT NULL,
    customer_name    VARCHAR(30)             NOT NULL,
    PRIMARY KEY(customer_id),
);




CREATE TABLE equiptment (
    equiptment_id         INT             NOT NULL    AUTO_INCREMENT,
    equiptment_name         VARCHAR(30)     NOT NULL,
    equiptment_sales            INT             NOT NULL,
    PRIMARY KEY(equiptment_id) 
);

CREATE TABLE bookings (
    customer_id        INT             NOT NULL    AUTO_INCREMENT,
    customer_name      VARCHAR(30)     NOT NULL,
    PRIMARY KEY(suppliers_id) 
);

CREATE TABLE bookings (
    total_customer     INT             NOT NULL    AUTO_INCREMENT,
    trip_id          DATE            NOT NULL,
    location_id         INT             NOT NULL,
);




CREATE TABLE acquisition_date (
    equiptment_id         INT             NOT NULL    AUTO_INCREMENT,
    equiptment_name          VARCHAR(30)     NOT NULL,
    equiptment_cost           VARCHAR(30)     NOT NULL,
    equiptment_acquired          DATE     NOT NULL,
    PRIMARY KEY(employee_id) 
);

