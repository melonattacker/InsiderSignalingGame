DROP SCHEMA IF EXISTS employee;
CREATE SCHEMA employee;
USE employee;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee
(
    id       INT         NOT NULL AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    action VARCHAR(60) NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARACTER SET=utf8mb4;

-- INSERT INTO employee (name, action) VALUES ("宮下 大樹", 0);
-- INSERT INTO employee (name, action) VALUES ("原田 栄", 1);
-- INSERT INTO employee (name, action) VALUES ("石田 颯人", 1);
-- INSERT INTO employee (name, action) VALUES ("原田 栄", 1);
-- INSERT INTO employee (name, action) VALUES ("秋保 修", 2);
-- INSERT INTO employee (name, action) VALUES ("仏淵 桜", 2);
-- INSERT INTO employee (name, action) VALUES ("鹿股 昴", 1);
-- INSERT INTO employee (name, action) VALUES ("柴田 早江子", 2);
-- INSERT INTO employee (name, action) VALUES ("佐野 飛成", 0);
-- INSERT INTO employee (name, action) VALUES ("東福間 心花", 2);
INSERT INTO employee (name, action) VALUES ("Alice", "Revoke");
INSERT INTO employee (name, action) VALUES ("Bob", "Warn");
INSERT INTO employee (name, action) VALUES ("Jacob", "Warn");
INSERT INTO employee (name, action) VALUES ("Noah", "Warn");
INSERT INTO employee (name, action) VALUES ("Lucas", "Keep");
INSERT INTO employee (name, action) VALUES ("Sophia", "Keep");
INSERT INTO employee (name, action) VALUES ("Chloe", "Warn");
INSERT INTO employee (name, action) VALUES ("Abigail", "Keep");
INSERT INTO employee (name, action) VALUES ("Harry", "Revoke");
INSERT INTO employee (name, action) VALUES ("Charlie", "Keep");