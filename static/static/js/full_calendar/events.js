$(function(){
  // endpoint
  var username = $('#username').html();
  var apiKey = $('#key').html();
  var endpoint = "http://localhost:8000/api/event/list/"
  var url = endpoint + "?username=" + username + "&api_key" + "=" + apiKey
    
    // -------------------------------------------
    //  event handler
    // -------------------------------------------
    
    getCalendar('month', url)


    // $("#dailyView, #monthlyView, #agendaWeek").change(function(d){

    //     var daily = $('#dailyView').is(':checked')
    //     var monthly = $('#monthlyView').is(':checked')
    //     var agenda = $('#agendaWeek').is(':checked')

    //     if(daily == true){
    //       $('#monthlyView').prop('checked', false);
    //       $('#agendaWeek').prop('checked', false);

    //       getCalendar('basicDay',url)
          
    //     } else if(monthly == true){
    //       $('#dailyView').prop('checked', false);
    //       $('#agendaWeek').prop('checked', false);
    //       getCalendar('month',url)
    //     } else if(agenda){
    //       $('#monthlyView').prop('checked', false);
    //       $('#dailyView').prop('checked', false);
    //       getCalendar('basicWeek',url)
    //     } 
        
    //     $('#eventobjid').val(4);
    //  })



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

    function refetch(){
      $('#fullCalendar').fullCalendar('refetchEvents')
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
        dayClick: function(date, allDay, jsEvent, view) {
          $('#createEvent').dialog({
          title: 'Create New Event',
          width: 350,
          position: {"my" : 'center'},
          draggable: false,
        });
        $(".ui-dialog-titlebar-close")
          .removeClass("ui-dialog-titlebar-close")
          .addClass("fa fa-times");
        },
        
        // modal popup
        // create form
        eventRender: function(event, element){
          element.attr('href', 'javascript:void(0);');
          element.click(function() {
          $("#startTime").html(moment(event.start).format('MMM Do h:mm A'));
          $("#endTime").html(moment(event.end).format('MMM Do h:mm A'));
          $("#eventInfo").html(event.description);
          $("#eventLink").attr('href', event.url);
          $("#eventId").html(event.id);
          $('#eventobjid').val(event.id)
          // $("#createobjid").append("<input id='eventobjid' name='form_id' value=" + event.id + '>')
          //  this will not work - having problems setting ids
          

          $("#eventContent").dialog({ modal: true, title: event.title, width:350});

          });
        } 

      });
    }

   

    // -------------------------------------------
    //  end function
    // -------------------------------------------


});