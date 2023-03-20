function updateAreaUM(){
    $.ajax({
        data : {},
        url : '/areaum/update_directory_single',
        type: 'get',
        success: function (data){
           var object = JSON.parse(data);
           
           if ( object.success == true){
                $("#messageSuccess").html(object.message);
                $("#divCancel").hide();
                $("#divOk").show();
                
           }else{
                $("#messageDanger").html(object.message);
                $("#divCancel").show();
                $("#divOk").hide();
           }
           
           $("#modalAreaUM").modal('show');
           
          

        },
        error: function(data){
            
        },
     });
}

function clickAcceptModal(){
     $("#modalAreaUM").modal('hide');
     $('#formFilter').submit();
}