<template>
  <div id="app">
    <app-header :title="title"></app-header>
    <router-view></router-view>
    <router-link to="/order">Make an Order</router-link>        
    <app-footer :author="author"></app-header>
  </div>
</template>

<script>
const fetchInitialData = store => {
  return store.dispatch(`fetchSnapshot`)
}

export default {
  name: 'app',  
  computed: {
    title: function () { return this.$store.state.title },
    author: function () { return this.$store.state.author }
  },
  preFetch: fetchInitialData,
  // mounted () {
  //   fetchInitialData(this.$store)
  // }
}
</script>

<style lang="stylus">
</style>
