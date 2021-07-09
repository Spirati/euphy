CREATE TABLE IF NOT EXISTS sentences (
  id int NOT NULL AUTO_INCREMENT,
  content varchar(255) NOT NULL unique,
  PRIMARY KEY (ID)
);
CREATE TABLE IF NOT EXISTS pronouns (
  id int NOT NULL AUTO_INCREMENT,
  nom varchar(25) unique,
  obj varchar(25),
  poss varchar(25),
  posspro varchar(25),
  ref varchar(25),
  plural bool default false,
  PRIMARY KEY (ID)
);
REPLACE INTO pronouns (nom, obj, poss, posspro, ref, plural) values
('they', 'them', 'their', 'theirs', 'themselves', true),
('he', 'him', 'his', 'his', 'himself', false),
('she', 'her', 'her', 'hers', 'herself', false),
('it', 'it', 'its', 'its', 'itself', false)
;
REPLACE INTO sentences (content) values
('This is a test sentence for {name}! {name} is a person, and I like {obj} a lot. Etc., etc.')
;