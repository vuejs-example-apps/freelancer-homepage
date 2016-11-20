var Price = Vue.component('Price', function (resolve, reject) {
    ajax.get("/components/common/templates/Price.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['price']                        
        });
    });
});  