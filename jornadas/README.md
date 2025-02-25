# 📂 League Results DataFrames

This directory contains the DataFrame files with the results of each matchday in the league, stored weekly in text files (`.txt`). These files will later be used for insertion into a database and analyzed with `pandas`.

## 📌 File Structure
Each file represents a matchday and follows a consistent format for easy processing. The file name follows the pattern:


## 📝 Data Format
Each `.txt` file contains the following columns separated by a delimiter:

- Shots                       
- Shots on target                          
- Assists                                  
- Successful dribbles
- Failed dribbles
- Goals
- Goals from inside the box
- Goals from outside the box
- Goals with the left foot
- Goals with the right foot
- Penalty goals
- Header goals
- Set-piece goals
- Own goals
- Minutes played
- Matches played
- ETC ...

## 📥 Data Insertion Process

1. **Loading the files**: The `.txt` files will be read using `pandas`.
2. **Data normalization**: The `normalizer.py` script will be used to clean and transform the data.
3. **Table creation**: The `Create-tables.sql` script will be used to generate the tables in SQL Server.
4. **Insertion into the database**: The normalized data will be loaded into the database.

## 📊 Data Analysis with Pandas
Once the data is in the database, `pandas` will be used to:

- Generate descriptive statistics.
- Visualize trends and patterns in the results.
- Compare the performance of teams throughout the season.
- Apply prediction models based on the collected data.



**⚠️ Note:** Follow the instructions in the `README.md` file located in the main folder