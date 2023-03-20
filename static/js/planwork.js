Date.prototype.addDays = function (days) {
  const date = new Date(this.valueOf())
  date.setDate(date.getDate() + days)
  return date
}

function formatDateForDB(_dateA){
    var day=_dateA.getDate();
    var month=_dateA.getMonth()+1;
    var year=_dateA.getFullYear();

    if(month <10) month = "0"+month;
    if(day <10) day = "0"+day;
    var convert = year+"-"+month+"-"+day;
    console.log(convert)
    return convert;
}

function showModalAddActivity(_year,_month,_day){
    
    if ( _month < 10 ) _month="0"+_month;
    if ( _day < 10 ) _day="0"+_day;

    var dateCurrent = _year+"-"+_month+"-"+_day;

    $("#id_startDate").val(dateCurrent);
    $("#id_endDate").val(dateCurrent);
    $("#id_name").val("");
    $("#id_description").val("");
    $("#id_color").val("#000000");
    $("#errorDiv").hide();


    $("#modalAddActivity").modal('show');
   
}

function addActivity(){
    
    var dateEnd = new Date($("#id_endDate").val());
    var dateBegin = new Date($("#id_startDate").val());

    dateBegin = dateBegin.addDays(1);
    dateEnd =dateEnd.addDays(1);

    var name = $("#id_name").val();
    var description = $("#id_description").val();
    var color = $("#id_color").val();
    var assignActivity = $('input[name="assignActivity"]:checked').val();
    var isMainMonth = $('#id_isMainMonth').val()

    if (dateBegin > dateEnd){
        $("#errorAddActivity").html("La fecha de comienzo no puede ser posterior a la fecha de finalización");
        $("#errorDiv").show();
    }else{
        $.ajax({
            data : {
                'name':name,
                'description':description,
                'startDate':formatDateForDB(dateBegin),
                'endDate':formatDateForDB(dateEnd),
                'color':color,
                'assignActivity':assignActivity,
                'isMainMonth':isMainMonth,
            },
            url : '/planwork/addAJAX',
            type: 'get',
            success: function (data){
                var object = JSON.parse(data);
                if( object.succes == true ){
                    $("#modalAddActivity").modal('hide');
                    $('#formFilter').submit();

                }else{
                    $("#errorAddActivity").html(object.msg);
                    $("#errorDiv").show();
                }
            },
            error: function(data){
            
            },
        });
    }

    return false;

}

function updateActivity() { 
    e = window.event;
    e.stopPropagation();
 }

function viewDetailsActivity(_idActivity) {
    e = window.event;
    e.stopPropagation();
    $.ajax({
        data : {},
        url: '/planwork/view/'+_idActivity,
        type : 'get',
        success: function(data){
            var object = JSON.parse(data);
            if( object.succes == true ){
                datesRanges =object.datesRanges;

                htmlList='';
                console.log(datesRanges);
                for(var i=0;i<datesRanges.length;i++){
                    htmlList=htmlList+'<div class="col-3 my-2">';
                    htmlList=htmlList+'<b>Inicio:</b>'+datesRanges[i].startDate+'<br><b>   Fin:</b>'+datesRanges[i].endDate;
                    htmlList=htmlList+'</div>';
                }

                $('#listDateRange').html(htmlList);
                $('#labelName').html(object.name);
                $('#labelDescription').html(object.description);
                $('#modalViewActivity').modal('show');
            }
        },
        error: function(data){

        },
    });
}


function removeActivity(_idActivity){
    e = window.event;
    e.stopPropagation();
    $.ajax({
        data : {},
        url : '/planwork/remove/'+_idActivity,
        type: 'get',
        success: function (data){
            var object = JSON.parse(data);
            if( object.succes == true ){
                $('#formFilter').submit();
            }else{
            }
        },
        error: function(data){
            
        },
    });
}


function changeOtherDates(){
    if( $('#id_hasOtherDate').prop('checked') == true){
        $("#tabDates").show();
    }else{
        $("#tabDates").hide();
    }
}

const addDateFormBtn = document.querySelector("#add-date-form");
const submitFormBtn = document.querySelector('[type="submit"]');
const dateForm =document.getElementsByClassName("date-form");
const mainForm =document.querySelector("#listDates");
const totalForms = document.querySelector("#id_form-TOTAL_FORMS")
  
let formCount  = dateForm.length;
  
  
function updateNameAndIDObject(_element,_count){
    if (_element.nodeName!="#text" && _element.nodeName!="BR"){
        const formRegexName = RegExp('form-(\\d+)-','g');
        const formRegexID = RegExp('id_form-(\\d+)-','g');
        if(_element.hasAttribute('name')){
            var name = _element.getAttribute('name');
            name = name.replace(formRegexName,'form-'+_count+'-');
            _element.setAttribute('name',name);
        }
        if(_element.hasAttribute('id')){
            var id = _element.getAttribute('id'); 
            id = id.replace(formRegexID,'id_form-'+_count+'-');
            _element.setAttribute('id',id);
        }
    }
        
    var childs = _element.childNodes;
    for(var i =0;i<childs.length;i++){
        updateNameAndIDObject(childs[i],_count);
    } 
}
  
function updateForm(){
    let count = 0;
    for (let form of dateForm){
        updateNameAndIDObject(form,count);
        count++;
    }
}  
  
if (addDateFormBtn != null){
    addDateFormBtn.addEventListener("click",function(event){
        event.preventDefault();
        const newDateForm = dateForm[0].cloneNode(true);
        const formRegex = RegExp('form-(\\d+)-','g');
        newDateForm.innerHTML = newDateForm.innerHTML.replace(formRegex,'form-'+formCount+'-');
        mainForm.insertBefore(newDateForm,addDateFormBtn);
        formCount++;
        totalForms.setAttribute('value',formCount);
    });
}

if (mainForm != null){
    mainForm.addEventListener("click",function(event){
        if(event.target.classList.contains("delete-date-form") && formCount>=2){
          event.preventDefault();
          event.target.parentElement.parentElement.parentElement.remove();
          formCount--;
          totalForms.setAttribute('value',formCount);
          updateForm();
        }else if(event.target.classList.contains("delete-date-form-icon") && formCount>=2){
          event.preventDefault();
          event.target.parentElement.parentElement.parentElement.parentElement.remove();
          formCount--;
          totalForms.setAttribute('value',formCount);
          updateForm();
        }
      });
}


  

