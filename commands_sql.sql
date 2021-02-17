create database teacher_userdata
use teacher_userdata
create table userdetails (username varchar(32),password varchar(32),classt char(3) UNIQUE)
insert into userdetails values ('dwayne','mathsisgod','12a'),('jeff','thexactr','12b'),('theta_jr','costheta','12e'),('derryl','twist4fun','12d'),('shahid','salam2alaikum','12c')
select * from userdetails
alter table userdetails add(classt char(3))
drop table userdetails
alter table userdetails drop d13_11_2020
drop database j_db
select * from timet
insert into timet (Period1,Period2,Period3,Period4,Period5,Period6,Period7,Period8,Period9) values ('XII-B',NULL,'XI-D',NULL,NULL,'XII-F',NULL,
update timet set Period1=NULL,Period2='XII-B',Period3=NULL,Period4=NULL,Period5='XI-E',Period6='XII-B',Period7=NULL,Period8=NULL,Period9='XII-F' where Day_Period='Friday'
insert into timet(Day_Period) values ('Monday')
desc timet
alter table timet modify Period9 varchar(6)
show databases
use jeff_db
show tables
SET SQL_SAFE_UPDATES = 0;
select * from attendence order by 
insert into attendence values ('name12','sabc12')
alter table attendence drop 18_12_2020
show databases;
use sakila;show tables;
select * from actor,actor_info
select * from actor natural join actor_info
create view davi2d as (select * from actor where last_name like 'P%' group by last_update )
select * from actor a , actor_info b where a.first_name=b.first_name
drop view davi2d
select * from actor b inner join actor_info a on a.first_name=b.first_name
select 2*3 as abd from dual
create table student_details (select studentname,admn_no from attendence) 
select * from student_details
UPDATE student_details SET blood_group='AB+' where admn_no in ('sabc1','sabc2')
alter table student_details add (gender varchar(15),contact_no varchar(15),address varchar(100),blood_group varchar(3),disciplinary_records varchar(100) )
INSERT INTO student_details (Father_name,gender,contact_no,address,blood_group,disciplinary_records) VALUES (father1
UPDATE student_details SET Father_name='Father3',gender='Female',contact_no='9999999999',address='31,B block,Dalk Apartments,Agra-223010',blood_group='O+',disciplinary_records='1 Yellow Card' WHERE admn_no='sabc3'
UPDATE student_details SET address='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',blood_group='AB-',disciplinary_records='2 Yellow Cards , 1 Red Card' WHERE admn_no='sabc4'
SET SQL_SAFE_UPDATES = 0;

