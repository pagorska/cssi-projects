function alerting() {
  alert("this is an awesome alert");
}

function hidePs() {
  $("p").hide();
}

alerting();

$(document).ready(hidePs);
