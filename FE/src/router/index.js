import Vue from "vue"
import VueRouter from "vue-router"
import InitialView from "../views/InitialView.vue"
import HomeView from "../views/HomeView.vue"
import MovieView from "../views/MovieView.vue"
import MovieContentView from "../views/MovieContentView.vue"
import ProfileView from "../views/ProfileView.vue"
import FeedView from "../views/FeedView.vue"
import LoginView from "../views/LoginView.vue"
import ArticleView from "../views/ArticleView.vue"
// import { store } from "@/store/index"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "initial",
    component: InitialView,
  },
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/movie/:movie_id",
    name: "movie",
    // // route level code-splitting
    // // this generates a separate chunk (about.[hash].js) for this route
    // // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/MovieView.vue')
    component: MovieView,
  },
  {
    path: "/feed",
    name: "feed",
    component: FeedView,
  },
  {
    path: "/article/:article_id",
    name: "article",
    component: ArticleView,
  },
  {
    path: "/profile/:username",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/movies",
    name: "movies",
    component: MovieContentView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
    // beforeEnter(to, from, next) {
    //   if (store.state.token) {
    //     console.log(store.state.token)
    //     console.log(to, from, next)
    //   }
    // },
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
