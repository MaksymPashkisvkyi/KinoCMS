function showPreview(name, event) {
    $("#" + name + "_preview").attr('src', URL.createObjectURL(event.target.files[0]));
}

function deletePreview(name, event) {
    $("#" + name + "_preview").attr('src', "/static/cinema/dist/img/preview_upload.png")
}