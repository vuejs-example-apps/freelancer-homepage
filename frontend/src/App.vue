<template>
  <div id="app">
    <app-header :title="title"></app-header>
    <router-view></router-view>
    <router-link to="/order">Make an Order</router-link>        
    <app-footer :author="author"></app-header>
  </div>
</template>

<script>
export default {
  name: 'app',  
  computed: {
    title: function () { return this.$store.state.title },
    author: function () { return this.$store.state.author }
  }
}
</script>

<style lang="stylus">
</style>
