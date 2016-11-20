var AppHeader = Vue.component('AppHeader', function (resolve, reject) {
    ajax.get("/components/common/templates/AppHeader.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['title']
        })
    });
});