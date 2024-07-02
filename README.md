# Event venue catchment area
Generate catchment areas based on travel time from a UK postcode

This Streamlit app lets you generate a list of postcodes that are reachable from a starting point. 
Reachable areas can be exported as a list of postcodes, to match against supporter records
for more accurate comms targetting. 

## Usage 
1. Enter the event postcode. 
   _The postcode must be a valid and correctly formatted UK postcode_
2. Enter the travel time in minutes (default is 60)
   _The app will search for postcodes reachable by driving for this amount of time
   under normal driving conditions_
3. Enter a Mapbox token
   _The app uses the Mapbox API to generate the search results. If you don't already
   have a token, create a Mapbox account and follow [these instructions](https://docs.mapbox.com/help/getting-started/access-tokens/) 
   to get a token._
4. Click the Search button to get the results 
   _The Search button will be inactive until all parameters are provided_
5. Results will be displayed on a map. To export the results as a CSV, click 
   the button below the map.


## Contribute
If you notice any bugs or have suggestions for improvements, please open an issue. 

## Credits
This application uses the [ONS Postcode directory](https://geoportal.statistics.gov.uk/datasets/a8a2d8d31db84ceea45b261bb7756771/about) which contains data from Royal Mail, Gridlink, LPS (Northern Ireland), Ordnance Survey and ONS Intellectual Property Rights.
* Contains OS data © Crown copyright and database right 2024
* Contains Royal Mail data © Royal Mail copyright and database right 2024
* Source: Office for National Statistics licensed under the Open Government Licence v.3.0
