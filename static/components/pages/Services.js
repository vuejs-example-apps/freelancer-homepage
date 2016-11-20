var ServicesPage = Vue.component('Services', function (resolve, reject) {
    ajax.get("/components/pages/templates/Services.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            computed: {
                'services': function () {
                    return store.state.services;
                }
            }
        });
    });
});  