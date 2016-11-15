var AdditionalServices = Vue.component('AdditionalServices', function (resolve, reject) {
    ajax.get("/components/pages/subpages/services/templates/AdditionalServices.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['services']
        });
    });
});  