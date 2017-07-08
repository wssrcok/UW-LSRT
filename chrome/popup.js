$(function() {

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
					newCourses += "\nNow registering "  + input;
				}

				chrome.storage.sync.set({'registering': newCourses});
			}
			$('#process').text(newCourses);
			$('#name').val('');
		});
	});
});