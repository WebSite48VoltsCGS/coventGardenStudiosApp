document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var events;

  $.ajax({
    url: "http://127.0.0.1:8000/all_events/",
    method: "GET",
    dataType: "json",
    success: function (datas) {
      events = datas;
      initializeCalendar();
    },
    error: function (error) {
      alert("Error while fetching events");
    }
  });

  function initializeCalendar() {
    var calendar = new FullCalendar.Calendar(calendarEl, {
      headerToolbar: {
        left: 'prev,next',
        center: 'title',
        right: '',
      },
      locale: 'fr',
      editable: false,
      firstDay: 1,
      slotMinTime: '10:00',
      slotMaxTime: '23:59',
      slotDuration: '01:00',
      allDaySlot: false,
      events: events,
    });

    calendar.render();
  }
});
