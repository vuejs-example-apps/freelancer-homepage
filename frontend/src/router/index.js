import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import HomePage from '../components/pages/Home.vue'
import ServicesPage from '../components/pages/Services.vue'
import PortfolioPage from '../components/pages/Portfolio.vue'
import BioPage from '../components/pages/Bio.vue'
import ContactsPage from '../components/pages/Contacts.vue'
import OrderPage from '../components/pages/Order.vue'

export default new Router({
  mode: 'history',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    { path: '/', component: HomePage },
    { path: '/services', component: ServicesPage },
    { path: '/portfolio', component: PortfolioPage },
    { path: '/bio', component: BioPage },
    { path: '/contacts', component: ContactsPage },
    { path: '/order', component: OrderPage }
  ]
})
