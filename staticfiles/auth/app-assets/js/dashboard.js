const paidUnpaidChart=(data, labels) => {
	var ctx = document.getElementById('paidUnpaidChart').getContext('2d');
	var myChart = new Chart(ctx, {
			type: 'doughnut',
			data: {
					labels: labels,
					datasets: [{
							label: 'Paid and Unpaid User',
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
						text:'Paid and Unpaid Users'
					}
			}
	});
};

const getPaidUnpaidChart=()=> {
	fetch('/paid_unpaid',{
    method: 'POST',
    headers: {
      'Content-Type':'application/json',
      'X-CSRFToken': csrftoken,
    }
  })
	.then((res) => res.json())
	.then((results) => {
    const user_data = results.PaymentData    
		const [label, data] = [Object.keys(user_data), Object.values(user_data)];
		paidUnpaidChart(data, label);
	})
}
try {
  document.onload = getPaidUnpaidChart();
} catch (error) {
  
}


  //-------------- Line Chart Widget 1 Configuration starts --------------

  widgetlineChart1 = new Chartist.Line('#Widget-line-chart', {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug"],
    series: [
      [55, 60, 50, 55, 50, 60, 55, 57]
    ]
  }, {
    axisX: {
      showGrid: false,
      showLabel: false,
      offset: 0,
    },
    axisY: {
      showGrid: false,
      low: 50,
      showLabel: false,
      offset: 0,
    },
    fullWidth: true
  });


  //-------------- Line Chart Widget 2 Configuration starts --------------

  widgetlineChart2 = new Chartist.Line('#Widget-line-chart2', {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug"],
    series: [
      [75, 50, 65, 55, 75, 50, 65, 70]
    ]
  }, {
    axisX: {
      showGrid: false,
      showLabel: false,
      offset: 0,
    },
    axisY: {
      showGrid: false,
      low: 50,
      showLabel: false,
      offset: 0,
    },
    fullWidth: true
  });
//-------------- Line Chart Widget 2 Configuration starts --------------

widgetlineChart2 = new Chartist.Line('#Widget-line-chart1', {
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug"],
  series: [
    [75, 50, 65, 55, 75, 50, 65, 70]
  ]
}, {
  axisX: {
    showGrid: false,
    showLabel: false,
    offset: 0,
  },
  axisY: {
    showGrid: false,
    low: 50,
    showLabel: false,
    offset: 0,
  },
  fullWidth: true
});


  //-------------- Line Chart Widget 3 Configuration starts --------------

  widgetlineChart3 = new Chartist.Line('#Widget-line-chart3', {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug"],
    series: [
      [57, 60, 55, 65, 50, 70, 60, 65]
    ]
  }, {
    axisX: {
      showGrid: false,
      showLabel: false,
      offset: 0,
    },
    axisY: {
      showGrid: false,
      low: 50,
      showLabel: false,
      offset: 0,
    },
    fullWidth: true
  });
