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

jQuery('#mirror').click(function () {
    jQuery.ajax({
        method: 'get',
        url: '/mirror'
    }).success(function (result) {
        document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
    });
});

jQuery("#eq3 > span").each(function (i) {
        var value = parseInt(jQuery(this).text(), 2);
        jQuery(this).empty().slider({
            value: value,
            range: 'max',
            min: 0,
            max: 100,
            animate: true,
            orientation: "vertical",
            slide: function (event, ui){
                if (i==0){
                    jQuery('#sharp').val(ui.value)
                }
                if (i==1){
                    jQuery('#blur').val(ui.value)
                }

                jQuery.ajax({
                    method: 'get',
                    url: '/sharp-blur',
                    data: {sharp: jQuery('#sharp').val(), blur: jQuery('#blur').val()}
                }).success(function (result) {
                    document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
                    //document.getElementById('imagen').innerHTML= 'asdasdasd'

                })
            }
        });
    });

