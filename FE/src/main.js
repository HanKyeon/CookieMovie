import "@babel/polyfill"
import "mutationobserver-shim"
import Vue from "vue"
import "./plugins/bootstrap-vue"
import App from "./App.vue"
import store from "./store"
import router from "./router"
import VueAwesomeSwiper from "vue-awesome-swiper"
import "swiper/css/swiper.css"
import vuetify from "./plugins/vuetify"
import LazyYoutube from "vue-lazytube"

Vue.component("LazyYoutube", LazyYoutube)
Vue.use(VueAwesomeSwiper)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app")
