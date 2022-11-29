create database twitter;
use twitter;

create table user(
	id int not null auto_increment,
    nickname varchar(64),
    email varchar(64),
    password varchar(64),
    primary key(id)
);

create table user_follows(
	user_follows_id int,
    user_followed_id int,
    primary key(user_follows_id, user_followed_id),
    foreign key (user_follows_id) references user(id),
    foreign key (user_followed_id) references user(id)
);

create table tweet(
	id int not null auto_increment,
    content text,
    retweet tinyint(1),
    owner_id int,
    parent int
);
