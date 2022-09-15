<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/download.png">
    <ConstituentsWeights msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ConstituentsWeights from '@/components/ConstituentsWeights.vue';

export default {
  name: 'HomeView',
  components: {
    ConstituentsWeights
}
}
</script>
