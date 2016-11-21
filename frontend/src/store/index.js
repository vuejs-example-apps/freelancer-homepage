import Vue from 'vue'
import Vuex from 'vuex'

const inBrowser = typeof window !== 'undefined'
// if in browser, use pre-fetched state injected by SSR
const state = (inBrowser && window.__INITIAL_STATE__) || require('./api_snapshot.json')

Vue.use(Vuex)

import * as actions from './actions'

const mutations = {
  SET_SNAPSHOT: (state, {contacts, customer_reviews, portfolio_works, author, texts, services}) => {
    state.contacts = {...contacts}
    state.customer_reviews = {...customer_reviews}
    state.portfolio_works = {...portfolio_works}
    state.author = {...author}
    state.texts = {...texts}
    state.services = {...services}
    return state
  }
}

export default new Vuex.Store({
  state,
  actions,
  mutations
})