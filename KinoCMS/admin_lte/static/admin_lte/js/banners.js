$(document).ready(function() {
    change_background();
});

function change_background() {
    if ($('#id_mode_0').is(':checked')) {
        $('#id_color').prop("disabled", true);
        $('.btn-img-control').prop("disabled", false);
    } else {
        $('#id_color').prop("disabled", false);
        $('.btn-img-control').prop("disabled", true);
    }
}