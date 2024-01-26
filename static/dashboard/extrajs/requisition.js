$(document).ready(function(){
    $('#m-cat , #s-cat , si-cat').on('change',function(){
        var category_id = $('#m-cat').val()
        var sub_category_id = $('#s-cat').val()
        var sub_in_category_id = $('#si_cat').val()

        $.ajax({
            url : '/requisition/get-products/',
            type : 'POST',
            data : {'category_id':category_id,'sub_category_id':sub_category_id,'sub_in_category_id':sub_in_category_id},

            success : function(response){
                if (response.status == 'success'){

                    html = '<option value="">Select Products</option>'

                    for (let i = 0; i < response.products.length; i++) {
                        html += `<option value="${response.products[i].id}">${response.products[i].name}</option>`
                    }

                    $('#response').html(html)
                }
            }
        })
    })



    $('#add-item').on('click' , function(){
        var product = $('#response').val()
        var quantity = $('#quantity').val()
        var note = $('#note').val()
    })
})