# Docker


Backup and restore postgres DB
```bash
# copy dump into container
docker cp local/path/to/db.dump CONTAINER_ID:/db.dump

# shell into container
docker exec -it CONTAINER_ID bash

# restore it from within
pg_restore -U postgres -d DB_NAME --no-owner -1 /db.dump
```
