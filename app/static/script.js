
var main = function(){
  $(".btn-primary").click(function(){
     location.reload();
    // $(".check").addClass("hidden");
  });
  $(".btn-head").click(function(){
    if($(this).attr("id") == "markov" && answer == 'M'){
      $("#markov-green").removeClass("hidden");
    }else if($(this).attr("id") == "markov" && answer != 'M'){
      $("#markov-red").removeClass("hidden");
    }else if($(this).attr("id") == "trump" && answer == 'T'){
      $("#trump-green").removeClass("hidden");
    }else if($(this).attr("id") == "trump" && answer != 'T'){
      $("#trump-red").removeClass("hidden");
    }
    console.log(answer);
  });
  $(".about").on("click", function(){
    $(".dropdown-menu").toggle();
  })
  $('img').on('dragstart', function(event) { event.preventDefault(); });
};
$(document).ready(main);
