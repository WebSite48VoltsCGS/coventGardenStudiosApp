
/*
document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
  
    var calendar = new FullCalendar.Calendar(calendarEl, {
      timeZone: 'UTC',
      initialView: 'resourceTimeGridDay',
      aspectRatio: 1.5,
      headerToolbar: {
        left: 'prev,next',
        center: 'title',
        right: 'resourceTimeGridDay,resourceTimelineWeek,resourceTimelineMonth'
      },
      editable: true,
      selectable: true,
      locale: 'fr',
      slotDuration: '01:00',
      slotMinTime:"10:00",
      slotMaxTime:"23:59",
      resourceAreaHeaderContent: 'Studios et Salles',
      resources: [
      {
        id: 'a',
        title: 'Room A'
      },
    ],
      events: [
        {
          id: '1',
          resourceId: 'a',
          title: 'Meeting',
          start: '2023-06-30 10:00:00'
        }
      ],
    });
  
    calendar.render();
  });

*/
document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    
    $.ajax({
        url: 'http://127.0.0.1:8000/salles/', // Replace with your endpoint URL
        method: 'GET', // HTTP method (GET, POST, etc.)
        dataType: 'json', // Expected data type of the response
        success: function(data) {
        console.log(data);

        var events_booking;

        $.ajax({
            url: "http://127.0.0.1:8000/api/all_booking_event/",
            method: "GET",
            dataType: "json",
            success: function (datas) {
                events_booking = datas;
                console.log("/api/all_booking_event/");
                console.log(events_booking);
                startCalendar(calendarEl, data, events_booking);
            },
            error: function (error) {
            alert("Error while fetching events");
            }
        });
        
    
        },
        error: function(error) {
        console.error(error);
        }
    });
    
});

function startCalendar(calendarEl, params, events_booking) {
    


    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'UTC',
        initialView: 'resourceTimeGridDay',
        aspectRatio: 1.5,
        headerToolbar: {
          left: 'prev,next',
          center: 'title',
          right: 'resourceTimeGridDay,resourceTimelineWeek,resourceTimelineMonth'
        },
        editable: true,
        selectable: true,
        locale: 'fr',
        slotDuration: '01:00',
        slotMinTime:"10:00",
        slotMaxTime:"23:59",
        resourceAreaHeaderContent: 'Studios et Salles',
        resources: params,
        events: events_booking,
        dateClick: function(info) {
            e.preventDefault();
            console.log(info.resource.title);
            $('#salleName').val(info.resource.title);
            $('#idSalle').val(info.resource.id);
            $('#startDate').val(info.startStr);
            $('#endDate').val(info.endStr);
            $('#confirmation-modal').modal('show');
        
        },
        select: function(info) {
        
            $('#idSalle').val(info.resource.id);
            $('#salleName').val(info.resource.title);
            $('#startDate').val(info.startStr);
            $('#endDate').val(info.endStr);
            $('#confirmation-modal').modal('show');
            console.log(new Date(info.startStr));
        },
    });

    calendar.render();
}

/*
document.addEventListener('DOMContentLoaded', function() {
var calendarEl = document.getElementById('calendar');

$.ajax({
    url: 'http://127.0.0.1:8000/salles/', // Replace with your endpoint URL
    method: 'GET', // HTTP method (GET, POST, etc.)
    dataType: 'json', // Expected data type of the response
    success: function(data) {
    console.log(data);
    startCalendar(calendarEl, data);

    },
    error: function(error) {
    console.error(error);
    }
});

});

function startCalendar(calendarEl, params) {
    var events;

    $.ajax({
      url: "http://127.0.0.1:8000/api/all_booking/",
      method: "GET",
      dataType: "json",
      success: function (datas) {
        events = datas;
      },
      error: function (error) {
        alert("Error while fetching events");
      }
    });
var calendar = new FullCalendar.Calendar(calendarEl, {
selectable: true,
timeZone: 'UTC',
locale: 'fr',
slotDuration: '01:00',
slotMinTime:"10:00",
slotMaxTime:"23:59",
initialView: 'resourceTimeGridDay',
headerToolbar: {
    left: 'prev,next today',
    center: 'title',
    right: 'resourceTimeGridDay,resourceTimeGridWeek'
},
events: events,
resources: params,
dateClick: function(info) {
    e.preventDefault();
    console.log(info.resource.title);
    $('#salleName').val(info.resource.title);
    $('#idSalle').val(info.resource.id);
    $('#startDate').val(info.startStr);
    $('#endDate').val(info.endStr);
    $('#confirmation-modal').modal('show');

},
select: function(info) {

    $('#idSalle').val(info.resource.id);
    $('#salleName').val(info.resource.title);
    $('#startDate').val(info.startStr);
    $('#endDate').val(info.endStr);
    $('#confirmation-modal').modal('show');
    console.log(new Date(info.startStr));
},

});

calendar.render();
}

$(document).ready(function() {
    // Afficher la modale de confirmation lorsqu'on clique sur le bouton
    $('#open-modal').on('click', function() {
        $('#confirmation-modal').modal('show');
    });

    // Lors de la confirmation du formulaire
    $('#confirm-form').on('submit', function(e) {
        //e.preventDefault();
        $('#getReservation').submit();
        // Actions à effectuer si le formulaire est confirmé
        // Exemple : envoyer une requête AJAX pour traiter les données

        // Fermer la modale
        $('#confirmation-modal').modal('hide');
    });

    // Lors de l'annulation du formulaire
    $('#cancel-btn').on('click', function() {
        // Actions à effectuer si le formulaire est annulé
        // Exemple : réinitialiser les champs du formulaire

        // Fermer la modale
        $('#confirmation-modal').modal('hide');
    });
});

*/

/*
for (var current of data) {
    data['id'] = current.id;
    data['title'] = current.username;
    datas.push(data);
}
console.log(datas);
datas = datas
*/

