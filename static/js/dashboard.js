/* globals Chart:false, feather:false */

(function () {
  'use strict';

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [
          8,
          9,
          10,
          18,
          10,
          7,
          6
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#28a745',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#28a745',//#007bff 
      },
      {
        data: [
          6,
          7,
          8,
          8,
          15,
          5,
          3
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#dc3545',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#dc3545',//#007bff 
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  });
})();
(function () {
  'use strict';

  feather.replace()

  // Graphs
  var ctx = document.getElementById('Hits')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        '00',
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23'
      ],
      datasets: [{
        data: [
          1,
          1,
          1,
          4,
          1,
          2,
          1,
          2,
          2,
          5,
          10,
          13,
          12,
          20,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#ffc107',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#ffc107',//#007bff 
      },
      {
        data: [
          3,
          4,
          5,
          5,
          5,
          5,
          4,
          3,
          2,
          1,
          0,
          1,
          2,
          3,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#007bff',//#007bff 
        },
      {
        data: [
          1,
          2,
          3,
          4,
          5,
          5,
          5,
          6,
          6,
          6,
          7,
          7,
          7,
          8,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
          ,
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#5633b6',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#5633b6',//#007bff 
      },]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  });
})();
