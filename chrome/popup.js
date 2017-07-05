$(function() {
	$('#name').keyup(function(){
		$('#greet').text('Now registering ' + $('#name').val());
	})
})