alert("hello!");



function stuffToDoWhenReady() {
   $("#hello").click(function() {
     $(this).fadeOut(1000, function() {})
   });
//  $("#hello").fadeOut(1000, stuffToDoWhenFadeOutIsDone)
}
function stuffToDoWhenFadeOutIsDone() {
  alert("done!");
}
function stuffToDoWhenClicked() {
  $(this).fadeOut(1000, function() {});
}

$(document).ready(stuffToDoWhenReady)
