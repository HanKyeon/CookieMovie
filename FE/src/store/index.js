import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import router from "@/router"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: null,
    username: null,
    userData: null,
  },
  getters: {},
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    SAVE_USERNAME(state, username) {
      state.username = username
    },
    SAVE_USERDATA(state, userData) {
      state.userData = userData
      state.userData.articles.reverse()
      state.userData.collections.reverse()
      state.userData.reviews.reverse()
    },
    LOGOUT(state) {
      state.token = null
      state.username = null
      state.userData = null
    },
  },
  actions: {
    getUserData(context, username) {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/detail/${username}/`,
        headers: {},
        data: {},
      }).then((res) => {
        context.commit("SAVE_USERDATA", res.data)
      })
    },
    pushMovieDetail(context, mov_id) {
      router.push({ name: "movie", params: { movie_id: mov_id } })
    },
    pushUserDetail(context, usnm) {
      router.push({ name: "profile", params: { username: usnm } })
    },
  },
  modules: {},
})
