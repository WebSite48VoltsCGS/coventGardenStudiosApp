document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  $.ajax({
    url: "http://127.0.0.1:8000/all_events/",
    method: "GET",
    dataType: "json",
    success: function(datas) {
      events = datas;
      initializeCalendar(datas);
    },
    error: function(error) {
      alert("Error while fetching events");
    }
  });

  function initializeCalendar(events) {
    var calendar = new FullCalendar.Calendar(calendarEl, {
      eventClick: function(info) {
        var eventObj = info.event;
  
        if (eventObj) {
          alert(
            eventObj.title +'.\n'+ eventObj.start + '.\n' + eventObj.end + '.\n' + eventObj.description + '.\n' + 
            eventObj.url
          );
        } 
      },
      headerToolbar: {
        left: 'prev,next',
        center: 'title',
        right: ''
      },
      locale: 'fr',
      editable: false,
      firstDay: 1,
      slotMinTime: '10:00',
      slotMaxTime: '23:59',
      slotDuration: '01:00',
      events: events,
      selectable: true,
    
    });
    calendar.render();
  }
});
