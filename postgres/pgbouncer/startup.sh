docker run --name some-pgbouncer   -p 6432:6432 \
  -v ./pgbouncer.ini:/etc/pgbouncer/pgbouncer.ini:ro \
  -v ./userlist.txt:/etc/pgbouncer/userlist.txt:ro \
  --user 70 \
  --add-host=host.docker.internal:host-gateway\
  dhi.io/pgbouncer:1-debian13-dev


docker run --name postgres-container -p 5430:5432\
     --add-host=host.docker.internal:host-gateway \
   -e POSTGRES_PASSWORD=mysecretpassword \
   -e POSTGRES_DB=mydb \
   -d postgres:alpine3.22