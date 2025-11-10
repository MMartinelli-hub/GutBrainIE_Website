// fixes an issue in main.js which prevents proper animation and loading of logo
$(document).ready(function() {
    setTimeout(function() {
     $("body").removeClass('is-loading');
    }, 1000);
   }); 