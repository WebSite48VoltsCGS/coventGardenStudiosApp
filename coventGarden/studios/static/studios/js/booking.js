
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

/*
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
*/

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
    
  /*
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
  */
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
