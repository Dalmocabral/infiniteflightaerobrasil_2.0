
const api_flight = 'https://api.infiniteflight.com/public/v2/flights/7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw';

const api_plans = 'https://api.infiniteflight.com/public/v2/flightplans/7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw';

const api_logo = 'https://raw.githubusercontent.com/Dalmocabral/infinteflightaerobrasil_atc/master/Planilha1.json';





async function tabelacomp() {

    const response = await fetch(api_flight);
    const data = await response.json();
    let array = data.result.filter(x => x.virtualOrganization && x.virtualOrganization.includes('Infinite Flight Aero Brasil'));

    const response_log = await fetch(api_logo);
    const comp = await response_log.json();

    const response_plan = await fetch(api_plans);
    const plan = await response_plan.json();
    plans = plan.result

    buildTable(array, comp, plans)
    function buildTable(data, data1, data2) {

        var table = document.getElementById('myTable')

        for (var a in data){
            for (var b in data1){
                for (var c in data2){
                    if(data[a].liveryId == data1[b].LiveryId){
                        if (data[a].flightId == data2[c].flightId){
                            var row = `<tr>
                                            <td>IFAB ${data[a].username}</td>
                                            <td>${data[a].callsign}</td>
                                            <td><img src="${data1[b].Logo}" alt="" style="width: 30px; height: 30px;"></td>
                                            <td><img src="../static/img/derp.png" alt=""style="width: 20px;"> ${data2[c].waypoints[1]}</td> 
                                            <td><img src="../static/img/arr.png" alt=""style="width: 20px;">${data2[c].waypoints[data2[c].waypoints.length - 1]}</td>
                                            <td>${Math.trunc(data[a].altitude)} ft</td>
                                            <td>${ Math.trunc(data[a].speed)} Kts</td> 
                                            <td><a href="https://liveflightapp.com/?f=${data[a].flightId}&s=7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856"
                                target="_blank">Track</a></td>
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