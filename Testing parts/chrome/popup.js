$(function() {
	$.ajax({ url: 'https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=AUT+2017&SLN=13862', 
		success: function() { 
			if ((document.documentElement.textContent || document.documentElement.innerText)
			.indexOf('** Closed **') > -1) {
				$('#found').text("yeah, we found it's closed");
			} else {
				$('#found').text("it's still open");
			}
		} 
	});
	chrome.storage.sync.get('registering', function(course) {
		$('#process').text(course.registering);
	})

	$('#button').click(function() {
		chrome.storage.sync.get('registering', function(course) {
			var newCourses = "";
			if (course.registering != "") {
				newCourses += course.registering;
			}

			var input = $('#name').val();

			if (input == "clear") {
				chrome.storage.sync.set({'registering': ""});
				newCourses = "";
			} else {
				if (input != "") {
					newCourses += "Now registering "  + input;
				}

				chrome.storage.sync.set({'registering': newCourses});
			}
			$('#process').text(newCourses);
			$('#name').val('');
		});
	});
});
/*
if (
  (
    document.documentElement.textContent || document.documentElement.innerText
  ).indexOf('Done successfuly') > -1
) {
  // Do something...
}
*/