var PortfolioWorks = Vue.component('PortfolioWorks', function (resolve, reject) {
    ajax.get("/components/pages/subpages/portfolio/templates/PortfolioWorks.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['works']
        });
    });
});  