sudo aptitude update
sudo aptitude upgrade
sudo aptitude install -y postgresql=9.3.9 postgresql-contrib
sudo aptitude install -y python-psycopg2
#Creating 2 users and assiging permisiions
sudo -u postgres bash -c "psql -c \"CREATE USER farmdev WITH PASSWORD 'farmdevdev';\""
sudo -u postgres bash -c "psql -c \"CREATE USER farmops WITH PASSWORD 'farmops';\""
sudo -u postgres bash -c "psql -c \"ALTER USER farmops set default_transaction_read_only = on;\"" 
sudo -u postgres bash -c "psql -c \"GRANT SELECT ON ALL TABLES IN SCHEMA public TO farmops;\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE seeddev WITH owner farmdev;\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE seedops WITH owner farmops;\""
