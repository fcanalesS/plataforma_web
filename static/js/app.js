    jQuery('#go-back').click(function () {
        document.reload()
    });

    jQuery('#enhanced').click(function () {
        jQuery.get('/enhanced', function (result) {
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
            //document.write(result)
        })
    });

    jQuery('#negative').click(function () {
        jQuery.get('/negative', function (result) {
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
            //document.write(result)
        })
    });

    jQuery('#sepia').click(function () {
        jQuery.get('/sepia', function (result) {
            document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
            //document.write(result)
        })
    });

    jQuery("#eq > span").each(function (i) {
        // read initial values from markup and remove that
        var value = parseInt(jQuery(this).text(), 3);
        jQuery(this).empty().slider({
            value: value,
            range: 'max',
            min: -100,
            max: 100,
            animate: true,
            orientation: "vertical",
            slide: function (event, ui){
                if (i==0){
                    jQuery('#blue').val(ui.value)
                }
                if (i==1){
                    jQuery('#green').val(ui.value)
                }
                if (i==2){
                    jQuery('#red').val(ui.value)
                }

                jQuery.ajax({
                    method: 'get',
                    url: '/bgr',
                    data: {blue: jQuery('#blue').val(), green: jQuery('#green').val(), red: jQuery('#red').val()}
                }).success(function (result) {
                    document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
                    //document.getElementById('imagen').innerHTML= 'asdasdasd'
                })
            }
        });
    });

    jQuery("#eq2 > span").each(function (i) {
        // read initial values from markup and remove that
        var value = parseInt(jQuery(this).text(), 3);
        jQuery(this).empty().slider({
            value: value,
            range: 'max',
            min: -100,
            max: 100,
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
                    url: '/brillo-contraste',
                    data: {brillo: jQuery('#bright').val(), contraste: jQuery('#contrast').val()}
                }).success(function (result) {
                    document.getElementById('imagen').innerHTML = '<img class="img-responsive" src="data:image/jpeg;base64,' + result + '">'
                    //document.getElementById('imagen').innerHTML= 'asdasdasd'

                })
            }
        });
    });/**
 * Created by fcanales on 15-04-16.
 */
