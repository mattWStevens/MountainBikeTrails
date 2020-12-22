$(document).ready(function() {
    var visitedCheckBox = document.getElementById('id_visited');

    visitedCheckBox.addEventListener("click", respondVisitedCheck);

    handleVisitedChecked(visitedCheckBox.checked);  // Initialize screen after refresh.
});

function respondVisitedCheck() {
    var visited = document.getElementById('id_visited');

    handleVisitedChecked(visited.checked)
}

function handleVisitedChecked(checked) {
    var els = document.getElementsByTagName('LABEL');

    for (var i = 0; i < els.length; i++) {
        if (els[i].innerHTML == "Visited on:" ||
            els[i].innerHTML == "My rating:" ||
            els[i].innerHTML == "Top ten:") {

            els[i].style.display = (checked) ? "Block" : "None";
        }
    }

    (checked) ? $('#id_visited_on_month').show() : $('#id_visited_on_month').hide();
    (checked) ? $('#id_visited_on_day').show() : $('#id_visited_on_day').hide();
    (checked) ? $('#id_visited_on_year').show() : $('#id_visited_on_year').hide();
    (checked) ? $('#id_my_rating').show() : $('#id_my_rating').hide();
    (checked) ? $('#id_top_ten').show() : $('#id_top_ten').hide();
    (checked) ? $('.helptext').show() : $('.helptext').hide();
}