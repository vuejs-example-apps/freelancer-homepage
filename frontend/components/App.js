var App = Vue.component('App', function (resolve, reject) {
    ajax.get("/components/App.tpl.html", function (template_string) {
        ajax.getJSON("/app_data.json", function (app_data) {        
            resolve({                
                template: template_string,
                data: function () { return app_data; }               
            })
        });    
    });
});