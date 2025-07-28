# LWA POC v1 2025-07-28

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("LWA POC")
st.write(
    "Start this journey of a thousand steps!"
)

st.set_page_config(layout="wide")

st.title("Interactive Map with Location Details on Hover")
st.write("Hover over the pins to see detailed information about each location.")

# Sample data for locations
data = {
    'name': ['Eiffel Tower', 'Statue of Liberty', 'Colosseum', 'Mount Everest Base Camp', 'Great Barrier Reef'],
    'latitude': [48.8584, 40.6892, 41.8902, 28.0062, -18.2871],
    'longitude': [2.2945, -74.0445, 12.4922, 86.8295, 147.699],
    'description': [
        'Iconic iron lattice tower on the Champ de Mars in Paris, France.',
        'Neoclassical sculpture on Liberty Island in New York Harbor, USA.',
        'Oval amphitheatre in the centre of the city of Rome, Italy.',
        'The starting point for Everest expeditions, located in Nepal.',
        'World\'s largest coral reef system, off the coast of Queensland, Australia.'
    ],
    'country': ['France', 'USA', 'Italy', 'Nepal', 'Australia']
}
df = pd.DataFrame(data)

# Center the map around a reasonable initial point (e.g., average lat/lon)
# You might want to adjust this based on your specific data
map_center = [df['latitude'].mean(), df['longitude'].mean()]

# Create a Folium map object
m = folium.Map(location=map_center, zoom_start=2, control_scale=True)

# Add markers for each location
for idx, row in df.iterrows():
    # Construct the tooltip text with detailed information
    tooltip_html = f"""
    <h4>{row['name']}</h4>
    <b>Country:</b> {row['country']}<br>
    <b>Description:</b> {row['description']}<br>
    <b>Coordinates:</b> ({row['latitude']:.2f}, {row['longitude']:.2f})
    """

    # Add a marker with the tooltip
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        tooltip=folium.Tooltip(tooltip_html, sticky=True), # 'sticky=True' makes it follow the mouse
        popup=folium.Popup(f"<b>{row['name']}</b><br>{row['description']}"), # Optional: popup on click
        icon=folium.Icon(color='red', icon='info-sign') # You can customize marker icons
    ).add_to(m)

# Display the map in Streamlit
st_data = st_folium(m, width=800, height=500)

st.subheader("Selected Location (on click):")
if st_data and st_data.get("last_object_clicked_popup"):
    st.info(f"You clicked on: {st_data['last_object_clicked_popup']}")
else:
    st.write("Click on a marker to see its details here.")

st.markdown("""
---
**Note:**
- **Hover** over a pin to see its `tooltip` (rich information).
- **Click** on a pin to see its `popup` and update the "Selected Location" text below the map.
- The `streamlit-folium` component provides a lot more customization options than `st.map()`.
""")
