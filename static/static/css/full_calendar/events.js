
$(function(){
  
  var username = $('#username').html();
  var apiKey = $('#key').html();
  var endpoint = "http://localhost:8000/api/event/list/"
  var url = endpoint + "?username=" + username + "&api_key" + "=" + apiKey
    $.when($.get(url).done(function(data){
      var all_events = data.objects;  
      console.log('hmm')
      $("#fullCalendar").fullCalendar({
        events: all_events,
        header:{
          left: '',
          center: 'prev title next',
          right: ''
        },
        eventColor: '#378006',
              
        // modal popup
        eventRender: function(event, element){
          element.attr('href', 'javascript:void(0);');
          element.click(function() {
          $("#startTime").html(moment(event.start).format('MMM Do h:mm A'));
          $("#endTime").html(moment(event.end).format('MMM Do h:mm A'));
          $("#eventInfo").html(event.description);
          $("#eventLink").attr('href', event.url);
          $("#eventId").html(event.id);
          $("#allDay").html(event.all_day);
          $("#eventContent").dialog({ modal: true, title: event.title, width:350});
          });

        }

      });
    }));
});