/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

function search_twitter(){
    var twitter_query = $("#twitter_query").val();
    var url = "/twitter/?query=" + twitter_query;
    $("#twitter_results_table tbody").empty();
    $.getJSON( url, function( data ) {
        $("#twitter_results_table tbody").empty();
        var rows = [];
        var count = 0;

        data.forEach(function(d){
            count+=1;
            var obj = JSON.parse(d);
            text = obj['text'];
            id = obj['id_str'];
            sn = obj['user']['screen_name'];
            link = "http://twitter.com/"+sn+"/status/"+id;
            link = "<a href='"+link+"'>"+link +"</a>";



            console.log(obj['source']);
            var row = "<tr><th scope='row'>"+count+"</th>" + "<td>"+text+"</td>"+ "<td>"+link+"</td>"+"<td>"+twitter_query+"</td>";


            rows.push(row);
        });




        $("#twitter_results_table tbody").append( rows);

    });

}
