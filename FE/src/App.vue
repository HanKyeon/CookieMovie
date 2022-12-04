<template>
  <v-app fluid id="app" class="p-0 m-0">
    <b-row
      id="navbar"
      class="d-flex flex justify-content-between align-items-center m-0"
    >
      <router-link
        :to="{ name: 'home' }"
        id="logo"
        class="fs-s1 mx-3 indigo no-underline hover-underline"
        ><img
          src="https://cdn-icons-png.flaticon.com/512/6241/6241230.png"
        />COOKIE MOVIE</router-link
      >
      <div
        id="nav-links"
        class="hidden d-flex sm-w-100pc md-flex md-flex-row md-justify-end align-items-center"
      >
        <router-link
          :to="{ name: 'movies' }"
          class="fs-s1 mx-3 indigo no-underline hover-underline"
          >MOVIES</router-link
        >
        |
        <router-link
          :to="{ name: 'feed' }"
          class="fs-s1 mx-3 indigo no-underline hover-underline"
          >FEED</router-link
        >
        |
        <a
          v-if="username"
          :to="{
            name: 'profile',
            params: { username: username },
          }"
          class="fs-s1 mx-3 indigo no-underline hover-underline"
          @click.prevent="pushProfile"
        >
          <div>
            <img
              :src="`http://127.0.0.1:8000/static/default_img/ndg.png`"
              alt=""
              style="height: 38px; weight: 38px; border-radius: 100%"
            />
            <span class="mr-auto">{{ username }}</span>
          </div>
        </a>
        <a
          v-if="!username"
          :to="{
            name: 'profile',
            params: { username: username },
          }"
          class="fs-s1 mx-3 indigo no-underline hover-underline"
        >
          <div>
            <span class="mr-auto">PROFILE</span>
          </div>
        </a>
        |
        <router-link
          class="fw-600 no-underline mx-3"
          :to="{ name: 'login' }"
          v-if="!username"
          >JOIN</router-link
        >
        <a
          class="fw-600 no-underline mx-3"
          v-if="username"
          @click.prevent="logout"
          >LOGOUT</a
        >
      </div>
    </b-row>
    <b-row style="height: 90vh; margin: 0">
      <router-view class="w-100" style="height: 93vh" />
      <!--  -->
    </b-row>
  </v-app>
</template>

<!-- <script src="https://unpkg.com/vue-slick-carousel"></script> -->

<script>
// @ is an alias to /src
// import VueSlickCarousel from "vue-slick-carousel"
// import "vue-slick-carousel/dist/vue-slick-carousel.css";
// optional style for arrows & dots
// import "vue-slick-carousel/dist/vue-slick-carousel-theme.css"

export default {
  name: "App",
  // components: { VueSlickCarousel },
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  methods: {
    logout() {
      this.$store.commit("LOGOUT")
      this.$router.push({ name: "home" })
    },
    pushProfile() {
      this.$router.push({
        name: "profile",
        params: { username: this.username },
      })
    },
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@500;600;700&display=swap");
@font-face {
  font-family: "LINESeedKR-Bd";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2")
    format("woff2");
  font-weight: 100;
  font-style: normal;
}
@font-face {
  font-family: "Cafe24Danjunghae";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Danjunghae.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "NanumBarunpen";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumBarunpen.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "InfinitySans-RegularA1";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/InfinitySans-RegularA1.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "MICEGothic Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2206-01@1.0/MICEGothic Bold.woff2")
    format("woff2");
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: "GoyangIlsan";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/GoyangIlsan.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@import url("https://fonts.googleapis.com/css?family=Black+Han+Sans:400");
@import url("https://fonts.googleapis.com/css?family=Black+Han+Sans&display=swap&subset=korean");

.v-application {
  font-family: "MICEGothic Bold" !important;
}
.v-application .indigo {
  background-color: transparent !important;
  border-color: transparent !important;
}
.v-application--wrap {
  min-height: 100%;
}
.theme--dark.v-application {
  background: black;
  color: white;
}
html,
body {
  width: 100vw;
  height: 100vh;
}
body {
  background-color: black !important;
  font-family: "MICEGothic Bold";
  font-weight: 100;
  letter-spacing: 0.09em;
  color: white;
  box-sizing: border-box;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* background-color: #081521; */
}
#navbar {
  font-family: "Black Han Sans", sans-serif;
  color: rgba(255, 238, 0, 0.842) !important;
  font-size: 1rem;
  padding-inline: 1.2rem;
}
#navbar a {
  color: rgb(255, 251, 198) !important;
  background-color: transparent !important;
  border-color: transparent !important;
  cursor: pointer;
}
#nav-links.router-link-exact-active {
  color: rgba(255, 238, 0, 0.842) !important;
}
#logo img {
  width: 4rem;
  height: 7vh;
  margin-inline: 0.8rem;
  margin-right: -0.4rem;
}
#logo {
  font-size: 1.8rem;
}
.paragraph {
  font-family: "GoyangIlsan";
  text-align: left;
}
</style>
