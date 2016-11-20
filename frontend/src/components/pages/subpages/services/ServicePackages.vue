<template>
  <div class="service-packages">
    <h3>Service Packages</h3>
    <package-description v-for="servicePackage in packages" :servicePackage="servicePackage"></package-description>
    <p class="note">{{ note }}</p>    
  </div>
</template>

<script>
import PackageDescription from './components/PackageDescription.vue'

export default {
  name: 'service-packages',
  props: ['packages', 'note'],
  components: {
    'package-description': PackageDescription
  }
}
</script>

<style lang="stylus">
</style>
