
$(function(){
	
  siteURL = "http://127.0.0.1:5000/"
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
  	alert(" arch");
  	$('#darchive').fadeIn("slow");
  	
  	
  });








  $('#delete').on('click',function(event){
  	    event.preventDefault();
        alert('this button was clicked');
        $('#formNewPost').hide();
        $('#tablePosts .col-lg-8').css("display:inline"); 
        $('#tablePosts').show(); 
  	    $('#formNewPost').css("display:none"); 
  	   
  	 
  })


  $('#tablePosts tr td a').on('click',function(event){
  	
  	 var ttt = $(this).parent().siblings().html();
     alert(ttt);
  	 alert("this is also");
  	  $.ajax({
        url: siteURL + "posts/post_to_delete/" + parseInt(ttt),
        type: 'GET',
        data: ttt,
        success: function(result) {
            alert("wow");
        }
     
        
    
 }); 
   
  	    
           
        
  })
  
 
var mySwiper1 = new Swiper ('.swiper1', {
    // Optional parameters
    autoplay: {
    delay: 5000,
    },
    // If we need pagination
    pagination: {
      el: '.swiper-pagination1',
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next1',
      prevEl: '.swiper-button-prev1',
    },

    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar1',
    },
  })


var mySwiper2 = new Swiper ('.swiper2', {
    // Optional parameters
    autoplay: {
    delay: 5000,
    },
    // If we need pagination
    pagination: {
      el: '.swiper-pagination2',
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next2',
      prevEl: '.swiper-button-prev2',
    },

    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar2',
    },
  })





  });





