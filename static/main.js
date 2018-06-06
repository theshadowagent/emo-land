var emojies = [];
$( ".emoji-card" ).click(function() {
   var elem = $(this);
   elem.toggleClass( "emoji-card-focus", !elem[0].classList.contains("emoji-card-focus"));
   if (elem[0].classList.contains("emoji-card-focus")) {
       elem.find(".emoji-name").css("display", "none");
       elem.find(".emoji").css("margin", "auto")
       if ($.inArray(elem[0].id, emojies) == -1) {
           emojies.push(elem[0].id);
       }
   } else {
       elem.find(".emoji-name").css("display", "block");
   }
});


$("#post-button").click(function () {
  $.get( "/search", {emo_ids: emojies.toString()}, function (data) {
      $( ".mdl-layout" ).html(data);
  });
});