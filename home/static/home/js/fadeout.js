$(window).scroll(function(){
    $(".top").css("opacity", 1 - $(window).scrollTop() / 250);
  });


/*win.scroll(function(){
  scrollPosition = win.scrollTop();
  scrollRatio = 1 - scrollPosition / 300;
  $(".top").css("opacity", scrollRatio);
*/





/*$(window).scroll(function(){
    var scrollVar = $(window).scrollTop();
    $('.top').css("opacity", 1 - scrollVar/300);
})*/
$('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrainWidth: false, // Does not change width of dropdown to that of the activator
      hover: false, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: false, // Displays dropdown below the button
      // Displays dropdown with edge aligned to the left of button
      stopPropagation: false // Stops event propagation
    }
  );


