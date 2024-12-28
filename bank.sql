create database bank;
use bank;
create table user(__account_no int primary key, name varchar(50),__password varchar(12) not null, balance float);
create table debit(__account_no int primary key , debit_ammount float, balance float, foreign key (__account_no) references user(__account_no));
create table credit(__account_no int primary key , credit_ammount float, balance float, foreign key (__account_no) references user(__account_no)); 
select * from user;
select*from debit;
select * from credit;
