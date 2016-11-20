<template>
  <main>
    <h2>PortfolioPage</h2>
    <portfolio-works :works="portfolio.works"></portfolio-works>
  </main>
</template>

<script>
import PortfolioWorks from './subpages/portfolio/PortfolioWorks.vue'

export default {
  name: 'portfolio-page',
  components: {
    'portfolio-works': PortfolioWorks
  },
  computed: {
    'portfolio': function () {
        return this.$store.state.portfolio;
    }
  }
}
</script>

<style lang="stylus">
</style>
