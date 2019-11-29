var replaceDigits = function() {
  var map = ["&\#1776;","&\#1777;","&\#1778;","&\#1779;","&\#1780;", "&\#1781;","&\#1782;","&\#1783;","&\#1784;","&\#1785;"]
  document.body.innerHTML = document.body.innerHTML.replace(/\d(?=[^<>]*(<|$))/g, function($0) { return map[$0]});
}

function detect_device() {
    if (innerWidth <= innerHeight) {
        document.getElementById('landscape').setAttribute('href', 'static/css/base-landscape-mobile.css');
    } else {
        document.getElementById('landscape').setAttribute('href', 'static/css/base-landscape-desktop.css');
    }
}

window.onload = replaceDigits;
detect_device();