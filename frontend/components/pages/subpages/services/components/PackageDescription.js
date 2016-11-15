var PackageDescription = Vue.component('PackageDescription', function (resolve, reject) {
    ajax.get("/components/pages/subpages/services/components/templates/PackageDescription.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['package']
        });
    });
});  