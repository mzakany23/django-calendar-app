$(function(){
			
			$('#deleteEvent').click(function(e){
				var result = confirm('Are you sure you want to delete event?')
				if(result == true){
					
					var username = $('#username').html();
		  		var apiKey = $('#key').html();
		  		var id = $('#eventId').html()
		  		var endpoint = "http://localhost:8000/api/event/list/" + id + '/'
		  		var url = endpoint + "?username=" + username + "&api_key" + "=" + apiKey

					$.ajax({
						url: url,
						type: 'DELETE',
						success: function(){
							console.log('worked')
						}
					});
				}
				
				// e.preventDefault();
				$('#eventContent').dialog('close')
			});

			$('#createEventId').click(function(){
				$('#createNewEvent').dialog({
					width: 350,
					position: {"my" : 'center'},
					draggable: false,
				});
				$(".ui-dialog-titlebar-close")
          .removeClass("ui-dialog-titlebar-close")
          .addClass("fa fa-times");
			});
		});