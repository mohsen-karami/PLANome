var replaceDigits = function() {
  var map = ["&\#1776;","&\#1777;","&\#1778;","&\#1779;","&\#1780;", "&\#1781;","&\#1782;","&\#1783;","&\#1784;","&\#1785;"]
  document.body.innerHTML = document.body.innerHTML.replace(/\d(?=[^<>]*(<|$))/g, function($0) { return map[$0]});
}

function specifyHeight() {
  document.getElementById('content').style.minHeight = String(innerHeight - 500) + 'px';
}

window.addEventListener('load', function() {
  replaceDigits();
  specifyHeight();
  if (document.getElementById('go-back') && localStorage.getItem('lastPage') && localStorage.getItem('lastPage') != document.referrer) {
    document.getElementById('go-back').style.display = 'block';
    if (window.location != document.referrer) {
      localStorage.setItem('lastPage', document.referrer);
    }
    document.getElementById('go-back').href = localStorage.getItem('lastPage');
  } else if (!document.getElementById('go-back')) {
    localStorage.setItem('lastPage', document.referrer);
  }
}, false);
