var PortfolioPage = Vue.component('Portfolio', function (resolve, reject) {
    ajax.get("/components/pages/templates/Portfolio.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            computed: {
                'portfolio': function () {
                    return store.state.portfolio;
                }
            }                
        });
    });
});  