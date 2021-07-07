CREATE TABLE IF NOT EXISTS sentences (
  id int NOT NULL,
  content varchar(280) NOT NULL,
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
INSERT INTO pronouns (nom, obj, poss, posspro, ref, plural) values
('they', 'them', 'their', 'theirs', 'themselves', true),
('he', 'him', 'his', 'his', 'himself', false),
('she', 'her', 'her', 'hers', 'herself', false),
('it', 'it', 'its', 'its', 'itself', false)
;