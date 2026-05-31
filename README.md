# Nairobi Neighborhood Population Density Map
## Overview
This project creates an interactive population density map of selected Nairobi neighborhoods using **Python**, **Pandas**, and **Folium**. The visualization displays neighborhoods as color-coded circle markers, where marker size represents population density and colors indicate neighborhood categories.

## Features
* Interactive web-based map centered on Nairobi
* Population density visualized through proportional marker sizes
* Category-based color coding:
  * **Commercial** – Red
  * **Business** – Blue
  * **Residential** – Green
  * **Informal Settlement** – Orange
* Informative popups with neighborhood details
* Custom map title and legend
* Exportable HTML output for easy sharing

## Technologies Used
* Python 3
* Pandas
* Folium

## Installation
Install the required dependencies:
```bash
pip install folium pandas
```

## Usage
Run the script:
```bash
python nairobi_population_map.py
```

After execution, an interactive HTML file will be generated:
```text
nairobi_population_map.html
```
Open the file in a web browser to explore the map.
## Dataset
The sample dataset includes:

| Neighborhood | Category            | Population Density (people/km²) |
| ------------ | ------------------- | ------------------------------- |
| Nairobi CBD  | Commercial          | 25,000                          |
| Westlands    | Business            | 12,000                          |
| Karen        | Residential         | 3,000                           |
| Eastleigh    | Commercial          | 30,000                          |
| Kibera       | Informal Settlement | 80,000                          |

## Output
The generated map provides:
* Interactive neighborhood markers
* Population density visualization
* Category-based color differentiation
* Custom legend and title for improved readability

## License
This project is available for educational and demonstration purposes.
