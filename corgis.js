alert("are you ready for some corgis???");

function bark() {if ($("span").attr("id") == "Tibby") {
  alert("Tibby just barked!")
} else if ($("span").attr("id") == "Simba") {
  alert("Simba just barked!")
} else if ($("span").attr("id") == "Logan1" || $("span").attr("id") == "Logan2") {
  alert("Logan just barked!")
}
}
$(document).ready(function() {
  bark();
});
