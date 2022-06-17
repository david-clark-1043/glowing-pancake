UPDATE courtzapi_filertype
SET filer_type = "party"
WHERE id = 3;

DELETE FROM courtzapi_filertype
WHERE id = 1;


INSERT INTO courtzapi_filertype
VALUES (null, "clerk");
INSERT INTO courtzapi_filertype
VALUES (null, "judge");
INSERT INTO courtzapi_filertype
VALUES (null, "pro se");
INSERT INTO courtzapi_filertype
VALUES (null, "filer");

INSERT INTO courtzapi_casestatus
VALUES (null, "open");
INSERT INTO courtzapi_casestatus
VALUES (null, "closed");

INSERT INTO courtzapi_filingtype
VALUES (null, "complaint");
INSERT INTO courtzapi_filingtype
VALUES (null, "reply");
INSERT INTO courtzapi_filingtype
VALUES (null, "motion");
INSERT INTO courtzapi_filingtype
VALUES (null, "order");

INSERT INTO courtzapi_partytype
VALUES (null, "clerk");
INSERT INTO courtzapi_partytype
VALUES (null, "judge");
INSERT INTO courtzapi_partytype
VALUES (null, "plaintiff");
INSERT INTO courtzapi_partytype
VALUES (null, "defendant");

INSERT INTO courtzapi_firm
VALUES (null, "Dewey, Cheatam, & Howe");
INSERT INTO courtzapi_firm
VALUES (null, "Hamlin, Hamlin, McGill");