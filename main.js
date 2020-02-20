let tickers = [];
let periods = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'];
let intervals = ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'];

function graph() {
    let data = {}
    data.stocks = tickers;
    data.period = periods[$('#period-slider').val()];
    data.interval = intervals[$('#interval-slider').val()];
    var settings = {
        'url': 'http://23.254.164.217:5000/compare',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': '*/*',
        },
        'data': JSON.stringify(data)
    }
      
    $.ajax(settings).done(function (response) {
        $('#graph').attr('src',"results.png?" + new Date().getTime());
        console.log(response)
    });
}

function optionsInfo(ticker) {
    let data = {}
    data.tickerName = ticker;
    data.date = '2020-02-21';
    data.percent = 5;
    data.contractType = 'call';
    $('#loading-ripple').show();
    var settings = {
        'url': 'http://23.254.164.217:5000/options_info',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': '*/*',
        },
        'data': JSON.stringify(data)
    }
      
    $.ajax(settings).done(function (response) {
        buildOptionsTable(JSON.parse(response.data))
        $('#options-table-div').show();
        $('#curr-price').html(response['curr_price'])
        $('#loading-ripple').hide();
    });
}

function pageLoad() {
    $('#loading-ripple').hide();
    $('#options-table-div').hide();
}

function addTicker() {
    $('#tickers-list').append('<li><div class="ticker-item">' + $('#ticker-input').val() + 
    '<span onclick="optionsInfo(\'' + $('#ticker-input').val() + '\')" class="ticker-remove">&#128269;</span>' + 
    '<span data-name="' + $('#ticker-input').val() + '" onclick="remove(this)" class="ticker-remove">&#10006;</span></div></li>');
    tickers.push($('#ticker-input').val());
    $('#ticker-input').val('')
}


function periodUpdate(){
    $('#period-label').html(periods[$('#period-slider').val()])
}

function intervalUpdate(){
    $('#interval-label').html(intervals[$('#interval-slider').val()])
}

/* function showCharts() {
    $('.chart-div').show();
    $('.options-div').hide();
}

function showOptions() {
    $('.chart-div').hide();
    $('.options-div').show();
} */

function remove(ticker) {
    let name = $(ticker).data('name')
    let index = tickers.indexOf(name)
    if (index != -1)
        tickers.splice(tickers,1)
    $(ticker).parent().remove();
}

function buildOptionsTable(data) {
    let table = '#options-table';
    $(table).empty();
    $(table).append('<thead></thead>');
    $(table + ' thead:last').append('<tr></tr>');
    for (let col in data)
        $(table + ' tr:last').append('<th>' + col + '</th>')
    $(table).append('<tbody></tbody>')
    for (let row in data[Object.keys(data)[0]]) {
        $(table + ' tbody').append('<tr id="' + row + '"></tr>') 
        for (let col in data)
            $(table + ' tbody tr:last').append('<td>' + roundTo(data[col][row],2) + colAddons(col)  + '</td>')
    }
}

function colAddons(col) {
    if (col == 'breakEvenPercentDiff' || col == 'percentOfCurr')
        return '%'
    return '';
}