var AppFooter = Vue.component('AppFooter', function (resolve, reject) {
    ajax.get("/components/common/templates/AppFooter.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['author']                        
        });
    });
});  