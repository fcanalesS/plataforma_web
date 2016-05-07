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
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
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
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
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
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
        })
    }
});

jQuery('#mirror').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/mirror'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
    });
});

jQuery("#eq4 > span").each(function (i) {
        // read initial values from markup and remove that
        var value = parseInt(jQuery(this).text(), 3);
        jQuery(this).empty().slider({
            value: value,
            range: 'max',
            min: 0,
            max: 500,
            animate: true,
            orientation: "vertical",
            slide: function (event, ui){
                if (i==0){
                    jQuery('#bright').val(ui.value)
                }
                if (i==1){
                    jQuery('#contrast').val(ui.value)
                }

                jQuery.ajax({
                    method: 'get',
                    url: '/border',
                    data: {val1: jQuery('#bright').val(), val2: jQuery('#contrast').val()}
                }).success(function (result) {
                    document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:images/jpeg;base64,' + result + '">'
                    //document.getElementById('imagen').innerHTML= 'asdasdasd'

                })
            }
        });
    });