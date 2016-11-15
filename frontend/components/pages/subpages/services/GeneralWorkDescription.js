var GeneralWorkDescription = Vue.component('GeneralWorkDescription', function (resolve, reject) {
    ajax.get("/components/pages/subpages/services/templates/GeneralWorkDescription.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['stages']                
        });
    });
});  