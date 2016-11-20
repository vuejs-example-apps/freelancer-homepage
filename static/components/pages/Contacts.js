var ContactsPage = Vue.component('Contacts', function (resolve, reject) {
    ajax.get("/components/pages/templates/Contacts.tpl.html", function (template_string) {
        resolve({
            template: template_string                
        });
    });
});  