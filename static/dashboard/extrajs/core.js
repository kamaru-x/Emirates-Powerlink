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

    // sub category fetch start //
    $('#m-cat').on('change' , function(){
        var cat_id = $('#m-cat').val()

        $.ajax({
            url : '/get-sub-categories/',
            type : 'POST',
            data : {'cat-id':cat_id},

            success : function(response){

                if(response.sub_categories){
                    $('#scat-div').show()
                }else{
                    $('#scat-div').hide()
                }

                html = '<option value="">Search Sub Category</option>'

                for (let i = 0; i < response.sub_categories.length; i++) {
                    html += '<option value="'+response.sub_categories[i].id+'">'+response.sub_categories[i].Name+'</option>'
                }

                html += '<option value="None">None</option>'

                $('#s-cat').html(html)
            }
        })
    })
    // sub category fetch end //

    // sub in category fetch start //
    $('#s-cat').on('change' , function(){
        var cat_id = $('#s-cat').val()

        $.ajax({
            url : '/get-sub-in-categories/',
            type : 'POST',
            data : {'cat-id':cat_id},

            success : function(response){

                if(response.sub_in_categories){
                    $('#sicat-div').show()
                }else{
                    $('#sicat-div').hide()
                }

                html = '<option value="">Search Sub Category</option>'

                for (let i = 0; i < response.sub_in_categories.length; i++) {
                    html += '<option value="'+response.sub_in_categories[i].id+'">'+response.sub_in_categories[i].Name+'</option>'
                }

                html += '<option value="None">None</option>'

                $('#si-cat').html(html)
            }
        })
    })
    // sub in category fetch start //

    // ############################################################################################ //

    // sub category fetch start //
    $('#new-m-cat').on('change' , function(){
        var cat_id = $('#new-m-cat').val()

        $.ajax({
            url : '/get-sub-categories/',
            type : 'POST',
            data : {'cat-id':cat_id},

            success : function(response){

                if(response.sub_categories){
                    $('#new-scat-div').show()
                }else{
                    $('#new-scat-div').hide()
                }

                html = '<option value="">Search Sub Category</option>'

                for (let i = 0; i < response.sub_categories.length; i++) {
                    html += '<option value="'+response.sub_categories[i].id+'">'+response.sub_categories[i].Name+'</option>'
                }

                html += '<option value="None">None</option>'

                $('#new-s-cat').html(html)
            }
        })
    })
    // sub category fetch end //

    // sub in category fetch start //
    $('#new-s-cat').on('change' , function(){
        var cat_id = $('#new-s-cat').val()

        $.ajax({
            url : '/get-sub-in-categories/',
            type : 'POST',
            data : {'cat-id':cat_id},

            success : function(response){

                if(response.sub_in_categories){
                    $('#new-sicat-div').show()
                }else{
                    $('#new-sicat-div').hide()
                }

                html = '<option value="">Search Sub Category</option>'

                for (let i = 0; i < response.sub_in_categories.length; i++) {
                    html += '<option value="'+response.sub_in_categories[i].id+'">'+response.sub_in_categories[i].Name+'</option>'
                }

                html += '<option value="None">None</option>'

                $('#new-si-cat').html(html)
            }
        })
    })
    // sub in category fetch start //

    // ############################################################################################ //
})