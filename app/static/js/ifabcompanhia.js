
const api_flight = 'https://api.infiniteflight.com/public/v2/flights/7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw';

const api_plans = 'https://api.infiniteflight.com/public/v2/flightplans/7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw';

const api_logo = 'https://raw.githubusercontent.com/Dalmocabral/infinteflightaerobrasil_atc/master/Planilha1.json';





async function tabelacomp() {

    const response = await fetch(api_flight);
    const data = await response.json();
    let array = data.result.filter(x => x.virtualOrganization && x.virtualOrganization.includes('IFAB'));

    const response_log = await fetch(api_logo);
    const comp = await response_log.json();

    const response_plan = await fetch(api_plans);
    const plan = await response_plan.json();
    plans = plan.result



    for (i in array) {


        const get_plane = 'https://api.infiniteflight.com/public/v2/flight/' + array[i].flightId + '/flightplan?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw'

        const response_plan = await fetch(get_plane);
        const plan = await response_plan.json();
        resultado = plan.result
        const lat = resultado.flightPlanItems.map(e => e.location.latitude)
        const long = resultado.flightPlanItems.map(e => e.location.longitude)

        const lat1x = array[i].latitude
        const lon1x = array[i].longitude
        const lat1 = lat[0]
        const lon1 = long[0]
        const lat2 = lat[lat.length - 1]
        const lon2 = long[long.length - 1]

        function distanceLatLongtotal(lat1, lon1, lat2, lon2) {
            if ((lat1 == lat2) && (lon1 == lon2)) {
                return 0;
            }
            else {
                var radlat1 = Math.PI * lat1 / 180;
                var radlat2 = Math.PI * lat2 / 180;
                var theta = lon1 - lon2;
                var radtheta = Math.PI * theta / 180;
                var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
                if (dist > 1) {
                    dist = 1;
                }
                dist = Math.acos(dist);
                dist = dist * 180 / Math.PI;
                dist = dist * 60 * 1.1515;
                dist = dist * 0.8684
                return dist;


            }
        }

        function distanceLatLong(lat1, lon1, lat2, lon2) {
            if ((lat1 == lat2) && (lon1 == lon2)) {
                return 0;
            }
            else {
                var radlat1 = Math.PI * lat1 / 180;
                var radlat2 = Math.PI * lat2 / 180;
                var theta = lon1 - lon2;
                var radtheta = Math.PI * theta / 180;
                var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
                if (dist > 1) {
                    dist = 1;
                }
                dist = Math.acos(dist);
                dist = dist * 180 / Math.PI;
                dist = dist * 60 * 1.1515;
                dist = dist * 0.8684
                return dist;


            }
        }
        total = distanceLatLongtotal(lat1, lon1, lat2, lon2)
        atual = distanceLatLong(lat1x, lon1x, lat2, lon2)       

        


    };

    const distancia = Math.round((atual / total) * 100)
    

    buildTable(array, comp, plans, distancia)
    function buildTable(data, data1, data2, data3) {

        var table = document.getElementById('myTable')

        for (var a in data) {
            for (var b in data1) {
                for (var c in data2) {
                    if (data[a].liveryId == data1[b].LiveryId) {
                        if (data[a].flightId == data2[c].flightId) {
                            var row = `<tr>
                                            <td>IFAB ${data[a].username}</td>
                                            <td>${data[a].callsign}</td>
                                            <td><img src="${data1[b].Logo}" alt="" style="width: 30px; height: 30px;"></td>
                                            <td><img src="../static/img/derp.png" alt=""style="width: 20px;"> ${data2[c].waypoints[1]}</td> 
                                            <td><img src="../static/img/arr.png" alt=""style="width: 20px;">${data2[c].waypoints[data2[c].waypoints.length - 1]}</td>
                                            <td>${Math.trunc(data[a].altitude)} ft</td>
                                            <td>${Math.trunc(data[a].speed)} Kts</td> 
                                            <td class="text-center">
                                            <div class="progress">
                                            <div class="progress-bar progress-bar-striped bg-success progress-bar-animated" role="progressbar" style="width: ${data3}%;" aria-valuenow="${data3}" aria-valuemin="0" aria-valuemax="100">${data3}%</div>
                                          </div>
                                            </td>
                                        </tr>`

                            table.innerHTML += row
                        }
                    }
                }
            }
        }
    }


}
tabelacomp()