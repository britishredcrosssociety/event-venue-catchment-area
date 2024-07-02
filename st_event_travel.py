import streamlit as st
import pandas as pd
import geopandas as gpd
import requests

st.title('Event travel time coverage')

@st.cache_data
def load_postcodes(file): 
	pcds_df = pd.read_parquet(file)
	return pcds_df

if 'disabled' not in st.session_state: 
	st.session_state.disabled = True

with st.spinner("Loading postcode data"): 
	postcodes = load_postcodes('./onspd_may24.parquet')
	postcodes_gdf = gpd.GeoDataFrame(postcodes, geometry= gpd.points_from_xy(postcodes.long, postcodes.lat))

if postcodes is not None: 
	# Get venue postcode input
	venue_postcode = st.text_input(label="Venue postcode (required)", value= None)

	# Get travel time input
	travel_time = st.number_input(label="Travel time in mins (required)", value=60, step=10)

	# Get Mapbox API key input
	token = st.text_input(label="Mapbox token (required)", type="password")

	# help info - where to get a token 
	st.info("How to get a Mapbox token: https://docs.mapbox.com/help/getting-started/access-tokens/")

	valid_postcode = False 

	# validate postcode 
	if type(venue_postcode) == None or venue_postcode == "": 
		valid_postcode = False
	elif type(venue_postcode) != None and ~postcodes.pcds.isin([venue_postcode]).any():	
		valid_postcode = False
	elif postcodes.pcds.isin([venue_postcode]).any(): 
		valid_postcode=True


	# Lookup venue lat/long 
	pcds = postcodes.set_index('pcds')

if valid_postcode == True:
	longitude, latitude = pcds.at[venue_postcode, 'long'], pcds.at[venue_postcode, 'lat']
	# Set API request parameters
	url = f'https://api.mapbox.com/isochrone/v1/mapbox/driving/{longitude}%2C{latitude}?contours_minutes={travel_time}&polygons=true&access_token={token}'

if token and venue_postcode: 
	st.session_state.disabled = False

if st.button(label="Search", type="primary", disabled=st.session_state.disabled):
		# Send API request
		r = requests.get(url)
		# Create GeoDataFrame from API response 
		gdf = gpd.GeoDataFrame.from_features(r.json()['features'])
		# Spatial join the reachable area to the postcode point locations
		reachable_postcodes = postcodes_gdf.sjoin(gdf)
		# Display map of results
		st.map(reachable_postcodes, latitude='lat', longitude='long')
		# Button to generate CSV of reachable postcodes
		st.download_button(label="Download postcodes as CSV", data=reachable_postcodes.to_csv(columns=["pcds"], index=False), 
			file_name=venue_postcode+"_reachable_postcodes.csv", 
			mime="text/csv", type="secondary")

		
