from flask import Flask, render_template, jsonify
import folium
from folium.features import GeoJson
from folium.plugins import MarkerCluster, Fullscreen, FeatureGroupSubGroup
from india_states import india_states, famous_monuments
import os
import logging
import requests
import json

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

@app.route('/')
def index():
    logger.debug("Rendering index page")
    
    # Create a map centered on India with a bright blue and white theme
    india_map = folium.Map(
        location=[22.9734, 78.6569], 
        zoom_start=5,
        tiles="CartoDB Positron",  # Bright white base map
        control_scale=True,
        zoom_control=False,  # We'll add custom zoom controls at the bottom
    )
    
    # Add a texture overlay to the map
    texture_script = """
    <script>
    (function() {
        // Add a subtle texture to the map tiles
        var mapPane = document.querySelector('.leaflet-map-pane');
        if (mapPane) {
            var style = document.createElement('style');
            style.textContent = `
                .leaflet-tile-pane::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAAUVBMVEWFhYWDg4N3d3dtbW17e3t1dXWBgYGHh4d5eXlzc3OLi4ubm5uVlZWPj4+NjY19fX2JiYl/f39ra2uRkZGZmZlpaWmXl5dvb29xcXGTk5NnZ2c8TV1mAAAAG3RSTlNAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEAvEOwtAAAFVklEQVR4XpWWB67c2BUFb3g557T/hRo9/WUMZHlgr4Bg8Z4qQgQJlHI4A8SzFVrapvmTF9O7dmYRFZ60YiBhJRCgh1FYhiLAmdvX0CzTOpNE77ME0Zty/nWWzchDtiqrmQDeuv3powQ5ta2eN0FY0InkqDD73lT9c9lEzwUNqgFHs9VQce3TVClFCQrSTfOiYkVJQBmpbq2L6iZavPnAPcoU0dSw0SUTqz/GtrGuXfbyyBniKykOWQWGqwwMA7QiYAxi+IlPdqo+hYHnUt5ZPfnsHJyNiDtnpJyayNBkF6cWoYGAMY92U2hXHF/C1M8uP/ZtYdiuj26UdAdQQSXQErwSOMzt/XWRWAz5GuSBIkwG1H3FabJ2OsUOUhGC6tK4EMtJO0ttC6IBD3kM0ve0tJwMdSfjZo+EEISaeTr9P3wYrGjXqyC1krcKdhMpxEnt5JetoulscpyzhXN5FRpuPHvbeQaKxFAEB6EN+cYN6xD7RYGpXpNndMmZgM5Dcs3YSNFDHUo2LGfZuukSWyUYirJAdYbF3MfqEKmjM+I2EfhA94iG3L7uKrR+GdWD73ydlIB+6hgref1QTlmgmbM3/LeX5GI1Ux1RWpgxpLuZ2+I+IjzZ8wqE4nilvQdkUdfhzI5QDWy+kw5Wgg2pGpeEVeCCA7b85BO3F9DzxB3cdqvBzWcmzbyMiqhzuYqtHRVG2y4x+KOlnyqla8AoWWpuBoYRxzXrfKuILl6SfiWCbjxoZJUaCBj1CjH7GIaDbc9kqBY3W/Rgjda1iqQcOJu2WW+76pZC9QG7M00dffe9hNnseupFL53r8F7YHSwJWUKP2q+k7RdsxyOB11n0xtOvnW4irMMFNV4H0uqwS5ExsmP9AxbDTc9JwgneAT5vTiUSm1E7BSflSt3bfa1tv8Di3R8n3Af7MNWzs49hmauE2wP+ttrq+AsWpFG2awvsuOqbipWHgtuvuaAE+A1Z/7gC9hesnr+7wqCwG8c5yAg3AL1fm8T9AZtp/bbJGwl1pNrE7RuOX7PeMRUERVaPpEs+yqeoSmuOlokqw49pgomjLeh7icHNlG19yjs6XXOMedYm5xH2YxpV2tc0Ro2jJfxC50ApuxGob7lMsxfTbeUv07TyYxpeLucEH1gNd4IKH2LAg5TdVhlCafZvpskfncCfx8pOhJzd76bJWeYFnFciwcYfubRc12Ip/ppIhA1/mSZ/RxjFDrJC5xifFjJpY2Xl5zXdguFqYyTR1zSp1Y9p+tktDYYSNflcxI0iyO4TPBdlRcpeqjK/piF5bklq77VSEaA+z8qmJTFzIWiitbnzR794USKBUaT0NTEsVjZqLaFVqJoPN9ODG70IPbfBHKK+/q/AWR0tJzYHRULOa4MP+W/HfGadZUbfw177G7j/OGbIs8TahLyynl4X4RinF793Oz+BU0saXtUHrVBFT/DnA3ctNPoGbs4hRIjTok8i+algT1lTHi4SxFvONKNrgQFAq2/gFnWMXgwffgYMJpiKYkmW3tTg3ZQ9Jq+f8XN+A5eeUKHWvJWJ2sgJ1Sop+wwhqFVijqWaJhwtD8MNlSBeWNNWTa5Z5kPZw5+LbVT99wqTdx29lMUH4OIG/D86ruKEauBjvH5xy6um/Sfj7ei6UUVk4AIl3MyD4MSSTOFgSwsH/QJWaQ5as7ZcmgBZkzjjU1UrQ74ci1gWBCSGHtuV1H2mhSnO3Wp/3fEV5a+4wz//6qy8JxjZsmxxy5+4w9CDNJY09T072iKG0EnOS0arEYgXqYnXcYHwjTtUNAcMelOd4xpkoqiTYICWFq0JSiPfPDQdnt+4/wuqcXY47QILbgAAAABJRU5ErkJggg==');
                    opacity: 0.05;
                    pointer-events: none;
                    z-index: 1000;
                }
            `;
            document.head.appendChild(style);
        }
    })();
    </script>
    """
    india_map.get_root().html.add_child(folium.Element(texture_script))
    
    # Add fullscreen control
    Fullscreen().add_to(india_map)
    
    # Add GeoJSON outline for India to highlight the country borders
    india_geojson_url = "https://raw.githubusercontent.com/datameet/maps/master/Country/india-composite.geojson"
    try:
        # Fetch India GeoJSON data
        response = requests.get(india_geojson_url)
        india_geojson = json.loads(response.text)
        
        # Add GeoJSON layer with styling to highlight India's borders with bright blue
        GeoJson(
            india_geojson,
            name="India Outline",
            style_function=lambda x: {
                "fillColor": "#2196F3",  # Bright blue
                "color": "#0D47A1",      # Darker blue for border
                "weight": 3,
                "fillOpacity": 0.2,
                "opacity": 0.8,
                "dashArray": "",
                "lineCap": "round",
                "lineJoin": "round"
            }
        ).add_to(india_map)
    except Exception as e:
        logger.error(f"Error loading GeoJSON data: {e}")
    
    # Add regions using individual state data
    try:
        # Create a feature collection for states
        states_features = []
        
        # Define a style function for hover effects
        def state_style(feature):
            return {
                "fillColor": "#42A5F5",    # Light blue
                "color": "#1565C0",        # Medium blue for borders
                "weight": 2.5,             # Slightly thicker
                "opacity": 0.8,            # Slightly transparent
                "fillOpacity": 0.15,
                "dashArray": "",           # Solid line
                "lineCap": "round",        # Rounded corners
                "lineJoin": "round",       # Rounded joins
                "smoothFactor": 2          # Smooth borders
            }
        
        # Add individual state boundaries
        for state in india_states:
            # You could fetch individual state GeoJSON here if available
            # For now, we'll rely on the country outline and the markers
            pass
            
    except Exception as e:
        logger.error(f"Error creating state boundaries: {e}")
    
    # Create a marker cluster group for better organization
    marker_cluster = MarkerCluster(
        name="States & Territories",
        overlay=True,
        control=True,
        icon_create_function="""
        function(cluster) {
            return L.divIcon({
                html: '<div style="background-color: rgba(33, 150, 243, 0.8); color: white; border-radius: 50%; width: 30px; height: 30px; line-height: 30px; text-align: center; border: 2px solid white; box-shadow: 0 0 5px rgba(0,0,0,0.3);">' + cluster.getChildCount() + '</div>',
                className: 'marker-cluster',
                iconSize: L.point(30, 30)
            });
        }
        """
    )
    
    # Create subgroups for the main categories
    states_group = FeatureGroupSubGroup(marker_cluster, name="States")
    states_group.add_to(india_map)
    
    union_territories_group = FeatureGroupSubGroup(marker_cluster, name="Union Territories")
    union_territories_group.add_to(india_map)
    
    monuments_group = FeatureGroupSubGroup(marker_cluster, name="Monuments")
    monuments_group.add_to(india_map)
    
    # Add markers for each state with improved visuals
    for state in india_states:
        # Create HTML for popup with image and information with improved styling
        popup_html = f"""
        <div style="width: 280px; font-family: 'Segoe UI', Roboto, Arial, sans-serif;">
            <h4 style="text-align: center; margin-bottom: 10px; color: #1565C0; border-bottom: 2px solid #2196F3; padding-bottom: 8px;">{state['name']}</h4>
            <div style="text-align: center;">
                <img src="{state['image_url']}" style="width: 100%; height: auto; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
            </div>
            <p style="background-color: rgba(33, 150, 243, 0.1); padding: 10px; border-radius: 5px; border-left: 3px solid #2196F3;">
                <strong style="color: #1565C0;">Famous For:</strong> {state['famous_for']}
            </p>
            
            {f'<p style="font-size: 13px; color: #555; text-align: center;"><i class="fas fa-university me-1"></i> Capital: {state.get("capital", "")}</p>' if state.get('capital') else ''}
            
            {f'<div style="margin-top: 5px;"><strong style="color: #1565C0; font-size: 13px;"><i class="fas fa-map-marker-alt me-1"></i> Type:</strong> <span style="font-size: 13px;">{state.get("type", "State").replace("_", " ").title()}</span></div>' if state.get('type') else ''}
        </div>
        """
        
        # Determine if this is a state or union territory and set appropriate icon
        state_type = state.get('type', 'state')
        marker_color = "#1976D2"  # Default blue for states
        pulse_duration = "1.5s"
        icon_size = 12
        
        if state_type == "union_territory":
            marker_color = "#9C27B0"  # Purple for union territories
            pulse_duration = "2s"
            icon_size = 10
        
        # Different animation based on state type
        animation_style = """
            @keyframes pulse-state {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.3); opacity: 0.8; }
                100% { transform: scale(1); opacity: 1; }
            }
            @keyframes pulse-ut {
                0% { transform: scale(1) rotate(0deg); opacity: 1; }
                50% { transform: scale(1.2) rotate(180deg); opacity: 0.8; }
                100% { transform: scale(1) rotate(360deg); opacity: 1; }
            }
        """
        
        animation_name = "pulse-state" if state_type != "union_territory" else "pulse-ut"
        
        # Custom icon HTML for a more attractive marker with different styling based on type
        icon_html = f"""
        <div style="background-color: {marker_color}; color: white; border-radius: 50%; width: {icon_size}px; height: {icon_size}px; 
                    box-shadow: 0 0 0 3px white, 0 0 5px rgba(0,0,0,0.5);
                    animation: {animation_name} {pulse_duration} infinite;"></div>
        <style>
            {animation_style}
        </style>
        """
        
        # Create custom icon with pulsing effect based on state type
        custom_icon = folium.DivIcon(
            html=icon_html,
            icon_size=(20, 20),
            icon_anchor=(6, 6),
            class_name=f"custom-icon-{state_type}"
        )
        
        # Add marker with enhanced popup and custom icon
        marker = folium.Marker(
            location=[state['latitude'], state['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=f"<strong>{state['name']}</strong>",
            icon=custom_icon
        )
        
        # Add to appropriate subgroup based on state type
        if state_type == "union_territory":
            marker.add_to(union_territories_group)
        else:
            marker.add_to(states_group)
            
        
    
    # Add monument markers
    for monument in famous_monuments:
        popup_html = f"""
        <div style="width: 280px; font-family: 'Segoe UI', Roboto, Arial, sans-serif;">
            <h4 style="text-align: center; margin-bottom: 10px; color: #2E7D32; border-bottom: 2px solid #4CAF50; padding-bottom: 8px;">{monument['name']}</h4>
            <div style="text-align: center;">
                <img src="{monument['image_url']}" style="width: 100%; height: auto; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
            </div>
            <p style="background-color: rgba(76, 175, 80, 0.1); padding: 10px; border-radius: 5px; border-left: 3px solid #4CAF50;">
                {monument['details']}
            </p>
            <p style="font-size: 13px; color: #555; text-align: center;">
                <i class="fas fa-map-marker-alt me-1"></i> {monument['state']}
            </p>
            <p style="text-align: center;">
                <a href="{monument['google_maps']}" target="_blank" style="color: #2E7D32; text-decoration: none;">
                    <i class="fas fa-map me-1"></i> View on Google Maps
                </a>
            </p>
        </div>
        """
        
        # Custom icon for monuments
        monument_icon = folium.DivIcon(
            html=f"""
            <div style="background-color: #4CAF50; color: white; border-radius: 50%; width: 14px; height: 14px; 
                    box-shadow: 0 0 0 3px white, 0 0 5px rgba(0,0,0,0.5);
                    animation: pulse-monument 2s infinite;">
            </div>
            <style>
                @keyframes pulse-monument {{
                    0% {{ transform: scale(1); opacity: 1; }}
                    50% {{ transform: scale(1.3); opacity: 0.8; }}
                    100% {{ transform: scale(1); opacity: 1; }}
                }}
            </style>
            """,
            icon_size=(20, 20),
            icon_anchor=(7, 7),
            class_name="monument-icon"
        )
        
        marker = folium.Marker(
            location=[monument['latitude'], monument['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=f"<strong>{monument['name']}</strong>",
            icon=monument_icon
        )
        marker.add_to(monuments_group)

    # Add the marker cluster to the map
    marker_cluster.add_to(india_map)
    
    # Apply smooth zoom effect and add enhanced custom zoom controls at the bottom
    custom_zoom_script = """
    <script>
        // Apply smooth zoom animation
        var map = document.querySelector('.leaflet-map-pane');
        if (map) {
            map._leaflet_map.options.zoomAnimation = true;
            map._leaflet_map.options.markerZoomAnimation = true;
            
            // Create custom zoom controls at the bottom
            setTimeout(function() {
                var mapContainer = document.querySelector('.leaflet-container');
                if (mapContainer) {
                    // Create stylesheet for animations
                    var style = document.createElement('style');
                    style.textContent = `
                        @keyframes zoom-button-pulse {
                            0% { transform: scale(1); box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
                            50% { transform: scale(1.05); box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
                            100% { transform: scale(1); box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
                        }
                        @keyframes button-click {
                            0% { transform: scale(1); }
                            50% { transform: scale(0.9); }
                            100% { transform: scale(1); }
                        }
                        .zoom-btn:hover {
                            animation: zoom-button-pulse 1s infinite;
                        }
                        .zoom-btn:active {
                            animation: button-click 0.3s;
                        }
                    `;
                    document.head.appendChild(style);
                    
                    // Create container for zoom controls
                    var zoomContainer = document.createElement('div');
                    zoomContainer.className = 'custom-zoom-controls';
                    zoomContainer.style.cssText = 'position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%); z-index: 1000; display: flex; gap: 20px; background-color: rgba(255, 255, 255, 0.98); border-radius: 15px; box-shadow: 0 6px 16px rgba(0,0,0,0.2); padding: 12px 20px; backdrop-filter: blur(8px);';
                    
                    // Zoom out button
                    var zoomOutBtn = document.createElement('button');
                    zoomOutBtn.className = 'zoom-btn';
                    zoomOutBtn.innerHTML = '<div style="background: white; width: 16px; height: 4px; border-radius: 2px;"></div>';
                    zoomOutBtn.style.cssText = 'background-color: #2196F3; color: white; border: none; border-radius: 50%; width: 50px; height: 50px; margin: 5px 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.25); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);';
                    zoomOutBtn.onmouseover = function() { this.style.backgroundColor = '#1976D2'; };
                    zoomOutBtn.onmouseout = function() { this.style.backgroundColor = '#2196F3'; };
                    zoomOutBtn.onclick = function() { 
                        map._leaflet_map.zoomOut(1); 
                        this.style.transform = 'scale(0.9)';
                        setTimeout(() => { this.style.transform = 'scale(1)'; }, 200);
                    };
                    
                    // Home button to reset view
                    var homeBtn = document.createElement('button');
                    homeBtn.className = 'zoom-btn';
                    homeBtn.innerHTML = '<i class="fas fa-home" style="font-size: 18px;"></i>';
                    homeBtn.style.cssText = 'background-color: #2196F3; color: white; border: none; border-radius: 50%; width: 45px; height: 45px; margin: 5px 8px; cursor: pointer; font-weight: bold; box-shadow: 0 3px 8px rgba(0,0,0,0.3); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);';
                    homeBtn.onmouseover = function() { this.style.backgroundColor = '#1976D2'; };
                    homeBtn.onmouseout = function() { this.style.backgroundColor = '#2196F3'; };
                    homeBtn.onclick = function() { 
                        map._leaflet_map.setView([22.9734, 78.6569], 5); 
                        this.style.transform = 'scale(0.9)';
                        setTimeout(() => { this.style.transform = 'scale(1)'; }, 200);
                    };
                    
                    // Zoom in button
                    var zoomInBtn = document.createElement('button');
                    zoomInBtn.className = 'zoom-btn';
                    zoomInBtn.innerHTML = '<div style="position: relative; width: 16px; height: 16px;"><div style="position: absolute; top: 6px; left: 0; background: white; width: 16px; height: 4px; border-radius: 2px;"></div><div style="position: absolute; top: 0; left: 6px; background: white; width: 4px; height: 16px; border-radius: 2px;"></div></div>';
                    zoomInBtn.style.cssText = 'background-color: #2196F3; color: white; border: none; border-radius: 50%; width: 45px; height: 45px; margin: 5px 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 3px 8px rgba(0,0,0,0.3); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);';
                    zoomInBtn.onmouseover = function() { this.style.backgroundColor = '#1976D2'; };
                    zoomInBtn.onmouseout = function() { this.style.backgroundColor = '#2196F3'; };
                    zoomInBtn.onclick = function() { 
                        map._leaflet_map.zoomIn(1); 
                        this.style.transform = 'scale(0.9)';
                        setTimeout(() => { this.style.transform = 'scale(1)'; }, 200);
                    };
                    
                    // Add buttons to container
                    zoomContainer.appendChild(zoomOutBtn);
                    zoomContainer.appendChild(homeBtn);
                    zoomContainer.appendChild(zoomInBtn);
                    
                    // Add container to map
                    mapContainer.appendChild(zoomContainer);
                    
                    // Add Font Awesome if not already added
                    if (!document.querySelector('link[href*="font-awesome"]')) {
                        var link = document.createElement('link');
                        link.rel = 'stylesheet';
                        link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css';
                        document.head.appendChild(link);
                    }
                }
            }, 1000); // Delay to ensure map is fully loaded
        }
    </script>
    """
    india_map.get_root().html.add_child(folium.Element(custom_zoom_script))
    
    # Add a layer control to toggle map features
    folium.LayerControl(collapsed=False).add_to(india_map)
    
    
    
    # Save the map to a file in static directory
    india_map.save('static/map.html')
    
    return render_template('index.html')

@app.route('/map')
def map_view():
    """Route to directly serve the map if needed"""
    return render_template('map.html')

@app.route('/api/search-data')
def search_data():
    """API endpoint to provide search data for states, cities, monuments and Kendriya Vidyalayas"""
    # Add necessary fields for search functionality
    search_data = []
    
    for state in india_states:
        # Include only essential data needed for search and navigation
        state_data = {
            'name': state.get('name', ''),
            'latitude': state.get('latitude', 0),
            'longitude': state.get('longitude', 0),
            'type': state.get('type', 'state')
        }
        
        # Include additional searchable fields if available
        if 'capital' in state:
            state_data['capital'] = state['capital']
        
        if 'major_cities' in state:
            state_data['major_cities'] = state['major_cities']
            
        if 'landmarks' in state:
            state_data['landmarks'] = state['landmarks']
        
        # Add state to search results
        search_data.append(state_data)
        
        # If state has Kendriya Vidyalayas, add them as separate searchable items
        if 'kendriya_vidyalayas' in state and state['kendriya_vidyalayas']:
            for kv in state['kendriya_vidyalayas']:
                if 'latitude' in kv and 'longitude' in kv:
                    kv_data = {
                        'name': kv['name'],
                        'latitude': kv['latitude'],
                        'longitude': kv['longitude'],
                        'type': 'kendriya_vidyalaya',
                        'location': kv['location'],
                        'state': state['name']
                    }
                    
                    if 'established' in kv:
                        kv_data['established'] = kv['established']
                        
                    search_data.append(kv_data)
    
    return jsonify(search_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
