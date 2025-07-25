CREATE DATABASE IF NOT EXISTS travel_management;
USE travel_management;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS user_to_trip;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS accommodation;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS transportation;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS destination;
DROP TABLE IF EXISTS app_user;

-- Create app_user table
CREATE TABLE app_user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL, 
    phone_number VARCHAR(20),
    street_num INT,
    street_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    registration_date DATE NOT NULL,
    CONSTRAINT chk_email CHECK (email LIKE '%_@__%.__%') 
);

-- Create destination table
CREATE TABLE destination (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    average_rating INT NOT NULL
);

-- Create trip table
CREATE TABLE trip (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    trip_type VARCHAR(50),
    destination_id INT,
    FOREIGN KEY (destination_id)
        REFERENCES destination (destination_id)
		ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create transportation table
CREATE TABLE transportation (
    transportation_id INT AUTO_INCREMENT PRIMARY KEY,
    transportation_type VARCHAR(50) NOT NULL,
    company VARCHAR(50) NOT NULL,
    departure_date DATE NOT NULL,
    arrival_date DATE NOT NULL,
    departure_location VARCHAR(50) NOT NULL,
    arrival_location VARCHAR(50) NOT NULL,
    trip_id INT NOT NULL,
    CONSTRAINT transportation_fk_trip FOREIGN KEY (trip_id)
        REFERENCES trip (trip_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create activities table
CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_name VARCHAR(50) NOT NULL,
    activity_description VARCHAR(2000) NOT NULL,
    activity_date DATE NOT NULL,
    location VARCHAR(50) NOT NULL,
    trip_id INT NOT NULL,
    CONSTRAINT activities_fk_trip FOREIGN KEY (trip_id)
        REFERENCES trip (trip_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create accommodation table
CREATE TABLE accommodation (
    accommodation_id INT AUTO_INCREMENT PRIMARY KEY,
    accommodation_name VARCHAR(50) NOT NULL,
    accommodation_type VARCHAR(50) NOT NULL,
    price_per_night INT NOT NULL,
    capacity INT NOT NULL,
    rating INT NOT NULL,
    destination_id INT NOT NULL,
    CONSTRAINT accommodation_fk_destination FOREIGN KEY (destination_id)
        REFERENCES destination (destination_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create booking table
CREATE TABLE booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_cost INT NOT NULL,
    booking_status VARCHAR(50) NOT NULL,
    trip_id INT NOT NULL,
    accommodation_id INT NOT NULL,
    CONSTRAINT booking_fk_trip FOREIGN KEY (trip_id)
        REFERENCES trip (trip_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT booking_fk_accommodation FOREIGN KEY (accommodation_id)
        REFERENCES accommodation (accommodation_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_method VARCHAR(50) NOT NULL,
    amount INT NOT NULL,
    payment_date DATE NOT NULL,
    transaction_status VARCHAR(50) NOT NULL,
    user_id INT NOT NULL,
    booking_id INT NOT NULL,
    CONSTRAINT payments_fk_app_user FOREIGN KEY (user_id)
        REFERENCES app_user (user_id)
		ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT payments_fk_booking FOREIGN KEY (booking_id)
        REFERENCES booking (booking_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create reviews table
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    rating INT NOT NULL,
    review_text VARCHAR(512) NOT NULL,
    review_date DATE NOT NULL,
    user_id INT NOT NULL,
    accommodation_id INT NOT NULL,
    CONSTRAINT reviews_fk_app_user FOREIGN KEY (user_id)
        REFERENCES app_user (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT reviews_fk_accommodation FOREIGN KEY (accommodation_id)
        REFERENCES accommodation (accommodation_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create user_to_trip table
CREATE TABLE user_to_trip (
    user_id INT NOT NULL,
    trip_id INT NOT NULL,
    PRIMARY KEY (user_id , trip_id),
    CONSTRAINT user_to_trip_fk_app_user FOREIGN KEY (user_id)
        REFERENCES app_user (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT user_to_trip_fk_trip FOREIGN KEY (trip_id)
        REFERENCES trip (trip_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- SAMPLE DATA -------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Insert into app_user
INSERT INTO app_user (first_name, last_name, email, phone_number, street_num, street_name, city, state, zip_code, registration_date)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 101, 'Main Street', 'Boston', 'MA', 02115, '2024-01-01'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', 202, 'Elm Street', 'Cambridge', 'MA', 02139, '2024-01-02'),
('Michael', 'Brown', 'michael.brown@example.com', '2345678901', 303, 'Oak Avenue', 'Newton', 'MA', 02458, '2024-01-03'),
('Emma', 'Davis', 'emma.davis@example.com', '3456789012', 404, 'Pine Lane', 'Somerville', 'MA', 02143, '2024-01-04'),
('Chris', 'Wilson', 'chris.wilson@example.com', '4567890123', 505, 'Maple Drive', 'Brookline', 'MA', 02446, '2024-01-05'),
('Sarah', 'Johnson', 'sarah.johnson@example.com', '5678901234', 606, 'Cedar Street', 'Waltham', 'MA', 02452, '2024-01-06'),
('David', 'Lee', 'david.lee@example.com', '6789012345', 707, 'Birch Road', 'Quincy', 'MA', 02169, '2024-01-07'),
('Laura', 'Martin', 'laura.martin@example.com', '7890123456', 808, 'Willow Court', 'Medford', 'MA', 02155, '2024-01-08'),
('James', 'Taylor', 'james.taylor@example.com', '8901234567', 909, 'Ash Circle', 'Malden', 'MA', 02148, '2024-01-09'),
('Olivia', 'White', 'olivia.white@example.com', '9012345678', 110, 'Spruce Boulevard', 'Revere', 'MA', 02151, '2024-01-10');

-- Insert into destination
INSERT INTO destination (location_name, country, average_rating)
VALUES 
('Paris', 'France', 3),
('New York', 'USA', 4),
('Tokyo', 'Japan', 5),
('Sydney', 'Australia', 5),
('Rome', 'Italy', 5),
('London', 'United Kingdom', 4),
('Barcelona', 'Spain', 4),
('Dubai', 'United Arab Emirates', 5),
('Singapore', 'Singapore', 3),
('Cape Town', 'South Africa', 5),
('Copenhagen', 'Denmark', 5),
('Dublin', 'Ireland', 3),
('Belfast', 'Northern Ireland', 4),
('Geneva', 'Switzerland', 5),
('Quebec', 'Canada', 3),
('Salzburg', 'Austria', 2),
('Reykjavik', 'Iceland', 5),
('Munich', 'Germany', 2),
('Vaduz', 'Liechtenstein', 3),
('Perth', 'Australia', 5),
('Boston', 'USA', 4);

-- Insert into trip
INSERT INTO trip (start_date, end_date, trip_type, destination_id)
VALUES 
('2024-06-01', '2024-06-10', 'Vacation', 1),
('2024-07-01', '2024-07-15', 'Business', 2),
('2024-01-05', '2024-01-12', 'Research', 3),
('2024-02-10', '2024-02-18', 'Business', 4),
('2024-03-01', '2024-03-07', 'Vacation', 5),
('2024-04-03', '2024-04-10', 'College Visit', 6),
('2024-05-10', '2024-05-20', 'Vacation', 7),
('2024-06-05', '2024-06-12', 'Business', 8),
('2024-07-01', '2024-07-08', 'Moving', 9),
('2024-08-05', '2024-08-12', 'Vacation', 10),
('2024-09-01', '2024-09-07', 'Research', 11),
('2024-10-01', '2024-10-10', 'Business', 12),
('2024-11-01', '2024-11-08', 'College Visit', 13),
('2024-12-01', '2024-12-10', 'Moving', 14),
('2024-02-15', '2024-02-22', 'Business', 15),
('2024-03-20', '2024-03-28', 'Vacation', 16),
('2024-04-25', '2024-05-02', 'College Visit', 17),
('2024-06-15', '2024-06-22', 'Vacation', 18),
('2024-08-01', '2024-08-08', 'Business', 19),
('2024-09-15', '2024-09-22', 'Research', 20),
('2024-10-20', '2024-10-27', 'College Visit', 21),
('2024-06-01', '2024-06-10', 'Vacation', 1),
('2024-07-01', '2024-07-15', 'Business', 2),
('2024-02-01', '2024-02-07', 'Research', 1),
('2024-08-15', '2024-08-22', 'Moving', 6),
('2024-04-03', '2024-04-10', 'Vacation', 10),
('2024-06-05', '2024-06-12', 'Business', 8),
('2024-07-01', '2024-07-15', 'College Visit', 13),
('2024-05-10', '2024-05-20', 'Research', 5),
('2024-10-15', '2024-10-22', 'Vacation', 1),
('2024-11-15', '2024-11-22', 'Business', 3),
('2024-06-15', '2024-06-22', 'Moving', 7),
('2024-12-05', '2024-12-12', 'Research', 14),
('2024-09-05', '2024-09-12', 'College Visit', 9),
('2024-08-20', '2024-08-27', 'Vacation', 17),
('2024-01-10', '2024-01-17', 'Business', 5),
('2024-07-10', '2024-07-17', 'Vacation', 8),
('2024-06-20', '2024-06-27', 'Research', 16),
('2024-02-10', '2024-02-17', 'Business', 9),
('2024-09-10', '2024-09-17', 'Vacation', 14);

-- Insert into transportation
INSERT INTO transportation (transportation_type, company, departure_date, arrival_date, departure_location, arrival_location, trip_id)
VALUES 
('Flight', 'Air France', '2024-06-1', '2024-06-1', 'Rome', 'Paris', 1),
('Train', 'Amtrak', '2024-07-1', '2024-07-1', 'Boston', 'New York', 2),
('Flight', 'Qantas', '2024-01-05', '2024-01-05', 'Sydney', 'Tokyo', 3),
('Train', 'ITA', '2024-02-10', '2024-02-10', 'Rome', 'Sydney', 4),
('Flight', 'ITA', '2024-03-01', '2024-03-01', 'London', 'Rome', 5),
('Flight', 'British Airways', '2024-04-03', '2024-04-03', 'Tokyo', 'London', 6),
('Flight', 'Emirates', '2024-05-10', '2024-05-10', 'Dubai', 'Barcelona', 7),
('Flight', 'Emirates', '2024-06-05', '2024-06-05', 'Barcelona', 'Dubai', 8),
('Flight', 'Singapore Airlines', '2024-07-01', '2024-07-01', 'Perth', 'Singapore', 9),
('Flight', 'South African Airways', '2024-08-05', '2024-08-05', 'Barcelona', 'Cape Town', 10);

-- Insert into activities
INSERT INTO activities (activity_name, activity_description, activity_date, location, trip_id)
VALUES 
('Museum Visit', 'Visit the Louvre Museum.', '2024-06-02', 'Paris', 1),
('Conference', 'Business conference at Times Square.', '2024-07-10', 'New York', 2),
('Cultural Tour', 'Explore the historical sites in Tokyo.', '2024-01-06', 'Tokyo', 3),
('Beach Day', 'Relax at Bondi Beach in Sydney.', '2024-04-05', 'Sydney', 4),
('Vatican Tour', 'Guided tour of the Vatican Museums in Rome.', '2024-03-02', 'Rome', 5),
('City Walk', 'Walk through the famous streets of London.', '2024-02-12', 'London', 6),
('Gaudí Architecture Tour', 'Explore the iconic works of Antoni Gaudí, including Sagrada Familia, Park Güell, and Casa Batlló.', '2024-05-12', 'Barcelona', 7),
('Shopping Spree', 'Shop at the famous Mall of the Emirates in Dubai.', '2024-05-12', 'Dubai', 8),
('Garden Visit', 'Explore the beautiful Gardens by the Bay in Singapore.', '2024-07-02', 'Singapore', 9),
('Safari Tour', 'Go on a safari adventure in Cape Town.', '2024-08-06', 'Cape Town', 10);

-- Insert into accommodation
INSERT INTO accommodation (accommodation_name, accommodation_type, price_per_night, capacity, rating, destination_id)
VALUES 
('Hilton Paris', 'Hotel', 250, 100, 5, 1),
('Marriott NYC', 'Hotel', 300, 85, 4, 2),
('Shibuya Excel Hotel Tokyu', 'Hotel', 120, 133, 4, 3),
('Cozy Studio in Darling Harbour', 'Airbnb', 180, 1, 4, 4),
('Hotel Artemide', 'Hotel', 250, 16, 4, 5), 
('Charming Flat in Notting Hill', 'Airbnb', 200, 1, 4, 6),
('Hostel One Barcelona', 'Hostel', 80, 58, 4, 7),
('Atlantis The Palm', 'Resort', 550, 68, 5, 8),
('Marina Bay Sands', 'Hotel', 500, 403, 5, 9),
('One&Only Cape Town', 'Resort', 650, 172, 5, 10);

-- Insert into booking
INSERT INTO booking (check_in_date, check_out_date, total_cost, booking_status, trip_id, accommodation_id)
VALUES 
('2024-06-01', '2024-06-10', 2250, 'Confirmed', 1, 1),
('2024-07-01', '2024-07-15', 4200, 'Confirmed', 2, 2),
('2024-01-05', '2024-01-12', 720, 'Confirmed', 3, 3),
('2024-02-10', '2024-02-18', 1260, 'Confirmed', 4, 4),
('2024-03-01', '2024-03-07', 1500, 'Confirmed', 5, 5),
('2024-04-03', '2024-04-10', 1200, 'Confirmed', 6, 6),
('2024-05-10', '2024-05-20', 720, 'Confirmed', 7, 7),
('2024-06-05', '2024-06-12', 3300, 'Confirmed', 8, 8),
('2024-07-01', '2024-07-08', 3500, 'Confirmed', 9, 9),
('2024-08-05', '2024-08-12', 3900, 'Confirmed', 10, 10);

-- Insert into payments
INSERT INTO payments (payment_method, amount, payment_date, transaction_status, user_id, booking_id)
VALUES 
('Credit Card', 2250, '2024-05-01', 'Completed', 1, 1),
('PayPal', 4200, '2024-07-01', 'Completed', 2, 2),
('Debit Card', 720, '2024-01-04', 'Completed', 3, 3), 
('Check', 1260, '2024-02-09', 'Completed', 4, 4), 
('Credit Card', 1500, '2024-02-28', 'Completed', 5, 5), 
('Credit Card', 1200, '2024-04-02', 'Completed', 6, 6), 
('Check', 720, '2024-05-09', 'Completed', 7, 7), 
('Debit Card', 3300, '2024-06-04', 'Completed', 8, 8), 
('Credit Card', 3500, '2024-06-30', 'Completed', 9, 9), 
('Credit Card', 3900, '2024-08-04', 'Completed', 10, 10);

-- Insert into reviews
INSERT INTO reviews (rating, review_text, review_date, user_id, accommodation_id)
VALUES 
(5, 'Amazing stay with great service.', '2024-06-15', 1, 1),
(3, 'Good experience, but room service was slow.', '2024-07-18', 2, 2),
(5, 'Cozy Studio in Darling Harbour was perfect for my stay. Great location and comfortable space.', '2024-02-20', 4, 4),
(1, 'The room was dirty and not as described. Very disappointing stay.', '2024-02-20', 4, 4),
(4, 'Hotel Artemide had great amenities, but the breakfast could have been better.', '2024-03-09', 5, 5),
(5, 'Charming Flat in Notting Hill was lovely. The flat had everything we needed for a relaxing stay.', '2024-04-12', 6, 6),
(1, 'Hostel One Barcelona was not what I expected. The place was noisy and uncomfortable.', '2024-05-22', 7, 7),
(2, 'Atlantis The Palm was beautiful, but the staff was unhelpful and the service was slow.', '2024-06-14', 8, 8),
(5, 'Marina Bay Sands was an unforgettable experience. The pool and view were exceptional.', '2024-07-10', 9, 9),
(5, 'One&Only Cape Town was incredible. Amazing service and views. Will definitely return.', '2024-08-14', 10, 10);

-- Insert into user_to_trip
INSERT INTO user_to_trip (user_id, trip_id)
VALUES 
(1, 1),  
(2, 2), 
(3, 3),
(4, 4), 
(5, 5),
(6, 6),
(7, 7), 
(8, 8), 
(9, 9), 
(10, 10);
-- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- FUNCTIONS ------------------------------------------------------------------------------------------------------------------------------------------------------------- 

-- SELECT count_user_bookings(1); 

DELIMITER //
CREATE FUNCTION count_user_bookings(user_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total_bookings INT;
    
    SELECT COUNT(*) 
    INTO total_bookings
    FROM booking
    WHERE user_id = user_id;
    
    RETURN total_bookings;
END //



-- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- PROCEDURES ---------------------------------------------------------------------------------------------------------------------------------------------------------------

-- CALL calculate_total_revenue_for_user(1, '2024-01-01', '2024-12-31');

DELIMITER //
CREATE PROCEDURE calculate_total_revenue_for_user(
    IN userId INT, 
    IN startDate DATE, 
    IN endDate DATE
)
BEGIN
    DECLARE totalRevenue DECIMAL(10, 2);
    
    -- Calculate the total revenue from bookings for the user within the specified period
    SELECT 
        SUM(b.total_cost) INTO totalRevenue
    FROM booking b
    JOIN user_to_trip ut ON b.trip_id = ut.trip_id
    WHERE ut.user_id = userId
    AND b.booking_status = 'Confirmed'  -- Only count confirmed bookings
    AND b.check_in_date BETWEEN startDate AND endDate;
    
    -- Return the total revenue, if any
    IF totalRevenue IS NULL THEN
        SET totalRevenue = 0;
    END IF;
    
    -- Return the result
    SELECT totalRevenue AS total_revenue;
END //

-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- EXTRA CREDIT: DATA QUERIES

-- Query 1: Find the most popular destinations this year (do not include destinations that have not been visited)

SELECT 
    d.location_name
FROM
    destination d
        JOIN
    trip t ON d.destination_id = t.destination_id
WHERE
    YEAR(t.start_date) = YEAR(CURDATE())
GROUP BY d.destination_id
ORDER BY COUNT(*) DESC;

-- Query 2: Display the number of trips made each month to find the busy/not busy months in the current year

SELECT 
    MONTHNAME(t.start_date) AS trip_month,
    COUNT(*) as trip_count
FROM
    destination d
        JOIN
    trip t ON d.destination_id = t.destination_id
WHERE
    YEAR(t.start_date) = YEAR(CURDATE())
GROUP BY MONTH(t.start_date)
ORDER BY trip_count DESC;

-- Query 3: Display the number of trip that are within various duration ranges

SELECT
    CASE 
        WHEN DATEDIFF(end_date, start_date) BETWEEN 0 AND 3 THEN '0-3 Days'
        WHEN DATEDIFF(end_date, start_date) BETWEEN 4 AND 7 THEN '4-7 Days'
        WHEN DATEDIFF(end_date, start_date) BETWEEN 8 AND 14 THEN '8-14 Days'
        WHEN DATEDIFF(end_date, start_date) > 14 THEN 'More than 14 Days'
    END AS trip_duration_range,
    COUNT(*) AS trip_count
FROM trip
GROUP BY trip_duration_range
ORDER BY trip_duration_range;

-- Query 4: Display the hotels and their locations with an average 4 or 5 star review rating (not the rating in the accommodation table)

SELECT 
    a.accommodation_name,
    d.location_name,
    AVG(r.rating) AS average_rating
FROM
    accommodation a
        JOIN
    reviews r ON a.accommodation_id = r.accommodation_id
        JOIN
    destination d ON a.destination_id = d.destination_id
GROUP BY a.accommodation_id
HAVING average_rating >= 4
ORDER BY average_rating DESC , accommodation_name DESC;

-- Query 5: Display accommodation, activities, and transportation for each trip in date order
;
SELECT 
	trip_id,
    event_type,
    event_description,
    event_start_date,
    event_end_date
FROM (
(SELECT 
    t.trip_id as trip_id,
    CONCAT(u.first_name,
            ' ',
            u.last_name,
            ' | ',
            t.trip_type,
            ' | ',
            d.location_name,
            ' on ',
            t.start_date) AS trip_name,
    'Accommodation' AS event_type,
    a.accommodation_name AS event_description,
    b.check_in_date AS event_start_date,
    b.check_out_date AS event_end_date
FROM
    trip t
        JOIN
    booking b ON t.trip_id = b.trip_id
        JOIN
    accommodation a ON b.accommodation_id = a.accommodation_id
        JOIN
    user_to_trip u2t ON u2t.trip_id = t.trip_id
        JOIN
    app_user u ON u.user_id = u2t.user_id
        JOIN
    destination d ON t.destination_id = d.destination_id) UNION (
SELECT 
    t.trip_id AS trip_id,
    CONCAT(u.first_name,
            ' ',
            u.last_name,
            ' | ',
            t.trip_type,
            ' | ',
            d.location_name,
            ' on ',
            t.start_date) AS trip_name,
    'Activity' AS event_type,
    av.activity_name AS event_description,
    av.activity_date AS event_start_date,
    av.activity_date AS event_end_date
FROM
    trip t
        JOIN
    user_to_trip u2t ON u2t.trip_id = t.trip_id
        JOIN
    app_user u ON u.user_id = u2t.user_id
        JOIN
    destination d ON t.destination_id = d.destination_id
        JOIN
    activities av ON av.trip_id = t.trip_id) UNION (
SELECT 
    t.trip_id as trip_id,
    CONCAT(u.first_name,
            ' ',
            u.last_name,
            ' | ',
            t.trip_type,
            ' | ',
            d.location_name,
            ' on ',
            t.start_date) AS trip_name,
    'Transportation' AS event_type,
    CONCAT(tr.company, ' ', tr.transportation_type) AS event_description,
    tr.departure_date AS event_start_date,
    tr.arrival_date AS event_end_date
FROM
    trip t
        JOIN
    user_to_trip u2t ON u2t.trip_id = t.trip_id
        JOIN
    app_user u ON u.user_id = u2t.user_id
        JOIN
    destination d ON t.destination_id = d.destination_id
		JOIN
	transportation tr ON tr.trip_id = t.trip_id)) trip_info
    ORDER BY trip_id ASC, event_start_date ASC, event_type DESC
    

