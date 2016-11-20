<template>
  <div class="price">
    <div class="base" :class="{old: price.discount}">
        <span class="currency">{{ price.currency }}</span>
        <span class="base">{{ price.base }}</span>
        per
        <span class="unit">{{ price.unit }}</span>        
    </div>
    <div class="discount" v-if="price.discount">
        <span class="currency">{{ price.currency }}</span>
        <span class="base">{{ price.discount }}</span>
        per
        <span class="unit">{{ price.unit }}</span>        
    </div>
  </div>
</template>

<script>
export default {
  name: 'price',
  props: ['price']
}
</script>

<style lang="stylus">
</style>
