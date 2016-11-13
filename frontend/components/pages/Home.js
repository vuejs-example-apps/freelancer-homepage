var HomePage = Vue.component('Home', function (resolve, reject) {
    ajax.get("/components/pages/templates/Home.tpl.html", function (template_string) {
        resolve({
            template: template_string                
        });
    });
});  