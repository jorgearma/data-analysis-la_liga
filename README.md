# Project: Web Scraping and Data Analysis - La Liga

This project performs web scraping of La Liga data and stores it in a SQL Server database for further analysis. It is designed to run on a Linux environment, leveraging Linux-compatible tools and libraries for scraping, data processing, and database interaction.

## 1. Clone the repository

To get started, clone the following repository:

```bash
    git clone https://github.com/jorgearma/data-analysis-la_liga.git
```

Access the project folder:

```bash
    cd data-analysis-la_liga/Web_scraping-SQL
```

## 2. Create the container and databasegit

To run SQL Server in a Docker container, use the following command:

```bash
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=yourPASSWORD' \
-p 1433:1433 \
-v /your/directory/data-analysis-la_liga/jornada-SQL:/var/opt/mssql/sql_files \
--name BD-name \
-d mcr.microsoft.com/mssql/server:2019-latest
```

**Note:** The path `/your/directory/BeyondStats-LaLiga/jornada` must match the location where the project was downloaded.

## 3. Modify the target directory

Inside the script, you need to update the `directory` variable with the path where the Docker container is mounted to host the SQL Server database. Edit the following lines in the corresponding scripts:

- `indice-posicion.py`
- `Scraping_Stats_LaLiga.py`

Change this line:

```python
    directory = '/your/directory/data-analysis-la_liga/jornadas/jornada25'
```

To the appropriate path within the Docker container.

## 4. Run the scripts

Run the scripts to perform web scraping and store the data in the database:

```bash
    python indice-posicion.py
    python Scraping_Stats_LaLiga.py
```

## 5. Normalize player names

After running the previous scripts, it is necessary to normalize player names using the `Text-Normalizer.py` script. Before executing it, make sure to modify the following path inside the script to match the correct directory:

```python
    directorio_entrada = '/your/directory/data-analysis-la_liga/jornadas/jornada25'
```

Then, run:

```bash
    python Text-Normalizer.py
```

## 6. Configure Docker and SQL Server

Ensure that the Docker container with SQL Server is running and accessible. You can check running containers with:

```bash
    docker ps
```

If necessary, start the container with:

```bash
    docker start <container_name>
```

Then, enter the database and create it with the following command:

```bash
    sqlcmd -S localhost -U sa -P yourPASSWORD    
    CREATE DATABASE BeyondStats;
    GO
```

Next, run the SQL script to add the data:

```bash
    sqlcmd -S localhost -U sa -P yourPASSWORD -i Create-tables.sql
```

##

\## Créditos



The original code was developed by Sergio Prieto García. You can find the original repository [here]\([https://github.com/SergioPrietoGarcia/BeyondStats-LaLiga.git](https://github.com/SergioPrietoGarcia/BeyondStats-LaLiga.git)).
