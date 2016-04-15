jQuery('#rotate').slider({
    range: 'max',
        min: 0,
        max: 360,
        value: 0,
        slide: function (event, ui) {
            jQuery.ajax({
                method: 'get',
                url: '/rotate',
                data: {angle: ui.value}
            }).success(function (result) {
                document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
            })
        }
});
