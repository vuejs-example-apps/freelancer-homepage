var ServicePackages = Vue.component('ServicePackages', function (resolve, reject) {
    ajax.get("/components/pages/subpages/services/templates/ServicePackages.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['packages']                
        });
    });
});  