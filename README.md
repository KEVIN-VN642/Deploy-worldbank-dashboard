# Worldbank Dashboard 


### Table of Contents
1. [Introduction](#intro)
2. [Data](#data)
3. [Software Requirements](#software)
4. [How to run project locally](#run)
5. [Results and API](#results)

## 1. Introduction<a id = "intro"></a>:
This project I built a dashboard to visualize some argiculture and rural indicators in top 10 economies (United States, China, Japan, Germany, United Kingdom, India, France, Brazil, Italy and Canada)

## 2. Data <a id = "data"></a>:
The data used in this project got from worldbank website, four indicators are used:
- Arable land (% of land area)
- Forest area (sq.km)
- Rural population (% of total population)
- Rural population

## 3. Software requirements<a id ="software"></a>:
- Data processing packages: numpy, pandas
- Charts and web framework: plotly, Flask
- Database: SQLite and Sqlalchemy

## 4. How to run project<a id = "run"></a>:
- First run ETL_Pipeline.ipynb in data folder to clean data and save results in database
- Run worldbank.py script to visualize data

## 5. Results <a id="results"></a>:
View the the dashboard (this may run a bit slow due to using free service), visit this URL: https://wb-dashboard.azurewebsites.net/
### 5.1 Overview 1:
![Overview 1](https://github.com/KEVIN-VN642/Deploy-worldbank-dashboard/blob/master/static/Overview1.png)

### 5.2 Overview 2:
![Overview 2](https://github.com/KEVIN-VN642/Deploy-worldbank-dashboard/blob/master/static/Overview2.png)

