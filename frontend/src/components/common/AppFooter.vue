<template>
  <footer>
    <navigation-links></navigation-links>
    <div class="credits">Site by <a :href="author.hyperlink">{{ author.name }}</a></div>
  </footer>
</template>

<script>
export default {
  name: 'app-footer',
  props: ['author']
}
</script>

<style lang="stylus">
</style>
