<template>
  <main>
    <h2>{{ bio.title }}</h2>
    <img :src="bio.image">
    <p>{{ bio.text }}</p>    
  </main>
</template>

<script>
export default {
  name: 'bio-page',
  computed: {
    'bio': function () {
      return this.$store.state.texts.about_me;
    }
  }
}
</script>

<style lang="stylus">
</style>