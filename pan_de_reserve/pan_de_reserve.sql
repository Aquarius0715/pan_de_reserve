CREATE TABLE pan_de_reserve_bakeryitem (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            price REAL NOT NULL
);

CREATE TABLE pan_de_reserve_allergy (
                                          id INTEGER PRIMARY KEY,
                                          name TEXT NOT NULL
);

CREATE TABLE pan_de_reserve_bakeryitemallergy (
                                                    id INTEGER PRIMARY KEY,
                                                    bakery_item_id INTEGER,
                                                    allergy_id INTEGER,
                                                    FOREIGN KEY (bakery_item_id) REFERENCES pan_de_reserve_bakeryitems (id),
                                                    FOREIGN KEY (allergy_id) REFERENCES pan_de_reserve_allergies (id)
);

CREATE TABLE pan_de_reserve_reservation (
                                             id INTEGER PRIMARY KEY,
                                             recieve_time DATETIME NOT NULL,
                                             customer_name TEXT NOT NULL,
                                             customer_phone_number TEXT NOT NULL,
                                             is_recieved BOOLEAN NOT NULL
);

CREATE TABLE pan_de_reserve_reservationdetail (
                                                   id INTEGER PRIMARY KEY,
                                                   reserve_id INTEGER,
                                                   bakery_item_id INTEGER,
                                                   FOREIGN KEY (reserve_id) REFERENCES pan_de_reserve_reservations (id),
                                                   FOREIGN KEY (bakery_item_id) REFERENCES pan_de_reserve_bakeryitems (id)
);

