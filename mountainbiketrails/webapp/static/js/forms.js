$(document).ready(function() {
    $('#id_visited_on_month').hide();
    $('#id_visited_on_day').hide();
    $('#id_visited_on_year').hide();
    $('#id_my_rating').hide();
    $('#id_top_ten').hide();
    $('.helptext').hide();

    var els = document.getElementsByTagName('LABEL');

    for (var i = 0; i < els.length; i++) {
        if (els[i].innerHTML == "Visited on:" ||
            els[i].innerHTML == "My rating:" ||
            els[i].innerHTML == "Top ten:") {
            els[i].style.display = "None";
        }
    }

    // Will also need function to listen for when visited gets checked and
    // when it is checked to reverse what is done above and when unchecked to reverse
    // again.
});