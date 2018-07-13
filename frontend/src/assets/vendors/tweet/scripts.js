jQuery(function($){
    var FEED = window.FEED||{};
    
    FEED.TWEET= function(){
        $('.tw_username').twittie({
            count: 1,
            template: '{{user_name}}'
        });
        $('.tweets_feed').twittie({
            dateFormat: '%d %b, %Y',
            count: 15,
            template:
                '<div class="row m0 tw_content"><div class="tweet_text row m0">'+'{{tweet}}'+'</div>'
                +'<div class="row m0">{{date}}</div></div>'
                +'<div class="row m0 footer"><div class="tweet_user fleft">'                    
                    + '<i class="fa fa-twitter"></i>{{user_name}}'
                +'</div>'
                +'<div class="tweet_time fright">'+'<a href="{{url}}">Visit my Twitter</a>'+ '</div></div>'
        },
        function(){
            $(".tweets_feed ul").owlCarousel({
                loop:true,
                margin:0,
                nav:true,
                navContainer: "#carousel_nav",
                navText: [
                  "<i class='fa fa-angle-left'></i>",
                  "<i class='fa fa-angle-right'></i>"
                  ],
//                autoplay:true,

                responsive:{
                    0:{
                        items:1
                    },
                    800:{
                        items:2
                    },
                    1000:{
                        items:3
                    },
                    1200:{
                        items:4
                    }
                }
            });
        })
    }
    
    $(document).ready(function(){FEED.TWEET();})
})