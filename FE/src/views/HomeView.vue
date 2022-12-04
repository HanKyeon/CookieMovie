<template>
  <div id="home">
    <!-- <printing-ticket /> -->
    <ranking-carousel />
    <br />
    <br />
    <h2 class="text-left ms-5 ps-5" v-if="username">
      {{ username }}님과 취향이 비슷한 사람들이 좋아하는 영화예요.
    </h2>
    <h2 class="text-left ms-5 ps-5" v-else>
      랜덤 영화
      <v-btn @click="pushLogin">
        로그인하고 취향 맞춤 영화 추천 받기
        <v-icon large>mdi-arrow-top-right-thick</v-icon>
      </v-btn>
    </h2>
    <movie-recommendations />
  </div>
</template>

<script>
// import PrintingTicket from "../components/PrintingTicket.vue"
import MovieRecommendations from "../components/MovieRecommendations.vue"
import RankingCarousel from "@/components/rankingCarousel.vue"
// import axios from "axios"
// @ is an alias to /src
export default {
  name: "HomeView",
  data() {
    return {}
  },
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  components: {
    RankingCarousel,
    // PrintingTicket,
    MovieRecommendations,
  },
  methods: {
    pushLogin() {
      this.$router.push({ name: "login" })
    },
  },
  mounted() {
    document.getElementById("navbar").style = "display: flex !important;"
  },
}
</script>
<style>
.theme--light.v-input--switch .v-input--switch__track {
  color: "primary";
}
</style>
