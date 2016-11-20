<template>
  <div class="portfolio-works">
    <portfolio-work v-for="work in works" :work="work"></portfolio-work>
  </div>
</template>

<script>
import PortfolioWork from './components/PortfolioWork.vue'

export default {
  name: 'portfolio-works',
  props: ['works'],
  components: {
    'portfolio-work': PortfolioWork
  }
}
</script>

<style lang="stylus">
</style>
