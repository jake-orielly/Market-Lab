function ping() {
    console.log($.ajax({
        url: "http://23.254.164.217:5000/",
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
            console.log(res);
        }
    }))
}