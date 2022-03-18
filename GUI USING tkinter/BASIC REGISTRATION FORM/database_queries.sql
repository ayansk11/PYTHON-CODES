create database gui;

use gui;

create table data
(
	c_id int NOT NULL AUTO_INCREMENT,
    name varchar(80),
    phone_no numeric unique,
    gender varchar(15),
    email varchar(80),
    Primary key(c_id)
    
);

delete from data where c_id = 1;

select * from data;