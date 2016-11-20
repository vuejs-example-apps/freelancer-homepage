var NavigationLinks = Vue.component('NavigationLinks', function (resolve, reject) {
    ajax.get("/components/common/templates/NavigationLinks.tpl.html", function (template_string) {
        resolve({
            template: template_string                        
        });
    });
});  