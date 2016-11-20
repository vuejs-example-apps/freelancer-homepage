<template>
  <div class="general-work-description">
    <h3>General Work Description</h3>
    <div v-for="stage in stages">
        <h4>{{ stage.caption }}</h4>            
        <p>{{ stage.descripton }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'general-work-description',
  props: ['stages']
}
</script>

<style lang="stylus">
</style>
