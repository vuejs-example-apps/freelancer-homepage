var PortfolioWork = Vue.component('PortfolioWork', function (resolve, reject) {
    ajax.get("/components/pages/subpages/portfolio/components/templates/PortfolioWork.tpl.html", function (template_string) {
        resolve({
            template: template_string,
            props: ['work']
        });
    });
});  