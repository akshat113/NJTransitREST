# NJTransit Vision Rest Service
>This is a REST service built on top of data from NjTransit API. 

## Requirements

To build this project you will need [Docker][Docker Install] and [Docker Compose][Docker Compose Install].

## Deploy and Run

After cloning this repository, you can type the following command to start the simple app:

```sh
make install
```

Then simply visit [localhost:5000/get?origin_station_id=HB&destination_station_id=NY][App] !
This link will give you all trains form Hoboken Station(HB) to New York Penn Station(NY). For station codes refer to 
stationcode excel file in the project directory or to the dictionary in the app.py file.

The response of the REST service is as below:
Note: This is a sample response. The full response returns more trains in the schedule

```sh
[
  {
    "date": "2020/05/28", 
    "destination_station": "New York Penn Station", 
    "end_time": "07:28 AM", 
    "origin_station": "Hoboken Terminal", 
    "start_time": "06:17 AM", 
    "transit_mode": "light_rail", 
    "travel_time": " 1 hour, 11 minutes"
  }, 
  {
    "date": "2020/05/28", 
    "destination_station": "New York Penn Station", 
    "end_time": "07:09 AM", 
    "origin_station": "Hoboken Terminal", 
    "start_time": "06:25 AM", 
    "transit_mode": "light_rail", 
    "travel_time": " 44 minutes"
  },
]
```


## Important Errors

If you open the API without a origin_station_id or destination_station_id, it will result in a error response.

```sh 
Error: No destination station provided. Please specify an destination station.
```
## Future Scope

The app can be improved by adding Google API to give directions to the nearest station


[Docker Install]:  https://docs.docker.com/install/
[Docker Compose Install]: https://docs.docker.com/compose/install/
[App]: http://127.0.0.1:5000/get?origin_station_id=HB&destination_station_id=NY