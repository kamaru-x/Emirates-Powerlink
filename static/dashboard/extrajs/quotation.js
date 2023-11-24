$(document).ready(function(){
    $('.price').on('input' , function(){
        var itemId = $(this).data('id');
        var quantity = $(this).data('quantity');
        var price = $(this).val();

        var netPrice = parseFloat(price) * parseInt(quantity);
        $('#net-' + itemId).val(netPrice.toFixed(2));
    })
})