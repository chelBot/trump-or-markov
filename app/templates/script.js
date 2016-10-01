
var main = function(){
  $(".btn-primary").click(function(){
    $(".check").addClass("hidden");
  });
  $(".btn-head").click(function(){
    if($(this).attr("id") == "markov"){
      $("#markov-red").removeClass("hidden");
    }else{
      $("#trump-green").removeClass("hidden");
    }
  });
};
$(document).ready(main);
