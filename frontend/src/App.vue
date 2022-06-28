<template>
<div>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Peter Park</a>
    </div>
    
  </nav>
  <plates-view/>
</div>
</template>

<script>
import PlatesView from './components/PlatesView.vue'

export default {
  name: 'App',
  components: {
    PlatesView
  }
}
</script>

<style>
</style>
