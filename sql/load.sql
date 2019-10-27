COPY region FROM '/csv/region.csv' DELIMITER ',' CSV;

COPY nation FROM '/csv/nation.csv' DELIMITER ',' CSV;

COPY customer FROM '/csv/customer.csv' DELIMITER ',' CSV;

COPY part FROM '/csv/part.csv' DELIMITER ',' CSV;

COPY orders FROM '/csv/orders.csv' DELIMITER ',' CSV;

COPY supplier FROM '/csv/supplier.csv' DELIMITER ',' CSV;

COPY partsupp FROM '/csv/partsupp.csv' DELIMITER ',' CSV;

COPY lineitem FROM '/csv/lineitem.csv' DELIMITER ',' CSV;
