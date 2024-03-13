const infoChart=(data, labels) => {
	var ctx = document.getElementById('infoChart').getContext('2d');
	var myChart = new Chart(ctx, {
			type: 'pie',
			data: {
					labels: labels,
					datasets: [{
							label: 'Information Supplied',
							data: data,
							backgroundColor: [
									'rgb(91,110,212)',
									'rgb(62,148,168)',
							],
							borderColor: [
									'rgb(124,166,232)',
									'rgb(91,192,136)',
							],
							borderWidth: 1
					}]
			},
			options: {
					scales: {
							yAxes: [{
									ticks: {
											beginAtZero: true
									}
							}]
					},
					title:{
						display:true,
						text:'Information Supplied'
					}
			}
	});
};

const getInfoChart=()=> {
	fetch('/user_info/',{
    method: 'POST',
    headers: {
      'Content-Type':'application/json',
      'X-CSRFToken': csrftoken,
    }
  })
	.then((res) => res.json())
	.then((results) => {
    const user_data = results.InfoDetails    
		const [label, data] = [Object.keys(user_data), Object.values(user_data)];
		infoChart(data, label);
	})
}


document.onload = getInfoChart();
