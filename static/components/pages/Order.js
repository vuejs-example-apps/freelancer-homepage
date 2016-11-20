var OrderPage = Vue.component('Order', function (resolve, reject) {
    ajax.get("/components/pages/templates/Order.tpl.html", function (template_string) {
        resolve({
            template: template_string                
        });
    });
});  