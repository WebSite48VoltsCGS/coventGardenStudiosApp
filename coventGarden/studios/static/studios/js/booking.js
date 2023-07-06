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