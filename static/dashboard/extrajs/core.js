$(document).ready(function(){

    // category duplication start //
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
    // category duplication end //

    // username duplication start //
    $('#username').on('keyup paste',function(){
        var username = $('#username').val()
        console.log(username)

        $.ajax({
            url : '/c-u-d/',
            type : 'POST',
            data : {'username':username},

            success : function(response){
                console.log(response.message)
                if (response.status === 'failed') {
                    $('#username').addClass('border-danger');
                    $('#error').show()
                    $('#submit-btn').prop('disabled', true);
                } else {
                    $('#username').removeClass('border-danger');
                    $('#error').hide()
                    $('#submit-btn').prop('disabled', false);
                }
            }
        })
    })
    // username duplication end //
})