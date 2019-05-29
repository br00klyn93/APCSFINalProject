function shake() {
  var el = document.getElementById("main-img");
  el.classList.add("animated");
  el.classList.add("bounceIn");

  setTimeout(function () {
    el.classList.remove("animated");
    el.classList.remove("bounceIn");
  }, 500);
}

function delays() {
  console.log("Work");
  var rows = document.getElementsByTagName("li");
  var place = 1;
  var i;
  for(i = 0; i < rows.length; i++) {
    console.log("ran");
    var time = "delay-"+place+"s";
    rows[i].classList.add("animated");
    rows[i].classList.add("fadeInUp");
    rows[i].classList.add(time);
    place+=1;
  }
}

function selectPhoto() {
     var elem = document.getElementById("photoSelect");
     if(elem && document.createEvent) {
        var evt = document.createEvent("MouseEvents");
        evt.initEvent("click", true, false);
        elem.dispatchEvent(evt);
     }

}

function checkFiles() {
  //Placeholder, replace with actual item count when complete
  items = 3;

  if(items != 0) {
    document.getElementById("blank").style.display = "none";
  }
}
