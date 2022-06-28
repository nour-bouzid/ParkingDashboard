<template>
<div class="container">
  <div class="wrapper">
    <legend>Add New Plate</legend>
    <div class="form-group">
      <label class="form-label mt-4">Plate</label>
      <input v-model="form.plate" type="text" class="form-control" placeholder="Enter Plate">
    </div>

    <div class="form-group">
      <label class="form-label mt-4">Owner</label>
      <input v-model="form.owner" type="text" class="form-control" placeholder="Enter Owner">
    </div>
  
    <div class="form-group">
      <label class="form-label mt-4">Start date</label>
      <datepicker v-model="form.startDate"  placeholder="Enter Start Date"/>
    </div>

    <div class="form-group">
      <label class="form-label mt-4">End date</label>
      <datepicker v-model="form.endDate"  placeholder="Enter End Date"/>
    </div>

    <button type="submit" class="btn btn-primary mt-4" @click="onSubmit">Submit</button>
  </div>
  <div class="separator">
  </div>
  <div class="wrapper-items">
    <legend>Plates</legend>
    <div class="list-group">
      <a href="#" v-for="plate in plates" :key="plate.plate" class="list-group-item list-group-item-action flex-column align-items-start">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">{{plate.plate}}</h5>
        </div>
        <p class="mb-1">Owner: {{plate.owner}}</p>
        <p class="mb-1">Start Date: {{plate.start_date}}</p>
        <p class="mb-1">End Date: {{plate.end_date}}</p>
      </a>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import Datepicker from 'vuejs-datepicker';

export default {
  name: 'PlatesView',
  components: {
    Datepicker
  },
  data() {
    return {
      plates: [],
      form: {
        plate: '',
        owner: '',
        start_date: new Date(),
        end_date: new Date(),
      }
    }
  },
  async mounted(){
    try {
      const res = await axios.get('http://localhost:5000/plate');
      this.plates = res.data;
      console.log('get response', res.data)
    } catch (err) {
      console.error(err)
    }
  },
  methods: {
    async onSubmit(){
      this.form.start_date = this.form.start_date.toISOString().split('.')[0]+"Z"
      this.form.end_date = this.form.end_date.toISOString().split('.')[0]+"Z"
      console.log(JSON.parse(JSON.stringify(this.form)))
      try {
        const resp = await axios.post('http://localhost:5000/plate', JSON.parse(JSON.stringify(this.form)));
        console.log(resp.data);
      } catch (err) {
        console.error(err);
      }
    }
  }
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
