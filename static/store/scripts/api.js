$((function(context) {
    return function() {
        
        $("#coolbtn").click(function(){
        
            $.ajax({
                "url": "/store/api.getdata/"
            }).done(function(data){
                $('#cooltitle').html(data);
            });
    });


        
    }
})(DMP_CONTEXT.get()));