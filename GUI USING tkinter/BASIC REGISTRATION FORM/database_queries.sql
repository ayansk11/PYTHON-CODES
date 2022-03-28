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


#insert sp
delimiter &&
create procedure sp_insert(name varchar(80), phone_no numeric, gender varchar(15), email varchar(80))
begin
insert into data (name, phone_no, gender, email) VALUES (name , phone_no, gender, email);
end&&
delimiter ;

call sp_insert("values")


#display sp
delimiter &&
create procedure sp_display()
begin
select * from data;
end&&
delimiter ;

call sp_display()


#delete row sp
delimiter &&
create procedure sp_delete_row(c_id_no int)
begin
delete from data where c_id = c_id_no;
end&&
delimiter ;

call sp_delete_row("value")