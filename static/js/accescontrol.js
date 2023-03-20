
function aviableRolUser(_usser) {
    $.ajax({
        data : {},
        url : '/accescontrol/rolesaviables/'+_usser,
        type: 'get',
        success: function (data){
           var object = JSON.parse(data);
        
           if( object.succes == true ){
                
                $("#urlRequest").val(object.urlRequest);    
                $("#username").val(_usser);

                for( var i =0;i<object.roles.length;i++ ){
                    $('#listRol').append(
                        $(document.createElement('input')).prop({
                            id: 'checkBox_'+object.roles[i],
                            name: 'interest',
                            value: object.roles[i],
                            type: 'checkbox',
                            class:'form-check-input new-rol',
                            style:'margin-right:5px;'
                        })
                    ).append(
                        $(document.createElement('label')).prop({
                            for: 'checkBox_'+object.roles[i],
                            class: 'form-check-label'
                        }).html(object.roles[i] )
                        ).append(document.createElement('br'));
                }
                $("#newRoles").modal('show');

           }else{
                $("#notRoles").modal('show');
           }

            
        },
        error: function(data){
            
        },
     });
}

function viewDetails(_usser) {
    console.log(_usser);
}

function acceptButtonRol(){

    rolesSelect=null;

    $('.new-rol').each(function(){
        if (this.checked) {
            if( rolesSelect == null ){
                rolesSelect =$(this).val();
            }else{ 
                rolesSelect =rolesSelect+"@"+$(this).val();
            }
        }
    });

    urlBack = $("#urlRequest").val();
    userName= $("#username").val();

    if( rolesSelect != null ){
        $.ajax({
            data : {},
            url : '/accescontrol/addrolesthisuser/'+rolesSelect+'/'+userName,
            type: 'get',
            success: function (data){
                
            },
            error: function(data){
                
            },
         });

        $("#listRol").empty(); 
        $("#newRoles").modal('hide');
        $('#formFilter').submit();
    }

    

    
}

