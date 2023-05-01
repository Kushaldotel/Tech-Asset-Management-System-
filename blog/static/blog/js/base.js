function responsiveNav() {
    var x = document.getElementById("nav");
    if (x.className === "responsive-nav") {
      x.className = "";
    } else {
      x.className = "responsive-nav";
    }
  }
  
  window.onload = function() {
    var icon = document.createElement("a");
    icon.setAttribute("class", "icon");
    icon.setAttribute("onclick", "responsiveNav()");
    icon.innerHTML = "&#9776;";
    document.querySelector("nav").appendChild(icon);
  };
  