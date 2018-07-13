;(function($) {
    "use strict";

        /*----------------------------------------------------*/
        /*  Chart
        /*----------------------------------------------------*/
        // Get context with jQuery - using jQuery's .get() method.
        var ctx = $(".example_chart").get(0).getContext("2d");
        // This will get the first returned node in the jQuery collection.
        var data = {
            labels: ["7:00", "8:00", "9:00", "10:00", "11:00", "12:00"],
            datasets: [
                {
                    label: "My First dataset",
                    fillColor: "rgba(32,149,242,0.2)",
                    strokeColor: "#2095f2",
                    pointColor: "#2095f2",
                    pointStrokeColor: "#2095f2",
                    pointHighlightFill: "#2095f2",
                    pointHighlightStroke: "#2095f2",
                    data: [15, 20, 25, 13, 45, 55]
                },
                {
                    label: "My Second dataset",
                    fillColor: "rgba(243,29,18,0.2)",
                    strokeColor: "#f31d12",
                    pointColor: "#f31d12",
                    pointStrokeColor: "#f31d12",
                    pointHighlightFill: "#f31d12",
                    pointHighlightStroke: "#f31d12",
                    data: [13, 32, 25, 50, 25, 15]
                }
            ]
        };
        var options = {
            scaleShowGridLines : false
        };
        var myNewChart = new Chart(ctx).Line(data, options);
    
})(jQuery)