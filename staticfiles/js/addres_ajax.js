// ajajx function for load districts by division id

$(document).ready(function () { 
    $("#id_division").change(function () {
        let division_id = $(this).val();
        let url = '/ajax/load_districts/'
        $.ajax({
            url: url,
            data: {
                'division_id': division_id,
            },
            success: function (data) {
                $("#id_district").html(data);
            },
        });
    });

// ajajx function for load upazila by district_id

    $("#id_district").change(function () {
        let district_id = $(this).val();
        let url = '/ajax/load_upazila/'
        $.ajax({
            url: url,
            data: {
                'district_id': district_id,
            },
            success: function (data) {
                $("#id_upazila").html(data);
            },
        });
    });

// ajajx function for load union by upazila_id

    $("#id_upazila").change(function () {
        let upazila_id = $(this).val();
        let url = '/ajax/load_union/'
        $.ajax({
            url: url,
            data: {
                'upazila_id': upazila_id,
            },
            success: function (data) {
                $("#id_union").html(data);
            },
        });
    });

// ajajx function for load village by union_id

    $("#id_union").change(function () {
        let union_id = $(this).val();
        let url = '/ajax/load_village/'
        $.ajax({
            url: url,
            data: {
                'union_id': union_id,
            },
            success: function (data) {
                $("#id_village").html(data);
            },
        });
    });
})