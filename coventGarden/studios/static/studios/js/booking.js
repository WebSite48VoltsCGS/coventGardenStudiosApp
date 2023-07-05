document.addEventListener('DOMContentLoaded', function() {

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
          for (let index = 1; index <= data.length; index++) {
            //const element = array[index];
            var name = "calendar"+index;
            var calendarEl = document.getElementById(name);
            console.log("event pour une ressource");
            var currentEvent = [];
            for (const event of events_booking) {
              if (event.resourceId == data[index-1].id) {
                currentEvent.push(event);
              }
            }
            console.log(currentEvent);
            startCalendar(calendarEl, data[index-1], currentEvent);
          }
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
    aspectRatio: 1.5,
    editable: true,
    selectable: true,
    locale: 'fr',
    slotDuration: '01:00',
    slotMinTime:"10:00",
    slotMaxTime:"23:59",
    initialView: 'timeGridWeek',
    allDaySlot: false,
    headerToolbar: {
      left: 'prev,next',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay' // user can switch between the two
    },
    events: events_booking,
    dateClick: function(info) {
      e.preventDefault();
      console.log(info);
      
      $('#salleName').val(params.title);
      $('#idSalle').val(params.id);
      $('#startDate').val(info.startStr);
      $('#endDate').val(info.endStr);
      $('#confirmation-modal').modal('show');
      
    },
    select: function(info) {
      $('#salleName').val(params.title);
      $('#idSalle').val(params.id);
      $('#startDate').val(info.startStr);
      $('#endDate').val(info.endStr);
      $('#confirmation-modal').modal('show');
      console.log(new Date(info.startStr));
    },
  });
  calendar.render();
}
<<<<<<< HEAD

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

const button = document.querySelector("button")
button.addEventListener("click", () => {
  fetch("http://localhost:3000/create-checkout-session", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      items: [
        { id: 1, quantity: 3 },
        { id: 2, quantity: 1 },
      ],
    }),
  })
    .then(res => {
      if (res.ok) return res.json()
      return res.json().then(json => Promise.reject(json))
    })
    .then(({ url }) => {
      window.location = url
    })
    .catch(e => {
      console.error(e.error)
    })
})
=======
>>>>>>> e8ef0676b57fd4fb5591658b5c99d4f0d18af9f1
