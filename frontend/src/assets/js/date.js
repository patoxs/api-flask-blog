;(function($) {
    "use strict";
    // Array For Months 
//    var months = ['January','February','March','April','May','June','July', 'August','September','October','November','December'];
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul', 'Aug','Sep','Oct','Nov','Dec'];
    
    // Array For Day of Weeks 
    var weekDay = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'];
    
    // Get the Date
    var today = new Date();
    
    // Print Date
    $('.current_date').html( '<i class="fa fa-clock-o"></i>' + weekDay[today.getDay()] + ', ' + months[today.getMonth()] + ", " + today.getDate()+ ", " + today.getFullYear() );

    
})(jQuery)