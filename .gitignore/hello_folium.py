import folium

# Center map on downtown mpls
#map_mn = folium.Map(location=[45, -93.2])

# Add a marker for MCTC at designated coordinates
# folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)
map_us = folium.Map(location=[40, -120], zoom_start=3)
map_us.save('map.html')