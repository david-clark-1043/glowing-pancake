INSERT INTO courtzapi_filertype
VALUES (null, "clerk")
INSERT INTO courtzapi_casestatus
VALUES (null, "open");
INSERT INTO courtzapi_casestatus
VALUES (null, "closed");
INSERT INTO courtzapi_filingtype
VALUES (null, "complaint");
INSERT INTO courtzapi_partytype
VALUES (null, "plaintiff");
INSERT INTO courtzapi_partytype
VALUES (null, "defendant");
INSERT INTO courtzapi_docketparty
    ('docket_id', 'party_id', 'party_type_id')
VALUES 
    (6, 1, 1)