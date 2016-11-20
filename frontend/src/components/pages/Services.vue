<template>
  <main>
    <h2>ServicesPage</h2>
    <general-work-description :stages="services.stages"></general-work-description>
    <service-packages :packages="services.packages" :note="services.packages_global_note"></service-packages>
    <additional-services :services="services.additional_services"></additional-services>
  </main>
</template>

<script>
import GeneralWorkDescription from './subpages/services/GeneralWorkDescription.vue'
import ServicePackages from './subpages/services/ServicePackages.vue'
import AdditionalServices from './subpages/services/AdditionalServices.vue'

export default {
  name: 'services-page',
  components: {
    'general-work-description': GeneralWorkDescription,
    'service-packages': ServicePackages,
    'additional-services': AdditionalServices
  },
  computed: {
    'services': function () {
        return this.$store.state.services;
    }
  }
}
</script>

<style lang="stylus">
</style>