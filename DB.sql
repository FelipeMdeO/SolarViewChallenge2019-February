create database nasadata
default character set utf8
default collate utf8_general_ci;

use nasadata;

create table irradiation2 (
id int unsigned not null auto_increment,
latitude decimal(5,2),
longitude decimal(5,2),
year smallint unsigned,
month tinyint unsigned,
incidence float,
primary key (id)
) default charset = utf8mb4;

# To test
#DROP TABLE irradiation;
# INSERT INTO irradiation (latitude, longitude, year, month, incidence) VALUES (-131.406, -154.4336, 1981, 01, -999.0);