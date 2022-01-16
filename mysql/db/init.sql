DROP SCHEMA IF EXISTS employee;
CREATE SCHEMA employee;
USE employee;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee
(
    id       INT         NOT NULL AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    action    INT         NOT NULL DEFAULT 0,
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
INSERT INTO employee (name, action) VALUES ("Alice", 0);
INSERT INTO employee (name, action) VALUES ("Bob", 1);
INSERT INTO employee (name, action) VALUES ("Jacob", 1);
INSERT INTO employee (name, action) VALUES ("Noah", 1);
INSERT INTO employee (name, action) VALUES ("Lucas", 2);
INSERT INTO employee (name, action) VALUES ("Sophia", 2);
INSERT INTO employee (name, action) VALUES ("Chloe", 1);
INSERT INTO employee (name, action) VALUES ("Abigail", 2);
INSERT INTO employee (name, action) VALUES ("Harry", 0);
INSERT INTO employee (name, action) VALUES ("Charlie", 2);