<template>
<div class="container">
  <div class="wrapper">
    <legend>Add New Plate</legend>
    <div class="form-group">
      <label class="form-label mt-4">Plate</label>
      <input type="text" class="form-control" aria-describedby="emailHelp" placeholder="Enter Plate">
    </div>

    <div class="form-group">
      <label class="form-label mt-4">Owner</label>
      <input type="text" class="form-control" aria-describedby="emailHelp" placeholder="Enter Plate">
    </div>

    <div class="form-group">
      <label class="form-label mt-4">Start date</label>
      <input type="text" class="form-control" aria-describedby="emailHelp" placeholder="Enter Plate">
    </div>

    <div class="form-group">
      <label class="form-label mt-4">End date</label>
      <input type="text" class="form-control" aria-describedby="emailHelp" placeholder="Enter Plate">
    </div>

    <button type="submit" class="btn btn-primary mt-4">Submit</button>
  </div>
  <div class="separator">
  </div>
  <div class="wrapper-items">
    <legend>Plates</legend>
    <div class="list-group">
      <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">List group item heading</h5>
        </div>
        <p class="mb-1">Owner:</p>
        <p class="mb-1">Start Date:</p>
        <p class="mb-1">End Date:</p>
      </a>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'PlatesView',
}
</script>

<style scoped>
.container {
  display: flex; /* or inline-flex */
  flex-direction: row;
  justify-content: space-between;
}
.separator {
  margin-top: 60px;
  width: 2px;
  height: 550px;
  border: 1px solid #78C2AD;
}
.wrapper{
  width: 650px;
  height: 650px;
  margin-top: 60px;
  margin-right: 20px;
}
.wrapper-items{
  width: 650px;
  height: 650px;
  margin-top: 60px;
  margin-left: 20px;
}
</style>
