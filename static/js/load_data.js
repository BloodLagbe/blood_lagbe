$("#division").change(function () {
alert("Clicked");
    var url = $("#application_form").attr("data-district-url");
    var divisionId = $(this).val();
    $.ajax({
        url: url,
        data: {
        'division': divisionId
        },
        success: function (data) {
        $("#district").html(data);
        }
    });

});

$("#district").change(function () {
    alert("Clicked");
    var url = $("#application_form").attr("data-upazila-url");
    var districtId = $(this).val();
    $.ajax({
        url: url,
        data: {
        'district': districtId
        },
        success: function (data) {
        $("#upazila").html(data);
        }
    });

});
