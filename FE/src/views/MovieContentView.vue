<template>
  <div class="movie-content">
    <h1>여기는 컨텐츠 치치</h1>
    <v-row>
      <v-col cols="2" offset="10">
        <v-switch
          v-model="onlyUnwatched"
          :label="onlyUnwatched ? '안 본 영화만 보기' : '전체 영화 보기'"
          inset
          color="primary"
        ></v-switch>
      </v-col>
    </v-row>
    <movie-list :onlyUnwatched="onlyUnwatched" />
  </div>
</template>

<script>
import MovieList from "../components/MovieList.vue"
// @ is an alias to /src

export default {
  components: { MovieList },
  name: "MovieContentView",
  data() {
    return {
      onlyUnwatched: false,
    }
  },
}
</script>
