//d3.json("/test_json/NewRoutes_def.json", function(data) {
 //   console.log(BEB_list_p20);
//});

d3.csv("/dataset/BEB_list_p20.csv", function(BEB_list_p20) {
    console.log(BEB_list_p20);
});

d3.csv("/dataset/BEB_list_p60.csv", function(BEB_list_p60) {
    console.log(BEB_list_p60);
});

d3.csv("/dataset/BEB_list_p180.csv", function(BEB_list_p180) {
    console.log(BEB_list_p180);
});