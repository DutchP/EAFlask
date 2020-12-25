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
          15,
          13,
          15,
          14,
          13,
          12,
          16
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#28a745',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#28a745',//#007bff 
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
          18,
          10,
          10,
          10,
          9,
          9,
          8,
          7,
          6,
          4,
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#28a745',// #007bff
        borderWidth: 4,
        pointBackgroundColor: '#28a745',//#007bff 
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
