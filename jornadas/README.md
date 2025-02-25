# 📂 League Results DataFrames

This directory contains the DataFrame files with the results of each matchday in the league, stored weekly in text files (`.txt`). These files will later be used for insertion into a database and analyzed with `pandas`.

## 📌 File Structure
Each file represents a matchday and follows a consistent format for easy processing. The file name follows the pattern:


## 📝 Data Format
Each `.txt` file contains the following columns separated by a delimiter:

ID
Jugador
Equipo
Posicion
Disparos
Disparos a puerta
Asistencias
Regates con éxito
Regates fallidos
Goles
Goles desde dentro del área
Goles desde fuera del área
Goles con la pierna izquierda
Goles con la pierna derecha
Goles de penalti
Goles de cabeza
Goles a balón parado
Goles en propia puerta
ID
Jugador
Minutos jugados
Partidos jugados
% Partidos jugados
Partidos completos
% Partidos completos
Partidos como titular
% Partidos como titular
Partidos sustituido
% Partidos sustituido
Tarjetas amarillas
Tarjetas rojas
Segundas amarillas
Goles
Penaltis recibidos
Goles en propia puerta
Goles en contra
Bloqueos
Intercepciones
Recuperaciones
Despejes
Entradas con éxito
Entradas fallidas
Jugadas como último hombre
Duelos con éxito
Duelos fallidos
Duelos aéreos con éxito
Duelos aéreos fallidos
Tarjetas amarillas
Tarjetas rojas
Segundas amarillas
Fueras de juego
Faltas recibidas
Faltas cometidas
Penaltis recibidos
Penaltis en contra
Manos
Faltas por tarjeta


## 📊 Data Analysis with Pandas
Once the data is in the database, `pandas` will be used to:

- Generate descriptive statistics.
- Visualize trends and patterns in the results.
- Compare the performance of teams throughout the season.
- Apply prediction models based on the collected data.



**⚠️ Note:** Follow the instructions in the `README.md` file located in the main folder