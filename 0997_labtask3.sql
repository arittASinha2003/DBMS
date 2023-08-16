create table students (sid int primary key, aadhaar int unique, age int not null check (age >= 18 and age < 25));
desc students;
select * from students;

insert into students values (1, 1234567890, 18);
insert into students values (2, 1023456789, 19);
insert into students values (3, 1203456789, 20);
insert into students values (4, 1230456789, 21);

insert into students values (1, 1234056789, 22);
insert into students values (5, 1203456789, 23);
insert into students values (6, 1234506789, 25);
insert into students values (5, 1234056789, 20);
