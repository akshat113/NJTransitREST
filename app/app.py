from flask import Flask, render_template
app = Flask(__name__)
from flask import request, jsonify
#import app.njtransit
#import app.stationCode
from bs4 import BeautifulSoup
import requests
from datetime import datetime


#web scraper which collects data from nj transit website. Currently it only runs for light rails
def njtransitScraper(origin,destination):
    origin = station_code_abbrev[origin]
    destination = station_code_abbrev[destination]
    date = str(datetime.now().date()).replace('-','/')
    r = requests.get('https://www.njtransit.com/train-to?origin='+origin+'&destination='+ destination+'&date='+date)

    soup = BeautifulSoup(r.text)
    li = soup.find('main').find(class_='widget').find('ol')
    listElement = li.find_all('li',{'class':'mb-3'})
    trains = []
    for listelement in listElement:
        #stations = listelement.find(class_='media-body').find_all(class_='media-body')
        #if have time add if conditions when we get multiple stations
        times = listelement.find_all(class_='mb-0')
        start_time = times[0].text.strip()
        end_time = times[1].text.strip()
        train = str(listelement.find(class_='mb-md-0').find(class_='w-100').find(text=True))
        train = " ".join(train.split())
        travel_time = listelement.find(class_='mb-md-0').find(class_='w-100').find('div').text
        trains.append({"transit_mode":"light_rail",'start_time': start_time,'end_time': end_time,'travel_time': travel_time,'origin_station': origin,'destination_station': destination,'date':date})
        #trains.append((start_time,end_time,train,travel_time,origin,destination))
    return trains

station_code_abbrev = {
    'AM':'Aberdeen-Matawan Station',
'AB':'Absecon Station',
'AZ':'Allendale Station',
'AH':'Allenhurst Station',
'AS':'Anderson Street Station',
'AN':'Annandale Station',
'AP':'Asbury Park Station',
'AO':'Atco Station',
'AC':'Atlantic City Rail Terminal',
'AV':'Avenel Station',
'BI':'Basking Ridge Station',
'BH':'Bay Head Station',
'MC':'Bay Street Station',
'BS':'Belmar Station',
'BY':'Berkeley Heights Station',
'BV':'Bernardsville Station',
'BM':'Bloomfield Rail Station',
'BN':'Boonton Station',
'BK':'Bound Brook Station',
'BB':'Bradley Beach Station',
'BU':'Brick Church Station',
'BW':'Bridgewater Station',
'BF':'Broadway Station Fair Lawn Station',
'CB':'Campbell Hall Station',
'CM':'Chatham Station',
'CY':'Cherry Hill Station',
'IF':'Clifton Station',
'CN':'Convent Station',
'XC':'Cranford Station',
'DL':'Delawanna Station',
'DV':'Denville Station',
'DO':'Dover Station',
'DN':'Dunellen Station',
'EO':'East Orange Station',
'ED':'Edison Station',
'EH':'Egg Harbor City Station',
'EL':'Elberon Station',
'EZ':'Elizabeth Station',
'EN':'Emerson Station',
'EX':'Essex Street Station (PVL)',
'FW':'Fanwood Station',
'FH':'Far Hills Station',
'FE':'Finderne Station',
'GD':'Garfield Station',
'GW':'Garwood Station',
'GI':'Gillette Station',
'GL':'Gladstone Station',
'GG':'Glen Ridge Station',
'RS':'Glen Rock Station',
'GK':'Glen Rock Boro Hall Station',
'GA':'Great Notch Station',
'HQ':'Hackettstown Station',
'HL':'Hamilton Station',
'HN':'Hammonton Station',
'HR':'Harriman Station',
'HW':'Hawthorne Station',
'HZ':'Hazlet Station',
'HG':'High Bridge Station',
'HI':'Highland Avenue Station',
'HD':'Hillsdale Station',
'HB':'Hoboken Terminal',
'UF':'Hohokus Station',
'JA':'Jersey Avenue Station',
'KG':'Kingsland Station',
'HP':'Lake Hopatcong Station',
'ON':'Lebanon Station',
'LP':'Lincoln Park Station',
'LI':'Linden Station',
'LW':'Lindenwold Station',
'FA':'Little Falls Station',
'LS':'Little Silver Station',
'LB':'Long Branch Station',
'LN':'Lyndhurst Station',
'LY':'Lyons Station',
'MA':'Madison Station',
'MZ':'Mahwah Station',
'SQ':'Manasquan Station',
'MW':'Maplewood Station',
'MP':'Metro Park Station',
'MU':'Metuchen Station',
'MI':'Middleton New Jersey Station',
'MD':'Middletown New York Station',
'MB':'Millburn Station',
'GO':'Millington Station',
'UV':'Montclair State U Station',
'MK':'Monmouth Park Station',
'HS':'Montclair Heights Station',
'ZM':'Montvale Station',
'MX':'Morris Plains Station',
'MR':'Morristown Station',
'OL':'Mount Olive Station',
'TB':'Mount Tabor Station',
'MS':'Mountain Avenue Station',
'ML':'Mountain Lakes Station',
'MT':'Mountain Station',
'MV':'Mountain View Station',
'MH':'Murray Hill Station',
'NN':'Nanuet Station',
'NT':'Netcong Station',
'NE':'Netherwood Station',
'NB':'New Brunswick Station',
'NV':'New Providence Station',
'NA':'Newark Airport Station',
'ND':'Newark Broad Street Station',
'NP':'Newark Penn Station',
'OR':'North Branch Station',
'NZ':'North Elizabeth Station',
'NH':'New Bridge Landing Station',
'OD':'Oradell Station',
'OG':'Orange Station',
'OS':'Ottisville Station',
'PV':'Park Ridge Station',
'PS':'Passaic Station',
'RN':'Paterson Station',
'PC':'Peapack Station',
'PQ':'Pearl River Station',
'NY':'New York Penn Station',
'PE':'Perth Amboy Station',
'PH':'Philadelphia Station',
'PF':'Plainfield Station',
'PL':'Plauderville Station',
'PP':'Point Pleasant Beach Station',
'PO':'Port Jervis Station',
'PR':'Princeton Station',
'PJ':'Princeton Junction Station',
'FZ':'Radburn-Fairlawn Station',
'RH':'Rahway Station',
'RY':'Ramsey Station',
'17':'Ramsey Rt 17 Station',
'RA':'Raritan Station',
'RB':'Red Bank Station',
'RW':'Ridgewood Station',
'RG':'River Edge Station',
'RL':'Roselle Park Station',
'RF':'Rutherford Station',
'CW':'Salisbury Mills-Cornwall Station',
'SE':'Secaucus Upper Lvl Station',
'TS':'Secaucus Lower Lvl Station',
'RT':'Short Hills Station',
'XG':'Sloatsburg Station',
'SM':'Somerville Station',
'CH':'South Amboy Station',
'SO':'South Orange Station',
'LA':'Spring Lake Station',
'SV':'Spring Valley Station',
'SG':'Stirling Station',
'SF':'Suffern Station',
'ST':'Summit Station',
'TE':'Teterboro Station',
'TO':'Towaco Station',
'TR':'Trenton Station',
'TC':'Tuxedo Station',
'US':'Union Station',
'UM':'Upper Montclair Station',
'WK':'Waldwick Station',
'WA':'Walnut Street Station',
'WG':'Watchung Avenue Station',
'WT':'Watsessing Avenue Station',
'23':'Wayne-Route 23 Station',
'WF':'Westfield Station',
'WW':'Westwood Station',
'WH':'White House Station',
'WR':'Wood Ridge Station',
'WB':'Woodbridge Station',
'WL':'Woodcliff Lake Station'
}

code_station_abbrev = dict(map(reversed, station_code_abbrev.items()))
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def api_all():
    if 'origin_station_id' in request.args:
        origin_station_id = request.args['origin_station_id']
    else:
        return "Error: No origin station provided. Please specify an origin station."

    if 'destination_station_id' in request.args:
        destination_station_id = request.args['destination_station_id']
    else:
        return "Error: No destination station provided. Please specify an destination station."

    trains = njtransitScraper(origin_station_id,destination_station_id)
        # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    #for book in books:
    #    if book['id'] == id:
    #        results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(trains)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')