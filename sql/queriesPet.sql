create database turfe;

create table pet(
	id int not null auto_increment,
    id_resp int,
    nome varchar(10),
    tipo varchar(10),
    raca varchar(10) not null,
    primary key(id),
    foreign key(id_resp) references responsavel(id)
);

create table responsavel(
 	id int not null auto_increment,
    nome varchar(30),
    cpf varchar(11) not null,
    telefone varchar(15),
    primary key(id)
);

select * from responsavel;
