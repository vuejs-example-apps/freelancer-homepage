var App = Vue.component('App', function (resolve, reject) {
    ajax.get("/components/App.tpl.html", function (template_string) {                
        resolve({
            template: template_string,
            computed: {
                title: function () { return store.state.title },
                author: function () { return store.state.author }
            }
        });    
    });
});