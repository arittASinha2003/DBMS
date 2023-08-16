create table sailors (sid int primary key, sname varchar2(15), rating int, age int);
create table boats (bid int primary key, bname varchar2(15), color varchar2(10));
create table reserves (sid int, bid int, day date, primary key (sid, bid, day), constraint r_fk1 foreign key (sid) references sailors (sid), constraint r_fk2 foreign key (bid) references boats (bid));

insert into sailors values (22, 'Dustin', 7, 45);
insert into sailors values (29, 'Brutus', 1, 33);
insert into sailors values (31, 'Lubber', 8, 55);
insert into sailors values (32, 'Andy', 8, 25);
insert into sailors values (58, 'Rusty', 10, 35);
insert into sailors values (64, 'Horatio', 7, 35);
insert into sailors values (71, 'Zorba', 10, 16);
insert into sailors values (74, 'Horatio', 9, 35);
insert into sailors values (85, 'Art', 3, 25);
insert into sailors values (95, 'Bob', 3, 63);

insert into boats values (101, 'Interlake', 'Blue');
insert into boats values (102, 'Interlske', 'Red');
insert into boats values (103, 'Clipper', 'Green');
insert into boats values (104, 'Marine', 'Red');

insert into reserves values (22, 101, '10-OCT-1998');
insert into reserves values (22, 102, '10-OCT-1998');
insert into reserves values (22, 103, '10-AUG-1998');
insert into reserves values (22, 104, '10-JUL-1998');
insert into reserves values (31, 102, '11-OCT-1998');
insert into reserves values (31, 103, '11-JUN-1998');
insert into reserves values (31, 104, '11-DEC-1998');
insert into reserves values (64, 101, '09-MAY-1998');
insert into reserves values (64, 102, '09-AUG-1998');
insert into reserves values (74, 103, '09-AUG-1998');

select * from sailors;
select * from boats;
select * from reserves;

select * from sailors where rating > 8;
select sname, rating from sailors where age > 20;
select * from sailors S where S.rating > 8;
select S.sname from sailors S, reserves R where R.bid = 103 and S.sid = R.sid;
select R.sid from reserves R, boats B where B.color = 'Red' and R.bid = B.bid;
