INSERT INTO courtzapi_filertype
VALUES (null, "clerk")
INSERT INTO courtzapi_casestatus
VALUES (null, "open");
INSERT INTO courtzapi_casestatus
VALUES (null, "closed");
INSERT INTO courtzapi_filingtype
VALUES (null, "complaint");
INSERT INTO courtzapi_filingtype
VALUES (null, "order");
INSERT INTO courtzapi_partytype
VALUES (null, "plaintiff");
INSERT INTO courtzapi_partytype
VALUES (null, "defendant");
INSERT INTO courtzapi_docketparty
    ('docket_id', 'party_id', 'party_type_id')
VALUES 
    (6, 1, 1)

UPDATE courtzapi_filer
SET filer_type_id = 2
WHERE user_id = 2

UPDATE auth_user
SET is_staff = 1
WHERE id = 3

UPDATE courtzapi_filer
SET id = 5
WHERE id = 4

DELETE FROM courtzapi_docketparty
WHERE id = 3

UPDATE courtzapi_docket
SET case_num = "B-000001"
WHERE id = 4