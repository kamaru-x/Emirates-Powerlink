$(document).ready(function(){
    $('#category-name').on('keyup paste',function(){
        var name = $('#category-name').val()
        console.log(name)

        $.ajax({
            url : '/c-c-d/',
            type : 'POST',
            data : {'name':name},

            success : function(response){
                console.log(response.message)
                if (response.status === 'failed') {
                    $('#category-name').addClass('border-danger');
                    $('#error').show()
                    $('#submit-btn').prop('disabled', true);
                } else {
                    $('#category-name').removeClass('border-danger');
                    $('#error').hide()
                    $('#submit-btn').prop('disabled', false);
                }
            }
        })
    })
})