function detect_device() {
    if (innerWidth <= innerHeight) {
        document.getElementById('landscape').setAttribute('href', 'static/css/base-landscape-mobile.css');
    } else {
        document.getElementById('landscape').setAttribute('href', 'static/css/base-landscape-desktop.css');
    }
}

detect_device();
