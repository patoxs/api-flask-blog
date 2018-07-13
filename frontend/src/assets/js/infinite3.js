;(function($) {
    "use strict";
    
    $(window).load(function(){
        
        /*----------------------------------------------------*/
        /*  Istope and Infinite Scroll
        /*----------------------------------------------------*/
        var $container = $('#gallery_posts');

        $container.isotope({
            // options
            itemSelector: '.post',
            percentPosition: true,
            layoutMode: 'masonry',
            masonry: {
              columnWidth: 0
            }
        });
        
        $('#filters li').on( 'click', function() {
            $('#filters').find('.active').removeClass('active');
            $(this).addClass('active');
            var $filterValue = $(this).data('filter');
            $container.isotope({ filter: $filterValue });
        });

        $container.infinitescroll({
            navSelector : '#page_nav a:last',    // selector for the paged navigation 
            nextSelector: '#page_nav a:last',  // selector for the NEXT link (to page 2)
            itemSelector: '#gallery_posts .post',     // selector for all items you'll retrieve
            loading: {
                finished: undefined,
                finishedMsg: "<em>Congratulations, you've reached the end of the internet.</em>",
                msgText: "<em>Loading the next set of posts...</em>",
                selector: null,
                speed: 'slow',
                start: undefined
            }
        },
        // call Isotope as a callback
        function( newElements ) {
            $container.isotope( 'appended', $( newElements ) ) 
        });
        
        // kill scroll binding
        $(window).unbind('.infscr');

        // hook up the manual click guy.
        $('#page_nav a').on("click",function(){
            $container.infinitescroll('retrieve');
            return false
        });

        // remove the paginator when we're done.
        $(document).ajaxError(function(e,xhr,opt){
            if (xhr.status == 404) $('#page_nav').remove()
        });
        
    })
    
})(jQuery)