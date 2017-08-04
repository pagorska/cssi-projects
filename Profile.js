
function disappear() {
    $(".buttons").toggleClass("hidden"); //hides
    $(".hidden-buttons").toggleClass("hidden"); //shows
}
function show() {
    $(".buttons").toggleClass("hidden"); //shows
    $(".hidden-buttons").toggleClass("hidden"); //hides
  //  $(document).ready(function() {alert("hello be happy pt. 3");})
}
function fadeHs() {
    $("h3").click(function() {
      $(this).fadeOut(1000, function() {});
    });
}
function toggleHs() {
    $("h3").toggle();
}
function alerting() {
    alert("hello be happy pt. 2");
}
function moveText() {
    var input_text = $('input').val();
    $('#result').text(input_text);
}
function alertText() {
    alert("you said: " + $('input').val());
}
function pageLoad() {
    $("#pic-button1").click(disappear);
    $("#pic-button2").click(show);
    fadeHs();
    $("img").click(toggleHs);
    $(".button").click(moveText);
    $(".button").click(alertText);

  //  setTimeout(alerting, 3000);
}
//when the document is ready, do this
$(document).ready(pageLoad);
