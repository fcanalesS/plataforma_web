jQuery('#rotate').slider({
    range: 'min',
    min: 0,
    max: 360,
    step: 90,
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

jQuery('#blur').slider({
    range: 'min',
    min: 0,
    max: 100,
    slide: function (event, ui) {
        jQuery.ajax({
            method: 'get',
            url: '/blur',
            data: {blur: ui.value}
        }).success(function (result) {
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
        })
    }
});

jQuery('#sharp').slider({
    range: 'min',
    min: 0,
    max: 100,
    slide: function (event, ui) {
        jQuery.ajax({
            method: 'get',
            url: '/sharp',
            data: {sharp: ui.value}
        }).success(function (result) {
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
        })
    }
});

jQuery('#mirror').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/mirror'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
    });
});

