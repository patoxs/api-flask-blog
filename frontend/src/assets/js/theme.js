;(function($) {
    "use strict";
    
    
    $(document).ready(function(){
        
        /*----------------------------------------------------*/
        /*  Header Padditon Top
        /*----------------------------------------------------*/
        $('.header1.row').css( "padding-top", function(){
            return $('.header1 .navbar-fixed-top').height() 
        });
        
        /*----------------------------------------------------*/
        /*  Tooltip
        /*----------------------------------------------------*/
        $('[data-toggle="tooltip"]').tooltip();
        
        
        /*----------------------------------------------------*/
        /*  Left Sided / Category Fixed Menu
        /*----------------------------------------------------*/
        $('#slideMenu_trigger').on( "click", function(){       
            $('.sliding_menu').addClass('show');
            $('.slideMenuClose').addClass('show')
        });
        $('.sliding_menu #menuHide,.slideMenuClose').on( "click", function(){
            $('.sliding_menu,.slideMenuClose').removeClass('show')
        });
        
        
        /*----------------------------------------------------*/
        /*  Right ScrollSpy Show/Hide
        /*----------------------------------------------------*/
        $('#scrollSpyTrigger').on('click',function(){
            $('.scrollspyMenu').toggleClass('show');
            return false
        });
        
        
        /*----------------------------------------------------*/
        /*  Navigation Scroll
        /*----------------------------------------------------*/
        $(window).scroll(function() {    
            var scroll = $(window).scrollTop();

            if (scroll >= 10) {
                $(".navigation_bar").addClass("scrolled")
            } else {
                $(".navigation_bar").removeClass("scrolled")
            }
        });
        
        /*----------------------------------------------------*/
        /*  Post Dot Gallery
        /*----------------------------------------------------*/
        $('.post_dot_gallery').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            autoplay:true,
            dots: true,
            dotsEach: true,
            items: 1
        });
        
        /*----------------------------------------------------*/
        /*  Post Dot Gallery
        /*----------------------------------------------------*/
        $('.simple_single_img_slider').owlCarousel({
            loop:true,
            margin:0,
            nav:true,
            navText: [
              "<i class='fa fa-angle-left'></i>",
              "<i class='fa fa-angle-right'></i>"
            ],
            navContainer: '.simple_single_img_slider',
            dots:false,
            autoplay:true,
            items: 1
        });
        
        /*----------------------------------------------------*/
        /*  Counter Up - Fun Facts
        /*----------------------------------------------------*/
        $('.social_facts li a span').counterUp({
            delay: 10,
            time: 1000
        });
                
        /*----------------------------------------------------*/
        /*  Instafeed
        /*----------------------------------------------------*/
        var feed = new Instafeed({
            get: 'popular',
            limit: 9,
            clientId: '489097d3abcf4dd285d6feb8d0dd83e9',
            template: '<li><a href="{{link}}" class="insta_img"><img src="{{image}}" /></a><li>'
        });
        feed.run();  
        
        /*----------------------------------------------------*/
        /*  Related Post Carousel
        /*----------------------------------------------------*/
        $('.related_posts_carousel').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            dotsContainer: '#related_post_dots',
            autoplay:true,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:2
                },
                1000:{
                    items:3
                }
            }
        });
        
        /*----------------------------------------------------*/
        /*  Staffs
        /*----------------------------------------------------*/
        $('.staffs_carousel').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            autoplay:false,
            dots:true,
            responsive:{
                0:{
                    items:1
                },
                700:{
                    items:2
                },
                990:{
                    items:3
                },
                1300:{
                    items:4
                }
            }
        });
        
        /*----------------------------------------------------*/
        /*  Staffs
        /*----------------------------------------------------*/
        $('.popular_posts_carousel').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            autoplay:false,
            dots:true,
            responsive:{
                0:{
                    items:1
                },
                700:{
                    items:2
                },
                1000:{
                    items:3
                },
                1300:{
                    items:4
                }
            }
        });
        
        /*----------------------------------------------------*/
        /*  PopUps
        /*----------------------------------------------------*/
        $('a.zoom_gallery_img').magnificPopup({
            type: 'image',
            gallery:{
                enabled: true
            }
        });
        
        /*----------------------------------------------------*/
        /*  PopUps - Newsletter Signup Popup / Search Form
        /*----------------------------------------------------*/
        $('a.subscribe_popup').magnificPopup({
            type: 'ajax'
        });
        $('a#search_form').magnificPopup({
            type: 'ajax'
        });
                
        /*----------------------------------------------------*/
        /*  Go To
        /*----------------------------------------------------*/        
        $('.scrollspyMenu a[href^="#"], a#tap2allpost').on('click', function(event) {

            var target = $( $(this).attr('href') );

            if( target.length ) {
                event.preventDefault();
                $('html, body').animate({
                    scrollTop: target.offset().top - 90
                }, 1000)
            }

        });
        
        /*----------------------------------------------------*/
        /*  Switch - Post by Author
        /*----------------------------------------------------*/
        $('#check_less_more_author_post').on('click',function(){
            $('#other_author_info').slideToggle()
        });
        
        /*----------------------------------------------------*/
        /*  Progress Bar
        /*----------------------------------------------------*/
        $('.counter').counterUp({
            delay: 10,
            time: 1000
        });
        $('.progress .progress-bar').each(function(){
            var $this = $(this);
            var width = $this.data('amount');
            $this.css({
                'transition' : 'width 2s'
            });

            setTimeout(function() {
                $this.waypoint(function(direction) {
                    if( direction === 'down' ) {
                        $this.css({
                            'width' : width + '%'
                        })
                    }
                } , { offset: '100%' } )
            }, 500)
        });
        
        /*----------------------------------------------------*/
        /*  Author Cover Image 
        /*----------------------------------------------------*/
        $( ".author_page_header .cover_img" ).each(function() {
            var attr = $(this).data('image');

            if (typeof attr !== typeof undefined && attr !== false) {
                $(this).css('background-image', 'url('+attr+')')
            }
        });          
        $('.author_page_header .cover_img').css( "height", function(){
            return $('.author_page_header .cover_img + .author_intro').height()
        })
        
    });
    
    $(window).load(function(){
        
        /*----------------------------------------------------*/
        /*  Preloader
        /*----------------------------------------------------*/
        $('.preloader').addClass('complete');
        setTimeout(
            function(){
                $('.preloader').fadeOut('slow')    
            },2100
        );
        
        /*----------------------------------------------------*/
        /*  Menu Scoll
        /*----------------------------------------------------*/
        $(".sliding_menu").mCustomScrollbar();
        
        /*----------------------------------------------------*/
        /*  Flexslider
        /*----------------------------------------------------*/        
        
        $('#post7_slider_control').flexslider({
            animation: "slide",
            controlNav: false,
            animationLoop: false,
            slideshow: false,
            itemWidth: 104,
            itemMargin: 5,
            asNavFor: '#post7_slider'
        });

        $('#post7_slider').flexslider({
            animation: "slide",
            controlNav: false,
            animationLoop: false,
            slideshow: false,
            sync: "#carousel"
        })
        
    })
    
})(jQuery)