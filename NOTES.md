# Database Notes

## First-time setup (run ONCE)
```
docker run --name warframe-db -e POSTGRES_PASSWORD=YOUR_PASSWORD -e POSTGRES_DB=warframe -p 5432:5432 -v warframe-data:/var/lib/postgresql/data -d postgres:16
```

## Every time after
1. Open Docker Desktop and wait for "Engine running"
2. Start the container: `docker start warframe-db`
3. Check it's running: `docker ps` (status should say "Up")
4. Connect: `docker exec -it warframe-db psql -U postgres -d warframe`  
5. Quit psql: `\q`

## Stop the container
`docker stop warframe-db` (data is kept in the warframe-data volume)

## psql tips
- SQL statements end with `;`
- psql commands start with `\` (`\q` quit, `\dt` list tables, `\?` help)
- Prompt `warframe-#` means psql is waiting for the rest of a statement