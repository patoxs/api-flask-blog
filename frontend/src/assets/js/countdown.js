;(function($) {
    "use strict";
                        
        /*----------------------------------------------------*/
        /*  Count Down
        /*----------------------------------------------------*/
        var clock;

        clock = $('.clock').FlipClock({
            clockFace: 'DailyCounter',
		    autoStart: false,
		    callbacks: {
                stop: function() {
		          $('.message').html('The clock has stopped!')
                }
            }
		});
				    
        clock.setTime(691200);
		clock.setCountdown(true);
		clock.start()
    
})(jQuery)