var BioPage = Vue.component('Bio', function (resolve, reject) {
    ajax.get("/components/pages/templates/Bio.tpl.html", function (template_string) {
        resolve({
            template: template_string                
        });
    });
});  