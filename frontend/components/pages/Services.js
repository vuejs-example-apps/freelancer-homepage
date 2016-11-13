var ServicesPage = Vue.component('Services', function (resolve, reject) {
    ajax.get("/components/pages/templates/Services.tpl.html", function (template_string) {
        resolve({
            template: template_string                
        });
    });
});  