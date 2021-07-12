/*
    Campbell Alexander
    Outland Adventures
    11JUL2021
    Professor Sampson
*/

 
DROP USER IF EXISTS 'Outland_Adventure_user'@'localhost';

 
CREATE USER 'Outland_Adventure_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';


GRANT ALL PRIVILEGES ON Outland_Adventure.* TO'Outland_Adventure_user'@'localhost';