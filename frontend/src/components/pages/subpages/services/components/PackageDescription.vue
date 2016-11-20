<template>
  <div class="package-description">
    <h4>{{ servicePackage.name }}</h4>
    <ul>
        <li v-for="service in servicePackage.services">{{ service.name }}</li>
    </ul>
    <div class="note" v-if="servicePackage.note">{{ servicePackage.note }}</div>
    <Price :price="servicePackage.price"></Price>
  </div>
</template>

<script>
export default {
  name: 'package-description',
  props: ['servicePackage']
}
</script>

<style lang="stylus">
</style>
