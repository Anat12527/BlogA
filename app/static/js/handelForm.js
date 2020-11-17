$(function(){
	
  $('#inputTitle').keyup(function(e){
  	console.log(e.target.value);
  });

  $('#inputPostAuthor').keyup(function(e){
  	console.log(e.target.value);
  });
 

 $('.custom-file-input').change(function (e) {
 	alert("in");
        if (e.target.files.length) {
            $(this).next('.custom-file-label').html(e.target.files[0].name);
        }
    });

 
 function checkUser(){
	var nameU = $('nav ul:eq(1) li:eq(0)').text();
	if (nameU!='Admin')
	{
      $('nav ul:eq(0) li:eq(3)').hide();
	}

	else
	{
	  $('nav ul:eq(0) li:(3)').show();
	}
 }
 
 checkUser();

  $('nav ul:eq(0) li:eq(4)').on('click',function(){
  	$('.data-archive').fadeIn(100);
  	$('.data-archive').css({'display' : 'block'});
  	
  });


  





  });
 
