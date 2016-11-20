<template>
  <div class="additional-services">
    <h3>Additional Services</h3> 
    <div class="additional-service" v-for="service in services">
        <h4>{{ service.name }}</h4>
        <p v-show="service.description_markdown">{{ service.description_markdown }}</p>
        <price :price="service.price"></price>
    </div>
  </div>
</template>

<script>
export default {
  name: 'service-packages',
  props: ['services']
}
</script>

<style lang="stylus">
</style>
