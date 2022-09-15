$('#add_img').click(function() {
	var form_idx = $('#id_form-TOTAL_FORMS').val();
	$('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});

function delete_image(index) {
    if (confirm("Вы действительно хотите удалить картинку?")) {
        $('#' + index + '-form').append('<input type="hidden" value="on" name="' + index  + '-DELETE" id="id_' + index + '-DELETE">');
        $('#' + index + '-form').css('display', 'none');
    }
}

function preview_gallery(index) {
	$('#' + index + '-image').attr('src', URL.createObjectURL(event.target.files[0]));
};