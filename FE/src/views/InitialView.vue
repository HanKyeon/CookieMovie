<template>
  <div id="initial" @mousewheel="pushLogin">
    <div class="row h-100">
      <div class="col-7 offset-1 align-self-center text-left">
        <h1 style="font-size: 120px">Cookie Movie</h1>
        <h5 style="font-size: 30px">여운을 나누는 영화 커뮤니티</h5>
      </div>
      <div class="col-2 align-self-center">
        <v-btn
          x-large
          color="amber"
          dark
          elevation="20"
          style="width: 200px; height: 100px; font-size: 30px"
          @click="pushLogin"
        >
          Join Us
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InitialView",
  methods: {
    pushLogin() {
      this.$router.push({ name: "login" })
    },
  },
  mounted() {
    document.getElementById("navbar").style = "display: none !important"
    document.getElementById("initial").style = "height: 100vh;"
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Bowlby+One+SC&display=swap");
#initial {
  /* height: 150vh; */
  background-image: url("https://www.themoviedb.org/t/p/original/2cQMVHBaP1wK0UBX5SGDahB3lp3.jpg");
  background-size: cover;
}
#initial h1 {
  font-family: "Bowlby One SC";
}
#initial h5 {
  font-family: "GoyangIlsan";
  font-weight: bold;
  color: beige;
}
</style>
