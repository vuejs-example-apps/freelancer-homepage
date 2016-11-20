<template>  
  <header>
    <router-link to="/"><h1>{{ title }}</h1></router-link>
    <navigation-links></navigation-links>
  </header>
</template>

<script>
export default {
  name: 'app-header',
  props: ['title']
}
</script>

<style lang="stylus">
</style>
