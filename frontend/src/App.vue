<template>
<div>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Peter Park</a>
      <form class="d-flex">
        <input class="form-control me-sm-2" type="text" placeholder="Search">
        <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
      </form>
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
