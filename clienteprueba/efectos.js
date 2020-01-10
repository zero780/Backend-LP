//METODO GET
$('.api_get').click( function() {
  var id_get = $("input#id_get").val();
    $.ajax({
      
             url : "http://localhost:8000/api/participants/"+String(id_get)+"/",
             type: 'GET',
             dataType: "json",
             success : function (data) {
                      $('#id').text( data.id);
                      $('#names').text( data.names);
                      $('#last_names').text( data.last_names);
              }
    });
});


//METODO POST
/*$(".api_post").click(function(){          

    var data = {};
    data.nombre = $("#nombre_post").val();
    data.precio = $("#precio_post").val();
    data.año = $("#año_post").val();

    $.ajax({
        url: "http://localhost:8000/api/carros/",
        type: "POST",
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function (xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
    },
    success: function (arg) {
        location.reload()
    },
        success: function(data){
            alert(data);
        },
        failure: function(errMsg) {
            alert(errMsg);
        }
    });
});*/