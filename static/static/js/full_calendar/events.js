$(function(){
  
  var username = $('#username').html();
  var apiKey = $('#key').html();
  var endpoint = "http://localhost:8000/api/event/list/"
  var url = endpoint + "?username=" + username + "&api_key" + "=" + apiKey
    
    // -------------------------------------------
    //  event handler
    // -------------------------------------------
     
     $('input').click(function(){
        
        if (this.id == 'dailyView'){
          getCalendar('basicDay',url)
        } else if (this.id == 'monthlyView'){
          getCalendar('month',url)
        } else if (this.id == 'agendaWeek'){
          getCalendar('basicWeek',url)
        }
    
      });

    // -------------------------------------------
    // functions
    // -------------------------------------------

    function getCalendar(type,url){
      $.when($.get(url).done(function(data){
      var all_events = data.objects; 
      var result = 'month'

      fullCalendarType(type,all_events)
 
    })); //end when
    }

    function fullCalendarType(type,events){
      $("#fullCalendar").fullCalendar({
        events: events,
        defaultView: type,
        header:{
          left: '',
          center: 'prev title next',
          right: ''
        },
        // eventColor: '#378006',
        backgroundColor: '#378006',
        
        // modal popup
        eventRender: function(event, element){
          element.attr('href', 'javascript:void(0);');
          element.click(function() {
          $("#startTime").html(moment(event.start).format('MMM Do h:mm A'));
          $("#endTime").html(moment(event.end).format('MMM Do h:mm A'));
          $("#eventInfo").html(event.description);
          $("#eventLink").attr('href', event.url);
          $("#eventId").html(event.id);
          $("#eventContent").dialog({ modal: true, title: event.title, width:350});
          });
        } //end of function

      });
    }

    // -------------------------------------------
    //  end function
    // -------------------------------------------


});