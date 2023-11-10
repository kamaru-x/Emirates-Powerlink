$(".file").change(function () {
    var fileExtension = ['jpg' , 'jpeg' , 'jfif ', 'pjpeg' , 'pjp','png'];
    if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
        alert("Only formats are allowed : "+fileExtension.join(', '));
        $(".file").val('');
    }
});