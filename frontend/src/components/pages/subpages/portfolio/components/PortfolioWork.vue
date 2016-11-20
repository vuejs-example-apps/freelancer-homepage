<template>
  <div class="portfolio-work">
    <h4>{{ work.name }}</h4>
    <ul>
        <li v-for="pic in work.pics">{{ pic.title }}</li>
    </ul>    
  </div>
</template>

<script>
export default {
  name: 'portfolio-work',
  props: ['work']
}
</script>

<style lang="stylus">
</style>
