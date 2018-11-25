function render_single_bar_graph(labels,data,y_axis){
    var backgroundColor = [];
    for (let i=0;i<labels.length;i++){
        backgroundColor.push('#5AB9EA')
    }
    var barData = {
        labels: labels,
        datasets: [{
            label: y_axis,
            backgroundColor: backgroundColor,
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

function render_double_bar_graph(){
    let data = {
        "labels": [
            "Food",
            "Alcoholic beverages",
            "Housing",
            "Apparel and services",
            "Transportation",
            "Healthcare",
            "Entertainment",
            "Personal care",
            "Reading",
            "Education",
            "Tobacco",
            "Miscellaneous",
            "Cash",
            "Personal"
        ],
        "datasets": [
            {
                "label": "percent",
                "data": [
                    "12.6",
                    "11.2"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "0.9",
                    "1"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "32.9",
                    "39.2"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "3.2",
                    "2.6"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "16.4",
                    "12.4"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "7.9",
                    "6.4"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "5.1",
                    "5.1"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "1.2",
                    "1.1"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "0.2",
                    "0.2"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "2.3",
                    "2.6"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "0.6",
                    "0.4"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "1.6",
                    "1.6"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "3.4",
                    "3.9"
                ]
            },
            {
                "label": "percent",
                "data": [
                    "11.6",
                    "12.1"
                ]
            }
        ]
    }

    var ctx = document.getElementById("chart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: data,
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
