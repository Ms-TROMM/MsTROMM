DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS recommendation;
DROP TABLE IF EXISTS control;
DROP TABLE IF EXISTS clothes;
DROP TABLE IF EXISTS scent;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS user_preference;
DROP TABLE IF EXISTS clothes_combination;
DROP TABLE IF EXISTS styler_alert; 

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email VARCHAR(30) UNIQUE NOT NULL, 
  username VARCHAR(30) UNIQUE NOT NULL,
  password VARCHAR(30) NOT NULL, 
  sex INTEGER NOT NULL, 
  birth_year SMALLINT NOT NULL, 
  push INTEGER DEFAULT 0 -- if accepted then 1, otherwise set to 0
);

CREATE TABLE user_preference (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL,
  scent_id INTEGER NOT NULL,
  fashion_style VARCHAR(30) NULL, 
  color INTEGER NULL, -- convert from integer to hex value of the color 
  FOREIGN KEY (user_id) REFERENCES user (id), 
  FOREIGN KEY (scent_id) REFERENCES scent (id)
);

CREATE TABLE recommendation (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  user_id INTEGER NOT NULL,
  recommendation_type_id INTEGER NOT NULL, 
  title VARCHAR(100) NOT NULL,
  description VARCHAR(255) NULL, 
  schedule_id INTEGER NULL,
  clothes_combination_id INTEGER NULL,
  scent_id INTEGER NULL,
  control_id INTEGER NULL,
  is_useful SMALLINT NULL, -- useful if 1, otherwise 0 
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (schedule_id) REFERENCES schedule (id), 
  FOREIGN KEY (clothes_combination_id) REFERENCES clothes_combination (id),
  FOREIGN KEY (scent_id) REFERENCES scent (id),
  FOREIGN KEY (control_id) REFERENCES control (id),
  FOREIGN KEY (recommendation_type_id) REFERENCES recommendation_type (type_id)
);

-- not user specific 
CREATE TABLE control (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  steam INTEGER NULL DEFAULT 0, 
  refresh INTEGER NULL DEFAULT 0, 
  dehumification INTEGER NULL DEFAULT 0, 
  indoor_dehumification INTEGER DEFAULT 0 
); 

-- not user specific
CREATE TABLE scent (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(30) NOT NULL 
);

-- combinations of top, down, outwear or onepiece
CREATE TABLE clothes_combination (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL,
  top_clothes_id INTEGER NULL, 
  down_clothes_id INTEGER NULL,  
  onepiece_clothes_id INTEGER NULL, 
  outwear_clothes_id INTEGER NULL,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (top_clothes_id) REFERENCES clothes (id),
  FOREIGN KEY (down_clothes_id) REFERENCES clothes (id),
  FOREIGN KEY (onepiece_clothes_id) REFERENCES clothes (id),
  FOREIGN KEY (outwear_clothes_id) REFERENCES clothes (id)
); 

-- does this need to be saved ? 
CREATE TABLE schedule (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL,
  description VARCHAR(255) NOT NULL, 
  datetime TIMESTAMP NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
); 

-- 새 옷 등록하기 화면 참고 
CREATE TABLE clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    type_id INTEGER NOT NULL,  
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stylered_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    need_styler SMALLINT NOT NULL DEFAULT 0, 
    is_inside_styler NOT NULL DEFAULT 0, 
    user_id INTEGER NOT NULL,
    name VARCHAR(30) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (type_id) REFERENCES clothes_type (type_id) 
);

-- alerts for styler state ex. water is full ! 
CREATE TABLE styler_alert (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES user (id)
);

-- enum for type of clothes 
CREATE TABLE clothes_type (
  type_id INTEGER PRIMARY KEY NOT NULL, 
  type VARCHAR(255) NOT NULL
);

-- enum for type of recommendations 
CREATE TABLE recommendation_type (
  type_id INTEGER PRIMARY KEY NOT NULL, 
  type VARCHAR(255) NOT NULL
);

INSERT INTO clothes_type(type_id, type) VALUES (0, 'top'); 
INSERT INTO clothes_type(type_id, type) VALUES (1, 'down'); 
INSERT INTO clothes_type(type_id, type) VALUES (2, 'outwear'); 
INSERT INTO clothes_type(type_id, type) VALUES (3, 'onepiece'); 

INSERT INTO recommendation_type(type_id, type) VALUES (0, 'today'); 
INSERT INTO recommendation_type(type_id, type) VALUES (1, 'control'); 
INSERT INTO recommendation_type(type_id, type) VALUES (2, 'scent'); 
INSERT INTO recommendation_type(type_id, type) VALUES (3, 'clothes'); 
