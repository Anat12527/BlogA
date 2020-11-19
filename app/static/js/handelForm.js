
$(function(){
	

 $('.custom-file-input').change(function (e) {
 	alert("in");
        if (e.target.files.length) {
            $(this).next('.custom-file-label').html(e.target.files[0].name);
        }
    });

 function checkUser(){
	var nameU = $('nav ul:eq(1) li:eq(0)').text();
	if (nameU!='Admin12')
	{
      $('nav ul:eq(0) li:eq(3)').hide();
	}

	else
	{
	  $('nav ul:eq(0) li:eq(3)').show();
	}
 }
 
 checkUser();
 
  $('nav ul:eq(0) li:eq(4)').on('click',function(){
  	$('.data-archive').fadeIn(100);
  	$('.data-archive').css({'display' : 'block'});
  	
  });




  $('#delete').on('click',function(e){
  	if (this.id == 'delete') {
        alert('this button was clicked');
    }

  	$('#formNewPost').hide();
    $('#tablePosts .col-lg-8').css("display:inline"); 
  	$('#tablePosts').show(); 
  	$('#formNewPost').css("display:none"); 
  	
  	 
  })





  });
 
