function render_bar_graph(labels,data){
    var barData = {
        labels: labels,
        datasets: [{
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
             data : data
        }]
    };

    var ctx = document.getElementById("chart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: barData,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });

}
