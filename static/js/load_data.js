$("#division").change(function () {
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

function callAjax(){
   var divisionID = $("#division").val();
   var districtID = $("#district").val();
   var upazilaID = $("#upazila").val();
   var bloodID = $("#blood").val();
   var url = $("#application_form").attr("donor-url");
    $.ajax({
        url: url,
        data: {
        'division': divisionID,
        'district': districtID,
        'upazila': upazilaID,
        'blood': bloodID,
        },
        success: function (data) {
        $("#object_all").html(data);
        }
    });
}
