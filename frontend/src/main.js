import Vue from 'vue'
import App from './App.vue'
import "bootstrap";
import "../node_modules/bootswatch/dist/minty/bootstrap.min.css";
import "jquery";
import "popper.js";
import axios from 'vue-axios';

Vue.use(axios)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
