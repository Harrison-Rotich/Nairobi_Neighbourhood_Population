import pandas as pd
import folium
from folium.plugins import MarkerCluster

data = {
    'Name': ['Nairobi CBD', 'Westlands', 'Karen', 'Eastleigh', 'Kibera'],
    'Latitude': [-1.2864, -1.2676, -1.3192, -1.2755, -1.3133],
    'Longitude': [36.8172, 36.8062, 36.7073, 36.8594, 36.7833],
    'Population_Density': [25000, 12000, 3000, 30000, 80000],
    'Category': ['Commercial', 'Business', 'Residential',
                 'Commercial', 'Informal Settlement']
}

df = pd.DataFrame(data)

# Color by category
color_map = {
    'Commercial': 'red',
    'Business': 'blue',
    'Residential': 'green',
    'Informal Settlement': 'orange'
}

# Create map with better styling
m = folium.Map(
    location=[-1.2921, 36.8219],
    zoom_start=12,
    tiles='CartoDB positron'  # Cleaner, professional basemap
)

# Add title
title_html = '''
<h3 align="center" style="font-size:16px">
<b>Nairobi Neighborhood Population Density Map</b></h3>
'''
m.get_root().html.add_child(folium.Element(title_html))

# Add points with color + rich popups
for _, row in df.iterrows():
    color = color_map.get(row['Category'], 'gray')
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Population_Density'] / 5000,  # Size = density
        popup=folium.Popup(
            f"""
            <b>{row['Name']}</b><br>
            Category: {row['Category']}<br>
            Population Density: {row['Population_Density']:,} people/km²
            """,
            max_width=200
        ),
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7
    ).add_to(m)

# Add legend manually
legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px;
     background-color: white; padding: 10px;
     border: 2px solid grey; z-index: 9999; font-size: 12px;">
<b>Category</b><br>
<i style="color:red">●</i> Commercial<br>
<i style="color:blue">●</i> Business<br>
<i style="color:green">●</i> Residential<br>
<i style="color:orange">●</i> Informal Settlement
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

m.save('nairobi_population_map.html')
print("Professional map created!")
