function showLocPopup(weekNum, locationContent, locationColor, locationHighlightColor) {
  var popup = document.getElementById("loc-popup");
  var title = document.getElementById("loc-popup-title");
  var info = document.getElementById("loc-popup-info");

  title.innerHTML = "Week " + weekNum;
  info.innerHTML = locationContent;
  info.style.color = locationHighlightColor;
  popup.style.display = "block";
}

function hideLocPopup() {
  document.getElementById("loc-popup").style.display = "none";
}

function showExpPopup(weekNum, experienceContent, experienceColor, experienceHighlightColor) {
  var popup = document.getElementById("exp-popup");
  var title = document.getElementById("exp-popup-title");
  var info = document.getElementById("exp-popup-info");

  title.innerHTML = "Week " + weekNum;
  info.innerHTML = experienceContent;
  info.style.color = experienceHighlightColor;
  popup.style.display = "block";
}

function hideExpPopup() {
  document.getElementById("exp-popup").style.display = "none";
}

// Add event listener to close the popup when clicked outside
window.onclick = function(event) {
  var popup = document.getElementById("loc-popup");
  if (event.target == popup) {
    popup.style.display = "none";
  }
}